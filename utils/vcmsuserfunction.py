import os,sys,traceback
import datetime,time
import collections,math,re,hashlib
from flask import render_template,session
from utils.jsonloader import Jsonloader
from utils.htmlbuilder import HtmlBuilder
from utils.vcmslogin import VcmsLogin
from utils.vcmsdbagent import VcmsDbAgent

class VcmsUserFunction :

    return_value = {"code":0,"message":"","data":{}}
    __max_show_data = 100

    def __init__(self) :
        pass

    def get_main_ui(self,page_settings) :
        self.__reset_return_value()
        tab_list = [
                   VcmsLogin().get_change_self_pwd(page_settings),
                   self.get_company_service_list(page_settings,int(session["company_sn"])),
                   self.get_company_product_list(page_settings,0,1),
                   self.get_system_announcement_list(page_settings,1),
                   self.get_system_announcement_by_board_hash(page_settings,None)
                   ]
        return tab_list

    def get_company_service_list(self,page_settings,company_sn = 0) :
        self.__reset_return_value()
        company_sn = int(session["company_sn"])
        html = ""
        page_settings["company_service_tab"] = 2
        if company_sn > 0 :
            page_settings["company_sn"] = company_sn
            page_settings["company_product_tab"] = 3
            page_settings["service_list"] = VcmsDbAgent()._get_company_service_data(company_sn)
            html = render_template("tab_ui/vcms_admin_company_service.tpl",data = page_settings)
        return html

    def get_company_product_list(self,page_settings,service_sn = 0,pages = 1) :
        self.__reset_return_value()
        html = ""
        company_sn = int(session["company_sn"])
        branch_sn = int(session["company_branch_sn"])
        max_page_show_data = self.__max_show_data
        max_pages = 1
        vcms_db_agent = VcmsDbAgent()
        db_data_cnt = vcms_db_agent._get_company_service_product_enabled_cnt(company_sn,service_sn)
        if db_data_cnt > 0 :
            max_pages = math.ceil(db_data_cnt/max_page_show_data)
        if int(pages) == 0 :
            pages = 1
        if int(pages) >= max_pages :
            pages = max_pages
        offset = (int(pages) - 1) * max_page_show_data
        page_settings["service_sn"] = service_sn
        page_settings["pages"] = pages
        page_settings["product_list"] = vcms_db_agent._get_company_service_product_enabled_data(company_sn,
                                                                                                service_sn,
                                                                                                max_page_show_data,
                                                                                                offset,
                                                                                                branch_sn)
        base_url = page_settings["company_product_url"]
        pagination_setting = {
                              "base_url" : page_settings["company_product_url"],
                              "tab_sn" : 3,
                              "data_sn" : service_sn,
                              "bind_class" : "company_product",
                              "direct_page" : pages,
                              "max_page" : max_pages,
                              "go_text" : page_settings["go_text"]
                             }
        page_settings["pagination"] = HtmlBuilder().pagination(base_url,pagination_setting)
        html = render_template("tab_ui/vcms_user_company_product.tpl",data = page_settings)
        return html

    def set_company_branch_product_status(self,page_settings,parameter_dict) :
        self.__reset_return_value()
        company_sn = int(session["company_sn"])
        branch_sn = int(session["company_branch_sn"])
        page_sn = 1
        enabled = 0
        deprecated = 0
        if parameter_dict.get("enabled") is not None :
            enabled = int(parameter_dict.get("enabled"))
        if parameter_dict.get("page_sn") is not None :
            page_sn = parameter_dict.get("page_sn")
        vcms_db_agent = VcmsDbAgent()
        data_cnt = 0
        success_cnt = 0
        for row in parameter_dict.getlist("data_sn[]") :
            data_cnt += 1
            product_info = vcms_db_agent._get_product_data(company_sn,int(row))
            service_sn = int(product_info["service_sn"])
            if vcms_db_agent._get_company_branch_product_settings_data(company_sn,service_sn,branch_sn,int(row)) > 0 :
                if vcms_db_agent._upd_company_branch_product_settings(company_sn,service_sn,branch_sn,int(row),enabled) > 0 :
                    success_cnt += 1
            else :
                if vcms_db_agent._add_company_branch_product_settings(company_sn,service_sn,branch_sn,int(row)) > 0 :
                    success_cnt += 1
        if data_cnt > 0 and data_cnt == success_cnt :
            self.return_value["data"] = self.get_company_product_list(page_settings,service_sn,page_sn)
            self.return_value["message"] = page_settings["success_text"]
            self.return_value["code"] = 1                  
        return self.return_value  

    def get_system_announcement_list(self,page_settings,pages = 1) :
        self.__reset_return_value()
        company_sn = int(session["company_sn"])
        page_settings["company_sn"] = company_sn
        page_settings["current_language"] = session["language"]
        page_settings["system_announcement_tab"] = 4
        page_settings["add_system_announcement_tab"] = 5
        page_settings["pages"] = pages
        publish_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        max_page_show_data = self.__max_show_data
        max_pages = 1
        vcms_db_agent = VcmsDbAgent()
        db_data_cnt = vcms_db_agent._get_all_enabled_system_announcement_cnt(publish_time)
        if db_data_cnt > 0 :
            max_pages = math.ceil(db_data_cnt/max_page_show_data)
        if int(pages) == 0 :
            pages = 1
        if int(pages) >= max_pages :
            pages = max_pages
        offset = (int(pages) - 1) * max_page_show_data
        page_settings["announcement_list"] = vcms_db_agent._get_all_enabled_system_announcement_data(publish_time,max_page_show_data,offset)
        base_url = page_settings["system_announcement_url"]
        pagination_setting = {
                              "base_url" : page_settings["system_announcement_url"],
                              "tab_sn" : 4,
                              "data_sn" : "0",
                              "bind_class" : "back_system_announcement",
                              "direct_page" : pages,
                              "max_page" : max_pages,
                              "go_text" : page_settings["go_text"]
                             }
        page_settings["pagination"] = HtmlBuilder().pagination(base_url,pagination_setting)
        return render_template("tab_ui/vcms_system_announcement.tpl",data = page_settings)

    def get_system_announcement_by_board_hash(self,page_settings,parameter_dict) :
        self.__reset_return_value()
        pages = 1
        html = ""
        if parameter_dict is not None :
            if parameter_dict.get("pages") is not None :
                pages = parameter_dict.get("pages")
            vcms_db_agent = VcmsDbAgent()
            page_settings["system_announcement_tab"] = 4
            page_settings["add_system_announcement_tab"] = 5
            page_settings["pages"] = pages
            page_settings["announcement_list"] = vcms_db_agent._get_all_system_announcement_detail_data(parameter_dict.get("data_sn"))[session["language"]]
            page_settings["publish_time"] = str(vcms_db_agent._get_system_announcement_data_by_board_hash(parameter_dict.get("data_sn"))["publish_time"]).replace(" 00:00:00","")
            html = render_template("tab_ui/vcms_system_announcement_detail.tpl",data = page_settings)
        return html

    def __reset_return_value(self) :
        self.return_value["code"] = 0
        self.return_value["message"] = ""
        self.return_value["data"] = {}
