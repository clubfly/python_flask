from flask import jsonify,render_template,session,escape,request
from utils.htmlbuilder import HtmlBuilder
from utils.vcmsengineerfunction import VcmsEngineerFunction
from utils.vcmsadminfunction import VcmsAdminFunction

def vcms_company_product_image(self,functions,actions,html_template,page_settings,parameter_dict):
    if session["user_rank_sn"] == 3 :
        pages = 1
        if parameter_dict.get("pages") is not None :
            pages = int(parameter_dict.get("pages"))
        return VcmsAdminFunction().get_company_product_image_list(page_settings,int(parameter_dict.get("data_sn")),pages)
    return ""
