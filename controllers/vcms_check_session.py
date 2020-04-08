from flask import jsonify,render_template,session,escape,redirect,make_response
from utils.htmlbuilder import HtmlBuilder

def vcms_check_session(self,functions,actions,html_template,page_settings,parameter_dict) :
    return_data = {"code":1,"message":"","data":{}}
    if "admin_id" not in session :
        return_data = {"code":0,"message":page_settings["session_expire_error"],"data":{}}
    return jsonify(return_data)
