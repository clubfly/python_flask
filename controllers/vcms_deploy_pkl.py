from flask import jsonify,render_template,session,escape,redirect,request
from utils.htmlbuilder import HtmlBuilder
from utils.vcmsadminfunction import VcmsAdminFunction
import requests,json

def vcms_deploy_pkl(self,functions,actions,html_template,page_settings,parameter_dict) :
    return_data = {}
    service_sn = int(actions)
    if session["user_rank_sn"] == 3 :
        return_data = VcmsAdminFunction().deploy_pkl_file_to_server(page_settings,service_sn)
        self.logger.info("on demand : "+str(service_sn))
        self.logger.info(return_data)
    return jsonify(return_data)
