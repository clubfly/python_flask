from flask import render_template,session,escape,request
from utils.htmlbuilder import HtmlBuilder

def vcms_test(self,functions,actions,html_template,page_settings,parameter_dict):
    html = HtmlBuilder()
    html_data = html.getHeaderFooterHtml(page_settings,1)
    return render_template(html_template,header_footer_data = html_data,data = page_settings)
