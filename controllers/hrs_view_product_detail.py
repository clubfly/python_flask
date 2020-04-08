from flask import render_template,session,escape,request
from utils.htmlbuilder import HtmlBuilder
from utils.hrs import Hrs

def hrs_view_product_detail(self,functions,actions,html_template,page_settings,parameter_dict):
    html = HtmlBuilder()
    html_data = html.getHeaderFooterHtml(page_settings,1)
    pages = 1
    if parameter_dict.get("pages") is not None :
        pages = int(parameter_dict.get("pages"))
    hrs = Hrs()
    token = actions
    page_settings["token"] = token
    base_url = page_settings["hrs_view_product_detail_url"] + token
    product_info = hrs.get_company_product_list(actions,parameter_dict,pages)
    pagination_setting = {
                          "base_url" : base_url,
                          "direct_page" : product_info["pages"],
                          "max_page" : product_info["max_pages"],
                          "service_sn" : product_info["service_sn"]
                         }
    page_settings["company_name"] = product_info["company_name"]
    page_settings["service_sn"] = product_info["service_sn"]
    page_settings["product_list"] = product_info["product_list"]
    page_settings["pagination"] = html.pagination2(base_url,pagination_setting)
    return render_template(html_template,header_footer_data = html_data,data = page_settings)
