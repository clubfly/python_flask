from flask import render_template,session,escape,redirect,make_response
from utils.htmlbuilder import HtmlBuilder
from utils.vcmslogin import VcmsLogin

def vcms_acc_login(self,functions,actions,html_template,page_settings,parameter_dict) :
    user_data = {
                 "account":parameter_dict.get("account"),
                 "password":parameter_dict.get("password")
                }
    return_data = VcmsLogin().login_by_account(user_data["account"],user_data["password"])
    if int(return_data["code"]) == 1 :
        self.logger.info(return_data["data"])
        for key,value in return_data["data"].items() :
            session[key] = value
        #session.permanent = True
        return redirect(page_settings["main_url"])
    return redirect(page_settings["login_url"])
