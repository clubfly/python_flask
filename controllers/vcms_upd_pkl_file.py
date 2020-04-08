from flask import jsonify,render_template,session,escape,redirect,request
from utils.htmlbuilder import HtmlBuilder
from utils.vcmsadminfunction import VcmsAdminFunction
import requests,json

def vcms_upd_pkl_file(self,functions,actions,html_template,page_settings,parameter_dict) :
    return_data = {}
    service_sn = int(actions)
    if session["user_rank_sn"] == 3 :
        return_data = VcmsAdminFunction().set_pkl_file_to_test_server(page_settings,service_sn)
    return jsonify(return_data)
