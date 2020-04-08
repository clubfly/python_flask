from flask import render_template,session,escape,request
from utils.htmlbuilder import HtmlBuilder
from utils.vcmsengineerfunction import VcmsEngineerFunction
from utils.vcmsrootfunction import VcmsRootFunction

def vcms_company_service(self,functions,actions,html_template,page_settings,parameter_dict):
    if session["user_rank_sn"] == 2 :
        return VcmsRootFunction().get_company_service_list(page_settings,int(parameter_dict.get("data_sn")))
    return ""
