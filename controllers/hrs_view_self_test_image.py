from flask import render_template,session,escape,request
from utils.htmlbuilder import HtmlBuilder
from utils.hrs import Hrs

def hrs_view_self_test_image(self,functions,actions,html_template,page_settings,parameter_dict):
    html = HtmlBuilder()
    html_data = html.getHeaderFooterHtml(page_settings,1)
    pages = 1
    if parameter_dict.get("pages") is not None :
        pages = int(parameter_dict.get("pages"))
    hrs = Hrs()
    company_sn = parameter_dict.get("company_sn")
    image_total,return_data = hrs.get_company_self_test_images(actions,company_sn,parameter_dict,pages)
    page_settings["image_list"] = return_data
    page_settings["image_total"] = image_total 
    page_settings["token"] = hrs.get_token()
    page_settings["company_name"] = hrs.get_company_info(int(company_sn))["company_name"]
    page_settings["forder"] = parameter_dict.get("folder")
    return render_template(html_template,header_footer_data = html_data,data = page_settings)
