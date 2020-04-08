from flask import jsonify,render_template,session,escape,request
from utils.htmlbuilder import HtmlBuilder
from utils.vcmsengineerfunction import VcmsEngineerFunction
from utils.vcmsrootfunction import VcmsRootFunction

def vcms_upd_system_announcement(self,functions,actions,html_template,page_settings,parameter_dict):
    return_data = {}
    if session["user_rank_sn"] == 2 :
        return_data = VcmsRootFunction().set_system_announcement(page_settings,parameter_dict)
    return jsonify(return_data)
