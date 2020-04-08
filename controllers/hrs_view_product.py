from flask import render_template,session,escape,request
from utils.htmlbuilder import HtmlBuilder
from utils.hrs import Hrs

def hrs_view_product(self,functions,actions,html_template,page_settings,parameter_dict):
    html = HtmlBuilder()
    html_data = html.getHeaderFooterHtml(page_settings,1)
    hrs = Hrs()
    page_settings["company_list"] = hrs.get_company_list(actions) 
    page_settings["token"] = hrs.get_token()
    return render_template(html_template,header_footer_data = html_data,data = page_settings)
