from flask import jsonify,render_template,session,escape,request
from utils.htmlbuilder import HtmlBuilder
from utils.vcmsengineerfunction import VcmsEngineerFunction
from utils.vcmsrootfunction import VcmsRootFunction
from utils.vcmsadminfunction import VcmsAdminFunction
from utils.vcmsuserfunction import VcmsUserFunction

def vcms_system_announcement(self,functions,actions,html_template,page_settings,parameter_dict):
    pages = 1
    if parameter_dict.get("pages") is not None :
        pages = int(parameter_dict.get("pages"))
    if session["user_rank_sn"] == 2 :
        return VcmsRootFunction().get_system_announcement_list(page_settings,pages)
    if session["user_rank_sn"] == 3 :
        return VcmsAdminFunction().get_system_announcement_list(page_settings,pages)
    if session["user_rank_sn"] == 4 :
        return VcmsUserFunction().get_system_announcement_list(page_settings,pages)
    return ""
