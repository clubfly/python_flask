from flask import jsonify,render_template,session,escape,redirect,make_response
from utils.htmlbuilder import HtmlBuilder
from utils.vcmsadminfunction import VcmsAdminFunction

def vcms_check_sku(self,functions,actions,html_template,page_settings,parameter_dict) :
    service_sn = parameter_dict.get("service_sn")
    return_data = VcmsAdminFunction().get_product_by_sku(actions,service_sn)
    return jsonify(return_data)
