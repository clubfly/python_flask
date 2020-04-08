from flask import jsonify,render_template,session,escape,request
from utils.htmlbuilder import HtmlBuilder
from utils.vcmslogin import VcmsLogin

def vcms_upd_self_pwd(self,functions,actions,html_template,page_settings,parameter_dict) :
    return_data = VcmsLogin().change_self_pwd(page_settings,parameter_dict)
    return jsonify(return_data)
