from flask import jsonify,render_template,session,escape,request
from utils.htmlbuilder import HtmlBuilder
from utils.vcmsadminfunction import VcmsAdminFunction

def vcms_upload_product_image(self,functions,actions,html_template,page_settings,parameter_dict) :
    return_data = {}
    if session["user_rank_sn"] == 3 :
        return_data = VcmsAdminFunction().set_company_product_image(page_settings,parameter_dict,request.files)
    return jsonify(return_data)
