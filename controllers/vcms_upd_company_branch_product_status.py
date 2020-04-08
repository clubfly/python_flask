from flask import jsonify,render_template,session,escape,redirect,make_response
from utils.htmlbuilder import HtmlBuilder
from utils.vcmsuserfunction import VcmsUserFunction

def vcms_upd_company_branch_product_status(self,functions,actions,html_template,page_settings,parameter_dict) :
    return_data = {}
    if session["user_rank_sn"] == 4 :
        return_data = VcmsUserFunction().set_company_branch_product_status(page_settings,parameter_dict)
    return jsonify(return_data)
