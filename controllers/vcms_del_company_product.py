from flask import jsonify,render_template,session,escape,request
from utils.htmlbuilder import HtmlBuilder
from utils.vcmsengineerfunction import VcmsEngineerFunction
from utils.vcmsadminfunction import VcmsAdminFunction

def vcms_del_company_product(self,functions,actions,html_template,page_settings,parameter_dict):
    return_data = {}
    if session["user_rank_sn"] == 3 :
        return_data = VcmsAdminFunction().del_company_product(page_settings,parameter_dict)
    return jsonify(return_data)
