from flask import jsonify,render_template,session,escape,request
from utils.htmlbuilder import HtmlBuilder
from utils.vcmsrootfunction import VcmsRootFunction
from utils.vcmsadminfunction import VcmsAdminFunction

def vcms_account_pwd(self,functions,actions,html_template,page_settings,parameter_dict) :
    if session["user_rank_sn"] == 2 :
        return VcmsRootFunction().get_change_account_pwd(page_settings,int(parameter_dict.get("data_sn")))
    if session["user_rank_sn"] == 3 :
        return VcmsAdminFunction().get_change_account_pwd(page_settings,int(parameter_dict.get("data_sn")))
    return ""
