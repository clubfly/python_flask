from flask import render_template,session,escape,request
from utils.htmlbuilder import HtmlBuilder
from utils.vcmsengineerfunction import VcmsEngineerFunction
from utils.vcmsrootfunction import VcmsRootFunction
from utils.vcmsadminfunction import VcmsAdminFunction
from utils.vcmsuserfunction import VcmsUserFunction

def vcms_company_product(self,functions,actions,html_template,page_settings,parameter_dict) :
    pages = 1
    if parameter_dict.get("pages") is not None :
        pages = int(parameter_dict.get("pages"))
    #if session["user_rank_sn"] == 2 :
    #    return VcmsRootFunction().get_company_product_list(page_settings,int(parameter_dict.get("data_sn")))
    if session["user_rank_sn"] == 3 :
        search = {
                  "product_sn" : parameter_dict.get("product_sn"),
                  "product_name" : parameter_dict.get("product_name"),
                  "abbreviation" : parameter_dict.get("abbreviation"),
                  "barcode" : parameter_dict.get("barcode"),
                  "ct_start_date" : parameter_dict.get("ct_start_date"),
                  "ct_end_date" : parameter_dict.get("ct_end_date"),
                  "ut_start_date" : parameter_dict.get("ut_start_date"),
                  "ut_end_date" : parameter_dict.get("ut_end_date"),
                  "image_cnt" : parameter_dict.get("image_cnt"),
                  "enabled" : parameter_dict.get("enabled") 
                 }
        return VcmsAdminFunction().get_company_product_list(page_settings,int(parameter_dict.get("data_sn")),pages,search)
    if session["user_rank_sn"] == 4 :
        return VcmsUserFunction().get_company_product_list(page_settings,int(parameter_dict.get("data_sn")),pages)
    return ""
