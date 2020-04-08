from flask import render_template,session,escape,request
from utils.htmlbuilder import HtmlBuilder
from utils.vcmsengineerfunction import VcmsEngineerFunction
from utils.vcmsrootfunction import VcmsRootFunction
from utils.vcmsadminfunction import VcmsAdminFunction
from utils.vcmsuserfunction import VcmsUserFunction

def vcms_product_csv_log(self,functions,actions,html_template,page_settings,parameter_dict) :
    #if session["user_rank_sn"] == 2 :
    #    return VcmsRootFunction().get_company_batch_product_list(page_settings,int(parameter_dict.get("data_sn")))
    if session["user_rank_sn"] == 3 :
        return VcmsAdminFunction().get_product_csv_log_list(page_settings,int(parameter_dict.get("data_sn")))
    #if session["user_rank_sn"] == 4 :
    #    return VcmsUserFunction().get_company_batch_product_list(page_settings,int(parameter_dict.get("data_sn")))
    return ""
