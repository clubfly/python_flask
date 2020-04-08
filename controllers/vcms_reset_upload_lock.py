from flask import jsonify,render_template,session,escape,redirect,make_response
from utils.htmlbuilder import HtmlBuilder
from utils.vcmsrootfunction import VcmsRootFunction

def vcms_reset_upload_lock(self,functions,actions,html_template,page_settings,parameter_dict) :
    return_data = {}
    lock_token = str(actions)
    return_data = VcmsRootFunction().set_uploading_images_lock_status(page_settings,lock_token,parameter_dict)
    return jsonify(return_data)
