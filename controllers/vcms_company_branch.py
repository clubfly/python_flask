from flask import jsonify,render_template,session,escape,request
from utils.htmlbuilder import HtmlBuilder
from utils.vcmsengineerfunction import VcmsEngineerFunction
from utils.vcmsadminfunction import VcmsAdminFunction

def vcms_company_branch(self,functions,actions,html_template,page_settings,parameter_dict):
    if session["user_rank_sn"] == 3 :
        return VcmsAdminFunction().get_company_branch_list(page_settings,int(parameter_dict.get("data_sn")))
    return ""
