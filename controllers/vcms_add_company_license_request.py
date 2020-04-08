from flask import jsonify,render_template,session,escape,request
from utils.htmlbuilder import HtmlBuilder
from utils.vcmsengineerfunction import VcmsEngineerFunction
from utils.vcmsrootfunction import VcmsRootFunction

def vcms_add_company_license_request(self,functions,actions,html_template,page_settings,parameter_dict):
    return_data = {}
    if session["user_rank_sn"] == 2 :
        print(parameter_dict)
        return_data = VcmsRootFunction().get_edit_company_license_request(page_settings,int(parameter_dict.get("data_sn")))
    return jsonify(return_data)