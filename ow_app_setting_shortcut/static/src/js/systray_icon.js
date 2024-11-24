/** @odoo-module **/
import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";
import { Component } from "@odoo/owl";

class SystrayIcon extends Component {
   setup() {
       super.setup(...arguments);
       this.action = useService("action");
   }
   _openAppView() {
            this.action.doAction({
                type: "ir.actions.act_window",
                name: "Apps",
                res_model: "ir.module.module",
                view_mode: "kanban",
                views: [[false, "kanban"]],
                target: "current", // Open in the same tab
            });
           }
    _openSettingView(){
        this.action.doAction({
            type: "ir.actions.act_window",
            name: "Settings",
            res_model: "res.config.settings",
            view_mode: "form",
            views: [[false, "form"]],
            target: "current", // Open in a modal
        });
    }
}
   SystrayIcon.template = "systray_icon";
   export const systrayItem = { Component: SystrayIcon,};
   registry.category("systray").add("SystrayIcon", systrayItem, { sequence: 40 });
