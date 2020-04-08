from flask import render_template,session,escape
import math,datetime
import collections

class HtmlBuilder :

    def __init__(self) :
        pass

    def getHeaderFooterHtml(self,page_settings,header_hide = 0) :
        page_settings["admin_id"] = 0
        page_settings["account"] = ""
        page_settings["header_hide"] = header_hide
        page_settings["permission_js"] = ""
        page_settings["seeds"] = datetime.datetime.now().strftime("%Y%m%d%H")
        if "admin_id" in session :
            page_settings["admin_id"] = session["admin_id"]
            page_settings["account"] = session["account"]
            page_settings["user_rank_sn"] = session["user_rank_sn"]
            page_settings["permission_js"] = session["permission_js"]
        header_html = render_template("common/header.tpl",data = page_settings)
        footer_html = render_template("common/footer.tpl",data = page_settings)
        return {"header_html" : header_html,"footer_html" : footer_html}

    def pagination(self,base_url,pagination_setting) :
        pagination = {}
        max_navigation_seed = 10
        direct_page = int(pagination_setting["direct_page"])
        max_page = pagination_setting["max_page"]
        if direct_page <= 0 :
            direct_page = 1
        min = math.ceil(direct_page/max_navigation_seed)
        max = math.ceil(max_page/max_navigation_seed)
        max_navigation = min * max_navigation_seed
        min_navigation = max_navigation - (max_navigation_seed - 1)
        if max_navigation > max_page :
            max_navigation = max_page
        bar_link = collections.OrderedDict()
        for i in range(min_navigation,(max_navigation+1)) :
            active = ""
            if i == direct_page :
                active = "active"
            bar_link[i] = {
                           "active" : active,
                           "name" : str(i)
                          }
        left_show = 1
        right_show = 1
        if min == 1 :
            left_show = 0
        if max == min:
            right_show = 0
        pagination["tab_sn"] = pagination_setting["tab_sn"]
        pagination["data_sn"] = pagination_setting["data_sn"]
        pagination["bind_class"] = pagination_setting["bind_class"]
        pagination["base_url"] = base_url
        pagination["bar"] = bar_link
        pagination["left_show"] = left_show
        pagination["right_show"] = right_show
        pagination["reduce"] = direct_page - 1
        pagination["add"] = direct_page + 1
        pagination["max_page"] = max_page
        pagination["go_text"] = pagination_setting["go_text"]
        pagination["search"] = ""
        if "search" in pagination_setting :
            pagination["search"] = pagination_setting["search"]
        return render_template("common/pagination.tpl",data = pagination)

    def pagination2(self,base_url,pagination_setting,tab_show = "") :
        pagination = {}
        max_navigation_seed = 10
        direct_page = int(pagination_setting["direct_page"])
        max_page = pagination_setting["max_page"]
        if direct_page <= 0 :
            direct_page = 1
        min = math.ceil(direct_page/max_navigation_seed)
        max = math.ceil(max_page/max_navigation_seed)
        max_navigation = min * max_navigation_seed
        min_navigation = max_navigation - (max_navigation_seed - 1)
        if max_navigation > max_page :
            max_navigation = max_page
        bar_link = collections.OrderedDict()
        for i in range(min_navigation,(max_navigation+1)) :
            active = ""
            if i == direct_page :
                active = "active"
            bar_link[i] = {
                           "active" : active,
                           "name" : str(i)
                          }
        left_show = 1
        right_show = 1
        if min == 1 :
            left_show = 0
        if max == min:
            right_show = 0
        pagination["base_url"] = base_url
        pagination["bar"] = bar_link
        pagination["left_show"] = left_show
        pagination["right_show"] = right_show
        pagination["reduce"] = direct_page - 1
        pagination["add"] = direct_page + 1
        pagination["max_page"] = max_page
        pagination["service_sn"] = pagination_setting["service_sn"]
        return render_template("common/pagination2.tpl",data = pagination)
