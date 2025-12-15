########################################################################
#                                                                      #
#     ------------------------ODOO WAVES----------------------         #
#     --------------odoowaves.solution@gmail.com--------------         #
#                                                                      #
########################################################################
from odoo import models, fields, api
from odoo.http import request
from urllib.parse import urlencode
from odoo.exceptions import UserError
import requests, logging
from datetime import datetime
_logger = logging.getLogger(__name__)


STATE = [
    ('draft', 'Draft'),
    ('connected', 'Connected'),
    ('error', 'Error')
]

SCOPE = "https://www.googleapis.com/auth/business.manage"

class GoogleReviewIntegration(models.Model):
    _name = "google.review.integration"
    _description = "Google Review Integration"

    name = fields.Char(string="Name")
    client_id = fields.Char(string="Client ID")
    client_secret = fields.Char(string="Client Secret")
    access_token = fields.Char(string="Access Token")
    refresh_token = fields.Char(string="Refresh Token")
    redirect_url = fields.Char(string='Redirect URL', compute='_compute_redirect_url', readonly=True, copy=False)
    state = fields.Selection(STATE, default='draft')

    account_ids = fields.Many2many('google.account', string="Account")
    location_id  = fields.Many2many('google.account.location', string="location")
    location_ids = fields.One2many("google.account.location", "review_integration_id", string="Locations")

    def base_url(self):
        return self.env['ir.config_parameter'].sudo().get_param('web.base.url')

    def _compute_redirect_url(self):
        for rec in self:
            rec.redirect_url = rec.base_url() + "/redirect"

    def google_connection(self):
        client_id = self.client_id
        redirect_url = self.redirect_url
        if redirect_url:
            if 'http' == redirect_url.split(":")[0]:
                redirect_url = redirect_url.replace("http", "https")
        request.session['instance_id'] = self.id
        base_url = "https://accounts.google.com/o/oauth2/v2/auth"
        params = {
            'response_type': 'code',
            'client_id': client_id,
            'redirect_uri': redirect_url,
            'scope': SCOPE,
            'access_type': 'offline',
            'prompt': 'consent',
        }
        full_url = f"{base_url}?{urlencode(params)}"
        return {
            'type': 'ir.actions.act_url',
            'target': 'self',
            'url': full_url,
        }

    def test_google_connection(self, env=None):
        if env:
            self = env['google.review.integration'].search([], limit=1)
        if not self.refresh_token:
            raise  UserError("First Click on the Connect Gmail Button")
        url = "https://oauth2.googleapis.com/token"
        data = {
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'refresh_token': self.refresh_token,
            'grant_type': 'refresh_token',
        }
        response = requests.post('https://oauth2.googleapis.com/token', data=data)
        if response.ok:
            access_token = response.json().get('access_token')
            self.access_token = access_token
        else:
            print("Error:", response.json())


    def get_accounts(self):
        url = "https://mybusinessbusinessinformation.googleapis.com/v1/accounts"
        headers = {
            'Authorization': f'Bearer {self.access_token}',
            'Content-Type': 'application/json',
        }
        resp = requests.get(url=url, headers=headers)
        if resp.ok and resp.status_code in [200]:
            accounts = resp.json().get('accounts',[])
            records = []
            for account in accounts:
                name = account.get('name')
                account_record = self.env['google.account'].search([('name','ilike',name)])
                if not account_record:
                    account_name = account.get('accountName')
                    role = account.get('role', False)
                    records.append({'name':name, 'account_name':account_name, 'role':role})
            if records:
                self.env['google.account'].create(records)
        else:
            raise UserError(resp.text)


    def get_locations(self):

        if not self.account_ids:
            raise UserError("Select at least one User Account")

        for account in self.account_ids:
            accountId = account.name.split('/')[1]
            url = f"https://mybusinessbusinessinformation.googleapis.com/v1/accounts/{accountId}/locations"
            headers = {
                "Authorization": f"Bearer {self.access_token}",
                "Accept": "application/json"
            }
            params = {
                "readMask": "name,title"
            }

            response = requests.get(url, headers=headers, params=params)
            if response.ok and response.status_code in [200]:
                locations = response.json().get('locations', [])
                records = []
                for location in locations:
                    name = location.get('name')
                    location_record = self.env['google.account.location'].search([('name','=',name)])
                    if not location_record:
                        title = location.get('title')
                        records.append({'name': name, 'title':title})
                if records:
                    self.env['google.account.location'].create(records)
            else:
                raise UserError(response.text)


    def set_to_draft(self):
        self.state = 'draft'

    def auto_reply_to_reviews(self, env=None):
        self = env['google.review.integration'].search([],limit=1)
        self.ensure_one()

        if not self.account_ids:
            raise UserError("Select a User Account")

        for account in self.account_ids:

            accountId = account.name.split('/')[1]

            headers = {
                "Authorization": f"Bearer {self.access_token}",
                "Accept": "application/json"
            }

            for location in self.location_id:
                if not location.last_updated_date:
                    continue
                locationId = location.name.split('/')[1]
                _logger.info(f"Fetching reviews for Location: {locationId}")

                base_url = f"https://mybusiness.googleapis.com/v4/accounts/{accountId}/locations/{locationId}/reviews"
                params = {
                    "orderBy": "updateTime desc",
                    "pageSize": 50,
                }


                next_page_token = None
                latest_update_time = location.last_updated_date

                while True:
                    if next_page_token:
                        params["pageToken"] = next_page_token

                    response = requests.get(base_url, headers=headers, params=params)
                    if response.status_code != 200:
                        _logger.error(f"Failed to fetch reviews for location {locationId}: {response.text}")
                        break

                    data = response.json()
                    reviews = data.get("reviews", [])

                    for review in reviews:
                        review_id = review.get("reviewId")
                        review_stars = review.get('starRating')
                        if review_stars in ['One', 'TWO']:
                            # body = (
                            #     "<p>Dear ,</p>"
                            #     f"<p>We have just received a new review with a low rating ({review_stars} star) "
                            #     f"from <strong>{review.get('reviewer').get('displayName')}</strong>.</p>"
                            #     f"<p>Review comment: \"{review.get('comment')}\"</p>"
                            #     f"<p>For the Location comment: \"{location.title}\"</p>"
                            #     "<p>We have just received a new review with a low rating.for the"
                            #     "Please review the feedback and respond to the client promptly.</p>"
                            #     "<p>Maintaining our service quality and reputation is important, so kindly address this at the earliest.</p>"
                            #     "<br/>"
                            #     "<p>Best regards,<br/>"
                            #     "Future Link Consultants Team</p>"
                            # )

                            # self.env['mail.mail'].create({
                            #     'subject': "Low-Rated Review Alert",
                            #     'body_html': body,
                            #     'email_from': "",
                            #     'email_to': "",
                            # }).send()
                            comment = f"Hello {review.get('reviewer').get('displayName')} . Thank you for taking the time to share your feedback. We sincerely apologize that our service did not meet your expectations. At Future Link Consultants, we set very high standards, and we are truly sorry that we fell short during your interaction with us. Client satisfaction is our top priority, and we would appreciate the opportunity to regain your trust. Please feel free to reach out to us at 📧 help@futurelinkconsultants.com or 📞 +91 99982 24688, and our team will be happy to assist you personally and resolve your concerns at the earliest. Your feedback is invaluable in helping us improve, and we are committed to restoring your confidence in our services. — Future Link Consultants Team"
                        elif review_stars in ['THREE']:
                            comment = f"Hello {review.get('reviewer').get('displayName')}, Thank you for sharing your feedback. We appreciate your input and are glad to have had the opportunity to serve you. Your feedback help us continue improving our services, and we look forward to providing an even better experience in the future. We’ll be reaching out to understand your concerns better and to see how we can enhance our service for you.  \n– Future Link Consultants Team"
                        elif review_stars in ['FOUR', 'FIVE']:
                            comment = f"Hello {review.get('reviewer').get('displayName')}, Thank you for your kind feedback. We are delighted to know that your experience with Future Link Consultants was positive and that our team could support you effectively. Your trust in our services is greatly valued, and your words encourage us to continue maintaining the highest standards of professionalism and personalized guidance. We remain committed to assisting you with any future needs and look forward to supporting you again. \n– Future Link Consultants Team"
                        update_time = review.get("updateTime")  # e.g. "2025-09-06T11:53:49.624503Z"
                        review_dt = datetime.strptime(update_time, "%Y-%m-%dT%H:%M:%S.%fZ")

                        if location.last_updated_date and review_dt <= location.last_updated_date:
                            _logger.info("No more new reviews to process for this location.")
                            next_page_token = None
                            break  # exit reviews loop

                        reply_url = f"{base_url}/{review_id}/reply"
                        payload = {"comment": comment}

                        reply_response = requests.put(reply_url, json=payload, headers=headers)
                        if reply_response.ok and reply_response.status_code in [200]:
                            _logger.info(f"Replied to review {review_id} (Location {locationId})")
                            review_model = self.env['google.location.review']
                            review_record = review_model.search([('reviewId','=',review_id)])
                            if not review_record:
                                review_model.create({
                                    'name': review.get('reviewer').get('displayName'),
                                    'reviewId': review_id,
                                    'rating': review.get('starRating'),
                                    'comment':review.get('comment'),
                                })
                        else:
                            _logger.error(f"Failed to reply review {review_id}: {reply_response.text}")

                        # Track latest update time for this location
                        if update_time:
                            review_dt = datetime.strptime(update_time, "%Y-%m-%dT%H:%M:%S.%fZ")
                            if not latest_update_time or review_dt > latest_update_time:
                                latest_update_time = review_dt

                    # Pagination
                    next_page_token = data.get("nextPageToken")
                    if not next_page_token:
                        break

                # Save per-location last update time
                if latest_update_time:
                    location.last_updated_date = latest_update_time
                    _logger.info(f"Last updated date for Location {locationId}: {latest_update_time}")