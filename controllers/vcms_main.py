from flask import render_template,session,escape,request
from utils.htmlbuilder import HtmlBuilder
from utils.vcmsengineerfunction import VcmsEngineerFunction
from utils.vcmsrootfunction import VcmsRootFunction
from utils.vcmsadminfunction import VcmsAdminFunction
from utils.vcmsuserfunction import VcmsUserFunction

def vcms_main(self,functions,actions,html_template,page_settings,parameter_dict):
    html_data = HtmlBuilder().getHeaderFooterHtml(page_settings)
    tab_ui = {}
    if session["user_rank_sn"] == 1 :
        tab_ui = VcmsEngineerFunction().get_main_ui(page_settings)
    if session["user_rank_sn"] == 2 :
        tab_ui = VcmsRootFunction().get_main_ui(page_settings)
    if session["user_rank_sn"] == 3 :
        tab_ui = VcmsAdminFunction().get_main_ui(page_settings)
    if session["user_rank_sn"] == 4 :
        tab_ui = VcmsUserFunction().get_main_ui(page_settings)
    page_settings["tab_ui"] = tab_ui
    return render_template(html_template,header_footer_data = html_data,data = page_settings)
