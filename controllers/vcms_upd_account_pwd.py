from flask import jsonify,render_template,session,escape,request
from utils.htmlbuilder import HtmlBuilder
from utils.vcmsengineerfunction import VcmsEngineerFunction
from utils.vcmsrootfunction import VcmsRootFunction
from utils.vcmsadminfunction import VcmsAdminFunction

def vcms_upd_account_pwd(self,functions,actions,html_template,page_settings,parameter_dict) :
    return_data = {}
    if session["user_rank_sn"] == 2 :
        return_data = VcmsRootFunction().change_account_pwd(page_settings,parameter_dict)
    if session["user_rank_sn"] == 3 :
        return_data = VcmsAdminFunction().change_account_pwd(page_settings,parameter_dict)
    return jsonify(return_data)
