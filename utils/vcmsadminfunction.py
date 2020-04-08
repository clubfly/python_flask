import os,sys,traceback
import datetime,time
import collections,math,re,hashlib,shutil,uuid,base64
from dateutil.relativedelta import relativedelta
from flask import render_template,session
from utils.jsonloader import Jsonloader
from werkzeug.utils import secure_filename
from utils.jsonloader import Jsonloader
from utils.htmlbuilder import HtmlBuilder
from utils.vcmslogin import VcmsLogin
from utils.vcmsdbagent import VcmsDbAgent
from system_service_models.embedding import Embedding
from system_service_models.csvmanage import Csvmanage

class VcmsAdminFunction :

    return_value = {"code":0,"message":"","data":{}}
    ALLOWED_EXTENSIONS = set(['bmp', 'tif', 'png', 'jpg', 'jpeg', 'gif'])
    __max_show_data = 100
    lock_token = "ee1aecfff2a34b1ab95198572337820e"

    def __init__(self) :
        #\u4e00-\u9fa5 (中文)
        #\x3130-\x318F (韓文)
        #\xAC00-\xD7A3 (韓文)
        #\u0800-\u4e00 (日文)
        pass

    def get_main_ui(self,page_settings) :
        self.__reset_return_value()
        tab_list = [
                   VcmsLogin().get_change_self_pwd(page_settings),
                   self.get_company_profile_list(page_settings,int(session["company_sn"])),
                   self.get_company_service_list(page_settings,int(session["company_sn"])),
                   self.get_company_branch_list(page_settings,int(session["company_sn"])),
                   self.get_edit_company_branch(page_settings,int(session["company_sn"])),
                   self.get_company_branch_account_list(page_settings,0),
                   self.get_edit_company_branch_account(page_settings,0),
                   self.get_change_account_pwd(page_settings,0),
                   self.get_company_product_list(page_settings,0,1,{}),
                   self.get_edit_company_product(page_settings,0,1),
                   self.get_company_product_image_list(page_settings,0,1),
                   self.get_self_recognition_test(page_settings,int(session["company_sn"]),0),
                   self.get_system_announcement_list(page_settings,1),
                   self.get_system_announcement_by_board_hash(page_settings,None),
                   self.get_company_batch_product_list(page_settings,0),
                   self.get_product_csv_log_list(page_settings,0),
                   self.get_product_image_csv_log_list(page_settings,0)
                   ]
        return tab_list

    def get_company_profile_list(self,page_settings,company_sn = 0) :
        self.__reset_return_value()
        company_sn = int(session["company_sn"])
        html = ""
        page_settings["company_profile_tab"] = 2
        if company_sn > 0 :
            page_settings["company_sn"] = company_sn
            page_settings["company_profile_list"] = VcmsDbAgent()._get_company_profile_data(int(company_sn))
            html = render_template("tab_ui/vcms_company_profile.tpl",data = page_settings)
        return html

    def get_company_service_list(self,page_settings,company_sn = 0) :
        self.__reset_return_value()
        company_sn = int(session["company_sn"])
        html = ""
        page_settings["company_service_tab"] = 3
        if company_sn > 0 :
            page_settings["company_sn"] = company_sn
            page_settings["company_product_tab"] = 9
            page_settings["self_test_tab"] = 12
            page_settings["service_list"] = VcmsDbAgent()._get_company_service_data(company_sn)
            html = render_template("tab_ui/vcms_admin_company_service.tpl",data = page_settings)
        return html

    def get_company_branch_list(self,page_settings,company_sn = 0) :
        self.__reset_return_value()
        company_sn = int(session["company_sn"])
        html = ""
        page_settings["add_company_branch_tab"] = 5
        page_settings["branch_account_manage_tab"] = 6
        if company_sn > 0 :
            page_settings["company_sn"] = company_sn
            page_settings["branch_list"] = VcmsDbAgent()._get_company_branch_data(company_sn)
            html = render_template("tab_ui/vcms_admin_company_branch.tpl",data = page_settings)
        return html

    def get_company_branch_account_list(self,page_settings,branch_sn = 0) :
        self.__reset_return_value()
        company_sn = int(session["company_sn"])
        html = ""
        if company_sn > 0 :
            page_settings["company_sn"] = company_sn
            page_settings["branch_sn"] = branch_sn
            page_settings["branch_account_manage_tab"] = 6
            page_settings["add_company_branch_account_tab"] = 7
            page_settings["company_account_tab"] = 8
            page_settings["account_list"] = VcmsDbAgent()._get_company_branch_account_data(company_sn,branch_sn)
            html = render_template("tab_ui/vcms_admin_company_branch_account.tpl",data = page_settings)
        return html

    def get_edit_company_branch(self,page_settings,company_sn = 0) :
        self.__reset_return_value()
        company_sn = int(session["company_sn"])
        html = ""
        if company_sn > 0 :
            page_settings["company_sn"] = company_sn
            page_settings["company_branch_tab"] = 4
            html = render_template("tab_ui/vcms_edit_company_branch.tpl",data = page_settings)
        return html

    def get_edit_company_branch_account(self,page_settings,branch_sn = 0) :
        self.__reset_return_value()
        company_sn = int(session["company_sn"])
        html = ""
        if company_sn > 0 :
            page_settings["company_sn"] = company_sn
            page_settings["branch_sn"] = branch_sn
            page_settings["branch_account_manage_tab"] = 6
            page_settings["company_name"] = VcmsDbAgent()._get_all_company_data()[company_sn]["company_name"]
            html = render_template("tab_ui/vcms_edit_company_branch_account.tpl",data = page_settings)
        return html

    def get_change_account_pwd(self,page_settings,user_sn = 0) :
        self.__reset_return_value()
        html = ""
        page_settings["user_sn"] = user_sn
        page_settings["company_account_tab"] = 6
        if user_sn > 0 :
            user_info = VcmsDbAgent()._get_account_data(user_sn)
            page_settings["branch_sn"] = user_info["company_branch_sn"]
            page_settings["company_sn"] = user_info["company_sn"]
            page_settings["account"] = user_info["account"]
            if int(user_info["company_sn"]) == int(session["company_sn"]) :
                html = render_template("tab_ui/vcms_edit_company_branch_account_pwd.tpl",data = page_settings)
        return html

    def get_company_product_list(self,page_settings,service_sn = 0,pages = 1,search = {}) :
        self.__reset_return_value()
        html = ""
        company_sn = int(session["company_sn"])
        max_page_show_data = self.__max_show_data
        max_pages = 1
        vcms_db_agent = VcmsDbAgent()
        db_data_cnt = vcms_db_agent._get_company_service_product_cnt(company_sn,service_sn,search)
        if db_data_cnt > 0 :
            max_pages = math.ceil(db_data_cnt/max_page_show_data)
        if int(pages) == 0 :
            pages = 1
        if int(pages) >= max_pages :
            pages = max_pages
        offset = (int(pages) - 1) * max_page_show_data
        page_settings["company_product_tab"] = 9
        page_settings["add_company_product_tab"] = 10
        page_settings["company_product_image_tab"] = 11
        page_settings["add_batch_company_product_tab"] = 15
        page_settings["product_csv_log_tab"] = 16
        page_settings["service_sn"] = service_sn
        page_settings["pages"] = pages
        page_settings["product_list"] = vcms_db_agent._get_company_service_product_data(company_sn,service_sn,search,max_page_show_data,offset)
        page_settings["product_totals"] = db_data_cnt
        page_settings["product_enabled_totals"] = vcms_db_agent._get_company_service_enabled_product_cnt(company_sn,service_sn,search)
        page_settings["image_totals"] = vcms_db_agent._get_company_service_product_image_cnt(company_sn,service_sn)
        page_settings["image_enabled_totals"] = vcms_db_agent._get_company_service_enabled_product_image_cnt(company_sn,service_sn)
        base_url = page_settings["company_product_url"]
        search_seed = ""
        for k,v in search.items() :
          if v is None :
              v = ""
          search_seed += str(k)+"="+str(v)+"&"
        pagination_setting = {
                              "base_url" : page_settings["company_product_url"],
                              "tab_sn" : 9,
                              "data_sn" : service_sn,
                              "bind_class" : "company_product",
                              "direct_page" : pages,
                              "max_page" : max_pages,
                              "go_text" : page_settings["go_text"],
                              "search" : search_seed
                             }
        page_settings["pagination"] = HtmlBuilder().pagination(base_url,pagination_setting)
        html = render_template("tab_ui/vcms_admin_company_product.tpl",data = page_settings)
        return html

    def get_edit_company_product(self,page_settings,service_sn = 0,pages = 1) :
        self.__reset_return_value()
        company_sn = int(session["company_sn"])
        html = ""
        page_settings["company_product_tab"] = 9
        print (service_sn)
        if company_sn > 0 :
            service_list = VcmsDbAgent()._get_company_service_data(company_sn)
            page_settings["company_sn"] = company_sn
            page_settings["service_sn"] = service_sn
            if service_sn > 0 :
                page_settings["system_service_sn"] = service_list[service_sn]["service_sn"]
            page_settings["product_sn"] = 0
            page_settings["pages"] = pages
            html = render_template("tab_ui/vcms_edit_company_product.tpl",data = page_settings)
        return html

    def get_edit_product(self,page_settings,product_sn = 0,pages = 1) :
        self.__reset_return_value()
        company_sn = int(session["company_sn"])
        html = ""
        page_settings["company_product_tab"] = 9
        page_settings["add_company_product_tab"] = 10
        if company_sn > 0 :
            vcms_db_agent = VcmsDbAgent()
            product_info = vcms_db_agent._get_product_data(company_sn,int(product_sn))
            page_settings.update(product_info)
            page_settings["company_sn"] = company_sn
            page_settings["service_sn"] = product_info["service_sn"]
            page_settings["product_sn"] = product_info["sn"]
            service_list = vcms_db_agent._get_company_service_data(company_sn)
            page_settings["system_service_sn"] = service_list[int(product_info["service_sn"])]["service_sn"]
            page_settings["pages"] = pages
            html = render_template("tab_ui/vcms_edit_company_product.tpl",data = page_settings)
        return html

    def get_company_product_image_list(self,page_settings,product_sn = 0,pages = 1) :
        self.__reset_return_value()
        company_sn = int(session["company_sn"])
        max_page_show_data = self.__max_show_data
        max_pages = 1
        vcms_db_agent = VcmsDbAgent()
        db_data_cnt = vcms_db_agent._get_company_product_image_cnt(company_sn,int(product_sn))
        if db_data_cnt > 0 :
            max_pages = math.ceil(db_data_cnt/max_page_show_data)
        if int(pages) == 0 :
            pages = 1
        if int(pages) >= max_pages :
            pages = max_pages
        offset = (int(pages) - 1) * max_page_show_data
        html = ""
        page_settings["company_product_tab"] = 9
        page_settings["company_product_image_tab"] = 11
        page_settings["company_sn"] = company_sn
        page_settings["image_lock"] = vcms_db_agent._get_system_lock_for_uploading_images(self.lock_token)["lock_mark"]
        if int(product_sn) > 0 :
            product_info = vcms_db_agent._get_product_data(company_sn,int(product_sn))
            page_settings["product_enabled"] = int(product_info["enabled"])
            page_settings["service_sn"] = product_info["service_sn"]
            page_settings["product_sn"] = product_info["sn"]
            page_settings["product_name"] = product_info["product_name"]
            page_settings["image_list"] = vcms_db_agent._get_company_product_image_data(company_sn,product_sn,max_page_show_data,offset)
            page_settings["pages"] = pages
            base_url = page_settings["company_product_image_url"]
            pagination_setting = {
                                  "base_url" : page_settings["company_product_image_url"],
                                  "tab_sn" : page_settings["company_product_image_tab"],
                                  "data_sn" : product_info["sn"],
                                  "bind_class" : "company_product_image",
                                  "direct_page" : pages,
                                  "max_page" : max_pages,
                                  "go_text" : page_settings["go_text"]
                                 }
            page_settings["pagination"] = HtmlBuilder().pagination(base_url,pagination_setting)
            page_settings["db_data_cnt"] = db_data_cnt
            page_settings["image_limit"] = vcms_db_agent._get_company_service_data(company_sn)[int(product_info["service_sn"])]["per_product_image_cnt"]
            html = render_template("tab_ui/vcms_admin_company_product_image.tpl",data = page_settings)
        return html

    def get_self_recognition_test(self,page_settings,company_sn,service_sn) :
        html = render_template("tab_ui/vcms_self_test.tpl",data = page_settings)
        return html

    def get_company_batch_product_list(self,page_settings,service_sn) :
        self.__reset_return_value()
        company_sn = int(session["company_sn"])
        html = ""
        if company_sn > 0 :
            page_settings["company_sn"] = company_sn
            page_settings["service_sn"] = service_sn
            page_settings["company_product_tab"] = 9
            page_settings["product_csv_log_tab"] = 16
            page_settings["product_image_csv_log_tab"] = 17
            html = render_template("tab_ui/vcms_admin_batch_product.tpl",data = page_settings)
        return html

    def get_product_csv_log_list(self,page_settings,service_sn) :
        self.__reset_return_value()
        company_sn = int(session["company_sn"])
        html = ""
        if company_sn > 0 :
            page_settings["company_sn"] = company_sn
            page_settings["service_sn"] = service_sn
            page_settings["company_product_tab"] = 9
            page_settings["product_csv_log_tab"] = 16
            page_settings["product_image_csv_log_tab"] = 17
            page_settings["log_list"] = Csvmanage().get_product_csv_log(company_sn,service_sn)
            html = render_template("tab_ui/vcms_admin_product_csv_log.tpl",data = page_settings)
        return html
    
    def get_product_image_csv_log_list(self,page_settings,service_sn) :
        self.__reset_return_value()
        company_sn = int(session["company_sn"])
        html = ""
        if company_sn > 0 :
            page_settings["company_sn"] = company_sn
            page_settings["service_sn"] = service_sn
            page_settings["company_product_tab"] = 9
            page_settings["product_csv_log_tab"] = 16
            page_settings["product_image_csv_log_tab"] = 17
            page_settings["log_list"] = {}
            html = render_template("tab_ui/vcms_admin_product_image_csv_log.tpl",data = page_settings)
        return html

    def set_company_profile(self,page_settings,parameter_dict) :
        self.__reset_return_value()
        data_check = {
                      "company_no_error" : "",
                      "company_address_error" : "",
                      "company_tel_error" : "",
                      "company_contact_error" : "",
                      "company_contact_tel_error" : "",
                      "company_contact_email_error" : ""
                     }
        company_sn = int(session["company_sn"])
        if company_sn is not None and int(company_sn) > 0 :
            error_data = 0
            company_no = parameter_dict.get("company_no")
            if company_no is not None and company_no != "" :
                if re.compile("^[a-zAz0-9\-]*$").match(company_no) is None :
                    error_data += 1
                    data_check["company_no_error"] = page_settings["number_error_text"]
            company_address = parameter_dict.get("company_address")
            if company_address is not None and company_address != "" :
                if re.compile("^[a-zA-Z0-9_\u4e00-\u9fa5\u0800-\u4e00\-\.\,\(\)#@]+$").match(company_address) is None :
                    error_data += 1
                    data_check["company_address_error"] = page_settings["symbol_format_error_text"]
            company_tel = parameter_dict.get("company_tel")
            if company_tel is not None and company_tel != "" :
                if re.compile("^[0-9\-\(\)#]*$").match(company_tel) is None :
                    error_data += 1
                    data_check["company_tel_error"] = page_settings["number_error_text"]
            company_contact = parameter_dict.get("company_contact")
            if company_contact is not None and company_contact != "" :
                if re.compile("^[a-zA-Z_\u4e00-\u9fa5\u0800-\u4e00\-]+$").match(company_contact) is None :
                    error_data += 1
                    data_check["company_contact_error"] = page_settings["utf8_words_only_error_text"]
            company_contact_tel = parameter_dict.get("company_contact_tel")
            if company_contact_tel is not None and company_contact_tel != "" :
                if re.compile("^[0-9_\-\(\)#]*$").match(company_contact_tel) is None :
                    error_data += 1
                    data_check["company_contact_tel_error"] = page_settings["number_error_text"]
            company_contact_email = parameter_dict.get("company_contact_email")
            if company_contact_email is not None and company_contact_email != "" :
                if re.compile("^[a-zA-Z0-9_\.]{1,63}@[a-zA-Z0-9]{2,63}\\.[a-zA-Z]{2,63}(\\.[a-zA-Z]{2,63})?$").match(company_contact_email) is None :
                    error_data += 1
                    data_check["company_contact_email_error"] = page_settings["email_format_error_text"]
            self.return_value["data"] = data_check
            if error_data == 0 :
                company_profile = {
                                   "company_no" : company_no,
                                   "company_address" : company_address,
                                   "company_tel" : company_tel,
                                   "company_contact" : company_contact,
                                   "company_contact_tel" : company_contact_tel,
                                   "company_contact_email" : company_contact_email
                                  }
                if VcmsDbAgent()._upd_company_profile_data(company_sn,company_profile) > 0 :
                    self.return_value["data"] = self.get_company_profile_list(page_settings,int(company_sn))
                    self.return_value["message"] = page_settings["success_text"]
                    self.return_value["code"] = 1
        return self.return_value

    def set_company_branch(self,page_settings,parameter_dict) :
        self.__reset_return_value()
        data_check = {
                      "branch_name_error" : ""
                     }
        error_data = 0
        company_sn = int(session["company_sn"])
        branch_name = parameter_dict.get("branch_name")
        vcms_db_agent = VcmsDbAgent()
        if vcms_db_agent._check_company_branch_data(company_sn,branch_name) == 1 :
            error_data += 1
            data_check["branch_name_error"] = page_settings["duplication_error_text"]
        else :
           branch_cnt = vcms_db_agent._get_company_branch_cnt(company_sn)
           max_branch = vcms_db_agent._get_all_company_data()[company_sn]["max_branch_cnt"]
           if branch_cnt >= max_branch :
               error_data += 1
               data_check["branch_name_error"] = page_settings["limitation_error"]
        self.return_value["data"] = data_check
        if error_data == 0 :
            if vcms_db_agent._add_company_branch_data(company_sn,branch_name) > 0 :
                self.return_value["data"] = self.get_company_branch_list(page_settings,int(company_sn))
                self.return_value["message"] = page_settings["success_text"]
                self.return_value["code"] = 1
        return self.return_value

    def set_company_branch_account(self,page_settings,parameter_dict) :
        self.__reset_return_value()
        data_check = {
                      "account_error" : page_settings["empty_cnt_error"],
                      "new_pwd_error" : page_settings["empty_cnt_error"],
                      "confirm_pwd_error" : page_settings["empty_cnt_error"]
                     }
        error_data = 0
        company_sn = int(session["company_sn"])
        vcms_db_agent = VcmsDbAgent()
        account = parameter_dict.get("account")
        if account is not None and account != "" :
            data_check["account_error"] = ""
            if re.compile("^[\w]+$").match(account) is None :
                error_data += 1
                data_check["account_error"] = page_settings["en_num_only_error_text"]
            else :
                if vcms_db_agent._check_account_data(account) == 1 :
                    error_data += 1
                    data_check["account_error"] = page_settings["account_exist_error_text"]
        else :
            error_data += 1
        new_password = parameter_dict.get("new_password")
        if new_password is not None and new_password != "" :
            data_check["new_pwd_error"] = ""
        else :
            error_data += 1
        confirm_password = parameter_dict.get("confirm_password")
        if confirm_password is not None and confirm_password != "" :
            data_check["confirm_pwd_error"] = ""
            if confirm_password != new_password :
                error_data += 1
                data_check["confirm_pwd_error"] = page_settings["confirm_pwd_error"]
        else :
            error_data += 1
        max_user = vcms_db_agent._get_all_company_data()[company_sn]["max_branch_user_cnt"]
        user_rank_sn = 4
        user_cnt = vcms_db_agent._get_company_rank_user_cnt(company_sn,user_rank_sn)
        if user_cnt >= max_user :
            error_data += 1
            data_check["account_error"] = page_settings["limitation_error"]
        self.return_value["data"] = data_check
        branch_sn = parameter_dict.get("branch_sn")
        if error_data == 0 :
            hash = hashlib.md5()
            hash.update(new_password.encode('utf-8'))
            pwd = str(hash.hexdigest())
            if vcms_db_agent._add_company_account_data(company_sn,account,pwd,user_rank_sn,int(branch_sn)) > 0 :
                self.return_value["data"] = self.get_company_branch_account_list(page_settings,int(branch_sn))
                self.return_value["message"] = page_settings["success_text"]
                self.return_value["code"] = 1
        return self.return_value

    def change_account_pwd(self,page_settings,parameter_dict) :
        self.__reset_return_value()
        data_check = {
                      "user_sn_error" : page_settings["empty_cnt_error"],
                      "npwd_error" : page_settings["empty_cnt_error"],
                      "cpwd_error" : page_settings["empty_cnt_error"]
                     }
        user_sn = parameter_dict.get("user_sn")
        new_password = parameter_dict.get("new_password")
        confirm_password = parameter_dict.get("confirm_password")
        vcms_db_agent = VcmsDbAgent()
        error_data = 0
        company_sn = int(session["company_sn"])
        branch_sn = 0
        if user_sn is not None and user_sn != "" :
            data_check["user_sn_error"] = ""
            if re.compile("^[\d]*$").match(user_sn) is None :
                error_data += 1
                data_check["user_sn_error"] = page_settings["user_sn_format_error"]
            else :
                user_info = vcms_db_agent._get_account_data(user_sn)
                if "admin_id" not in user_info :
                    error_data += 1
                    data_check["user_sn_error"] = page_settings["none_user_sn_error"]
                else :
                    branch_sn = int(user_info["company_branch_sn"])
        else :
            error_data += 1
        if new_password is not None and new_password != "" :
            data_check["npwd_error"] = ""
        else :
            error_data += 1
        if confirm_password is not None and confirm_password != "" :
            data_check["npwd_error"] = ""
            if confirm_password != new_password :
                error_data += 1
                data_check["cpwd_error"] = page_settings["confirm_pwd_error"]
        else :
            error_data += 1
        self.return_value["data"] = data_check
        if error_data == 0 :
            hash2 = hashlib.md5()
            hash2.update(new_password.encode('utf-8'))
            pwd = str(hash2.hexdigest())
            if vcms_db_agent._upd_account_pwd(user_sn,pwd) == 1 :
                self.return_value["data"] = self.get_company_branch_account_list(page_settings,branch_sn)
                self.return_value["message"] = page_settings["success_text"]
                self.return_value["code"] = 1
        return self.return_value

    def set_company_product(self,page_settings,parameter_dict,product_image_file) :
        self.__reset_return_value()
        data_check = {
                      "service_error" : "",
                      "thumbnail_error" : "",
                      "sku_error" : "",
                      "product_name_error" : "",
                      "abbreviation_error" : "",
                      "barcode_error" : ""
                     }
        company_sn = int(session["company_sn"])
        service_sn = parameter_dict.get("service_sn")
        error_data = 0
        print (parameter_dict)
        vcms_db_agent = VcmsDbAgent()
        if service_sn is not None and service_sn != "" :
            if vcms_db_agent._check_company_service(company_sn,int(service_sn)) == 0 :
                error_data += 1
                data_check["service_error"] = page_settings["service_invalid_error"]
        else :
            error_data += 1
            data_check["service_error"] = page_settings["service_invalid_error"]
        product_sn = parameter_dict.get("product_sn")
        if product_sn is not None :
            if int(product_sn) == 0 :
                product_cnt = vcms_db_agent._get_company_service_product_cnt(company_sn,int(service_sn),{})
                max_product_cnt = vcms_db_agent._get_company_service_data(company_sn)[int(service_sn)]["max_product_cnt"]     
                if int(product_cnt) >= int(max_product_cnt) :
                    error_data += 1
                    data_check["sku_error"] = page_settings["limitation_error"]
                    self.return_value["data"] = data_check
                    return self.return_value
        sku = parameter_dict.get("sku")
        if sku is not None and sku != "" :
            if re.compile("^[a-zA-Z0-9_\-]+$").match(sku) is None :
                error_data += 1
                data_check["sku_error"] = page_settings["en_num_only_error_text"]
        else :
            error_data += 1
            data_check["sku_error"] = page_settings["empty_cnt_error"]
        product_name = parameter_dict.get("product_name")
        if product_name is not None and product_name != "" :
            if re.compile("^[a-zA-Z0-9_\(\)\u4e00-\u9fa5\u0800-\u4e00\-\.#@\s\u3000]+$").match(product_name) is None :
                error_data += 1
                data_check["product_name_error"] = page_settings["symbol_format_error_text"]
        else :
            error_data += 1
            data_check["product_name_error"] = page_settings["empty_cnt_error"]
        abbreviation = parameter_dict.get("abbreviation")
        if abbreviation is not None and abbreviation != "" :
            if re.compile("^[a-zA-Z0-9_\(\)\u4e00-\u9fa5\u0800-\u4e00\-\.#@\s\u3000]+$").match(abbreviation) is None :
                error_data += 1
                data_check["abbreviation_error"] = page_settings["symbol_format_error_text"]
        barcode = parameter_dict.get("barcode")
        if barcode is not None and barcode != "" :
            if re.compile("^[a-zA-Z0-9]+$").match(barcode) is None :
                error_data += 1
                data_check["barcode_error"] = page_settings["en_num_only_error_text"]
        if product_sn is not None :
            if int(product_sn) == 0 :
                if "thumbnail" not in product_image_file :
                    error_data += 1
                    data_check["thumbnail_error"] = page_settings["thumbnail_empty_error"]
        categories = parameter_dict.get("category")
        category = None
        if categories is not None and categories != "" :
            category = categories
        self.return_value["data"] = data_check
        if error_data == 0 :   
            base_upload_path = "%s/%s/%s" % (os.getcwd(),"static","uploads") 
            if not os.path.exists(base_upload_path) :
                os.makedirs(base_upload_path)
            company_upload_path = "%s/%s" % (base_upload_path,company_sn)
            if not os.path.exists(company_upload_path) :
                os.makedirs(company_upload_path)
            image_file_path = "%s/%s" % (company_upload_path,service_sn)
            if not os.path.exists(image_file_path) :
                os.makedirs(image_file_path)
            thumbnail = ""
            for row in product_image_file.getlist("thumbnail") :
                if row and self.__allowed_file(row.filename) :
                    ori_image_file_name = str(row.filename)
                    filename = secure_filename(row.filename)
                    row.save(os.path.join(image_file_path, filename))
                    sys_image_file_name = str(uuid.uuid4()).replace("-","") + os.path.splitext(row.filename)[1]
                    thumbnail = os.path.join(image_file_path,sys_image_file_name)
                    shutil.move(os.path.join(image_file_path, filename),thumbnail)
                    thumbnail = thumbnail.replace(os.getcwd(),"")
            pages = 1
            if int(product_sn) == 0 :
                if vcms_db_agent._check_company_product_data(company_sn,service_sn,barcode,sku,product_name,abbreviation) == 0 :
                    if vcms_db_agent._add_company_product_data(company_sn,service_sn,barcode,sku,product_name,abbreviation,thumbnail,category) > 0 :
                        pages = 1
            else :
                pages = parameter_dict.get("pages")
                if vcms_db_agent._upd_company_product_data(company_sn,product_sn,barcode,sku,product_name,abbreviation,category) > 0 :
                    if thumbnail != "" :
                        if vcms_db_agent._upd_company_product_image_data(company_sn,product_sn,thumbnail) > 0 :
                            pages = parameter_dict.get("pages")
            self.return_value["data"] = self.get_company_product_list(page_settings,service_sn,int(pages),{})
            self.return_value["message"] = page_settings["success_text"]
            self.return_value["code"] = 1
        return self.return_value

    def set_company_product_status(self,page_settings,parameter_dict) :
        self.__reset_return_value()
        company_sn = int(session["company_sn"])
        product_sn = 0
        service_sn = 0
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
            if vcms_db_agent._upd_company_product_status_data(company_sn,int(row),enabled,deprecated) > 0 :
                vcms_db_agent._upd_company_product_image_feature_status_by_product(company_sn,int(row),enabled,deprecated)
                #vcms_db_agent._upd_company_product_image_status_by_product(company_sn,int(row),enabled)
                success_cnt += 1
                product_sn = int(row)
        if data_cnt > 0:
            product_info = vcms_db_agent._get_product_data(company_sn,int(product_sn))
            if "service_sn" in product_info :
                service_sn = int(product_info["service_sn"])
            self.return_value["data"] = self.get_company_product_list(page_settings,service_sn,page_sn,{})
            self.return_value["message"] = page_settings["success_text"]
            self.return_value["code"] = 1
        return self.return_value

    def del_company_product(self,page_settings,parameter_dict) :
        self.__reset_return_value()
        company_sn = int(session["company_sn"])
        product_sn = 0
        service_sn = 0
        page_sn = 1
        enabled = 0
        deprecated = 1
        if parameter_dict.get("page_sn") is not None :
            page_sn = parameter_dict.get("page_sn")
        vcms_db_agent = VcmsDbAgent()
        data_cnt = 0
        success_cnt = 0
        for row in parameter_dict.getlist("data_sn[]") :
            data_cnt += 1
            if data_cnt == 1 :
                product_info = vcms_db_agent._get_product_data(company_sn,int(row))
                if "service_sn" in product_info :
                    service_sn = int(product_info["service_sn"])
            if vcms_db_agent._upd_company_product_status_data(company_sn,int(row),enabled,deprecated) > 0 :
                vcms_db_agent._upd_company_product_image_feature_status_by_product(company_sn,int(row),enabled,deprecated)
                #vcms_db_agent._upd_company_product_image_status_by_product(company_sn,int(row),enabled)
                success_cnt += 1
                product_sn = int(row)
        if data_cnt > 0 and data_cnt == success_cnt :
            self.return_value["data"] = self.get_company_product_list(page_settings,service_sn,page_sn,{})
            self.return_value["message"] = page_settings["success_text"]
            self.return_value["code"] = 1
        return self.return_value

    def set_company_product_image(self,page_settings,parameter_dict,product_image_file) :
        self.__reset_return_value()
        data_check = {
                      "thumbnail_error" : ""
                     }
        company_sn = int(session["company_sn"])
        vcms_db_agent = VcmsDbAgent()
        lock_mark = vcms_db_agent._get_system_lock_for_uploading_images(self.lock_token)["lock_mark"]
        if int(lock_mark) == 1 :
            return self.return_value
        product_sn = parameter_dict.get("product_sn")
        product_info = vcms_db_agent._get_product_data(company_sn,int(product_sn))
        service_sn = int(product_info["service_sn"])
        db_data_cnt = vcms_db_agent._get_company_product_image_cnt(company_sn,int(product_sn))
        service_info = vcms_db_agent._get_company_service_data(company_sn)
        max_image_cnt = int(service_info[service_sn]["per_product_image_cnt"])
        error_data = 0
        if db_data_cnt >= max_image_cnt :
            error_data += 1
            data_check["thumbnail_error"] = page_settings["limitation_error"]
        self.return_value["data"] = data_check
        if error_data == 0 :
            i = db_data_cnt
            base_upload_path = "%s/%s/%s" % (os.getcwd(),"static","uploads")
            if not os.path.exists(base_upload_path) :
                os.makedirs(base_upload_path)
            company_upload_path = "%s/%s" % (base_upload_path,company_sn)
            if not os.path.exists(company_upload_path) :
                os.makedirs(company_upload_path)
            image_file_path = "%s/%s" % (company_upload_path,service_sn)
            if not os.path.exists(image_file_path) :
                os.makedirs(image_file_path)
            thumbnail = ""
            for row in product_image_file.getlist("thumbnail") :
                if row and self.__allowed_file(row.filename) :
                    if max_image_cnt > i :
                        ori_image_file_name = str(row.filename)
                        filename = secure_filename(row.filename)
                        row.save(os.path.join(image_file_path, filename))
                        sys_image_file_name = str(uuid.uuid4()).replace("-","") + os.path.splitext(row.filename)[1]
                        thumbnail = os.path.join(image_file_path,sys_image_file_name)
                        shutil.move(os.path.join(image_file_path, filename),thumbnail)
                        thumbnail = thumbnail.replace(os.getcwd(),"")
                        if vcms_db_agent._add_company_product_image_data(company_sn,service_sn,int(product_sn),thumbnail) > 0 :
                            i += 1
            image_totals = vcms_db_agent._get_company_product_image_cnt(company_sn,product_sn)
            if image_totals > 0 :
                vcms_db_agent._upd_company_product_image_totals(company_sn,product_sn,image_totals)
            self.return_value["data"] = self.get_company_product_image_list(page_settings,product_sn,1)
            self.return_value["message"] = page_settings["success_text"]
            self.return_value["code"] = 1
        return self.return_value

    def set_company_product_image_status(self,page_settings,parameter_dict) :
        self.__reset_return_value()
        company_sn = int(session["company_sn"])
        product_sn = parameter_dict.get("product_sn")
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
        product_info = vcms_db_agent._get_product_data(company_sn,product_sn)
        for row in parameter_dict.getlist("data_sn[]") :
            data_cnt += 1
            if int(product_info["enabled"]) == 0 :
                enabled = 0
            if vcms_db_agent._upd_company_product_image_status_data(company_sn,int(row),enabled,deprecated) > 0 :
                vcms_db_agent._upd_company_product_image_feature_status_by_image(company_sn,int(row),enabled,deprecated)
                success_cnt += 1
        if data_cnt > 0:
            self.return_value["data"] = self.get_company_product_image_list(page_settings,int(product_sn),page_sn)
            self.return_value["message"] = page_settings["success_text"]
            self.return_value["code"] = 1
        return self.return_value

    def del_company_product_image(self,page_settings,parameter_dict) :
        self.__reset_return_value()
        company_sn = int(session["company_sn"])
        product_sn = parameter_dict.get("product_sn")
        page_sn = 1
        enabled = 0
        deprecated = 1
        if parameter_dict.get("page_sn") is not None :
            page_sn = parameter_dict.get("page_sn")
        vcms_db_agent = VcmsDbAgent()
        data_cnt = 0
        success_cnt = 0
        for row in parameter_dict.getlist("data_sn[]") :
            data_cnt += 1
            if vcms_db_agent._upd_company_product_image_status_data(company_sn,int(row),enabled,deprecated) > 0 :
                vcms_db_agent._upd_company_product_image_feature_status_by_image(company_sn,int(row),enabled,deprecated)
                success_cnt += 1
        if data_cnt > 0 and data_cnt == success_cnt :
            image_totals = vcms_db_agent._get_company_product_image_cnt(company_sn,int(product_sn))
            vcms_db_agent._upd_company_product_image_totals(company_sn,int(product_sn),image_totals)
            self.return_value["data"] = self.get_company_product_image_list(page_settings,int(product_sn),page_sn)
            self.return_value["message"] = page_settings["success_text"]
            self.return_value["code"] = 1
        return self.return_value 

    def set_company_product_camera_image(self,page_settings,parameter_dict) :
        self.__reset_return_value()
        data_check = {
                      "thumbnail_error" : ""
                     }
        company_sn = int(session["company_sn"])
        vcms_db_agent = VcmsDbAgent()
        lock_mark = vcms_db_agent._get_system_lock_for_uploading_images(self.lock_token)["lock_mark"]
        if int(lock_mark) == 1 :
            return self.return_value
        product_sn = parameter_dict.get("data_sn")
        product_info = vcms_db_agent._get_product_data(company_sn,int(product_sn))
        service_sn = int(product_info["service_sn"])
        db_data_cnt = vcms_db_agent._get_company_product_image_cnt(company_sn,int(product_sn))
        service_info = vcms_db_agent._get_company_service_data(company_sn)
        max_image_cnt = int(service_info[service_sn]["per_product_image_cnt"])
        error_data = 0
        if db_data_cnt >= max_image_cnt :
            error_data += 1
            data_check["thumbnail_error"] = page_settings["limitation_error"]
        self.return_value["data"] = data_check
        if error_data == 0 :
            i = db_data_cnt
            base_upload_path = "%s/%s/%s" % (os.getcwd(),"static","uploads")
            if not os.path.exists(base_upload_path) :
                os.makedirs(base_upload_path)
            company_upload_path = "%s/%s" % (base_upload_path,company_sn)
            if not os.path.exists(company_upload_path) :
                os.makedirs(company_upload_path)
            image_file_path = "%s/%s" % (company_upload_path,service_sn)
            if not os.path.exists(image_file_path) :
                os.makedirs(image_file_path)
            for row in parameter_dict.getlist("thumbnail[]") :
                if max_image_cnt > i :
                    sys_image_file_name = str(uuid.uuid4()).replace("-","") + ".jpg"
                    thumbnail = os.path.join(image_file_path,sys_image_file_name)
                    with open(thumbnail,"wb") as f:
                        imagestr = row.split(",")[1]
                        f.write(base64.decodebytes(imagestr.encode("utf8")))
                    f.close()
                    thumbnail = thumbnail.replace(os.getcwd(),"")
                    if vcms_db_agent._add_company_product_image_data(company_sn,service_sn,int(product_sn),thumbnail) > 0 :
                        i += 1
            image_totals = vcms_db_agent._get_company_product_image_cnt(company_sn,product_sn)
            if image_totals > 0 :
                vcms_db_agent._upd_company_product_image_totals(company_sn,product_sn,image_totals)
            self.return_value["data"] = self.get_company_product_image_list(page_settings,product_sn,1)
            self.return_value["message"] = page_settings["success_text"]
            self.return_value["code"] = 1
        return self.return_value

    def set_pkl_file_to_test_server(self,page_settings,service_sn) :
        self.__reset_return_value()
        company_sn = int(session["company_sn"])
        #config_path = os.getcwd() + "/conf/"
        #config = Jsonloader(config_path + "default.conf").getJsonDataMapping()
        #api_setting = config_path + config["project_name"] + "/" +config[config["env"]]["api_setting"]
        api_config = {}#Jsonloader(api_setting).getJsonDataMapping()
        embedding = Embedding(api_config)
        #pkl_key = "1_2_0_e071e0acc4924aedb91b69ad2e1c4248"
        #pkl_key = embedding.create_pkl_file_data(company_sn,service_sn,0)
        #rs = embedding.create_pkl_file(company_sn,pkl_key)
        #rs = embedding.create_pkl_file_data(company_sn,service_sn,0)
        #if rs["code"] == "0001" :
        self.return_value["message"] = page_settings["success_text"]
        self.return_value["code"] = 1
        return self.return_value
 
    def deploy_pkl_file_to_server(self,page_settings,service_sn) :
        self.__reset_return_value()
        company_sn = int(session["company_sn"])
        api_config = {}
        embedding = Embedding(api_config)
        return embedding.deploy_pkl_file(company_sn,service_sn)

    def get_product_by_sku(self,sku,service_sn) :
        self.__reset_return_value()
        company_sn = int(session["company_sn"])
        vcms_db_agent = VcmsDbAgent()
        rs = vcms_db_agent._get_company_product_by_sku(company_sn,sku,int(service_sn))
        if rs == 0 :
            self.return_value["code"] = 1
        return self.return_value

    def get_system_announcement_list(self,page_settings,pages = 1) :
        self.__reset_return_value()
        company_sn = int(session["company_sn"])
        page_settings["company_sn"] = company_sn
        page_settings["current_language"] = session["language"]
        page_settings["system_announcement_tab"] = 13
        page_settings["add_system_announcement_tab"] = 14
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
                              "tab_sn" : 13,
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
            page_settings["system_announcement_tab"] = 13
            page_settings["add_system_announcement_tab"] = 14
            page_settings["pages"] = pages
            page_settings["announcement_list"] = vcms_db_agent._get_all_system_announcement_detail_data(parameter_dict.get("data_sn"))[session["language"]]
            page_settings["publish_time"] = str(vcms_db_agent._get_system_announcement_data_by_board_hash(parameter_dict.get("data_sn"))["publish_time"]).replace(" 00:00:00","")
            html = render_template("tab_ui/vcms_system_announcement_detail.tpl",data = page_settings)
        return html

    def set_company_account_status(self,page_settings,parameter_dict) :
        self.__reset_return_value()
        company_sn = int(session["company_sn"])
        user_sn = parameter_dict.get("data_sn")
        enabled = 1
        if parameter_dict.get("enabled") is not None :
            enabled = parameter_dict.get("enabled")
        vcms_db_agent = VcmsDbAgent()
        rs = vcms_db_agent._upd_company_account_status(company_sn,int(user_sn),int(enabled))
        if rs > 0 :
            branch_sn = vcms_db_agent._get_user_data_by_user_sn(int(user_sn))["company_branch_sn"]
            self.return_value["data"] = self.get_company_branch_account_list(page_settings,int(branch_sn))
            self.return_value["message"] = page_settings["success_text"]
            self.return_value["code"] = 1
        return self.return_value

    def set_company_product_csv(self,page_settings,parameter_dict,product_csv_file) :
        self.__reset_return_value()
        company_sn = int(session["company_sn"])
        service_sn = int(parameter_dict.get("service_sn"))
        user_sn = int(session["admin_id"])
        rs = Csvmanage().product_csv_uploads(product_csv_file,company_sn,service_sn,user_sn)
        if rs :
            self.return_value["message"] = page_settings["success_text"]
            self.return_value["code"] = 1
        return self.return_value

    def set_company_product_image_csv(self,page_settings,parameter_dict,product_image_file) :
        self.__reset_return_value()
        company_sn = int(session["company_sn"])
        service_sn = int(parameter_dict.get("service_sn"))
        user_sn = int(session["admin_id"])
        rs = Csvmanage().product_image_csv_uploads(product_image_file,company_sn,service_sn,user_sn)
        if rs :
            self.return_value["message"] = page_settings["success_text"]
            self.return_value["code"] = 1
        return self.return_value

    def download_company_product_csv(self,page_settings,parameter_dict) :
        self.__reset_return_value()
        company_sn = int(session["company_sn"])
        service_sn = int(parameter_dict.get("service_sn"))
        search = {}
        for k ,v in parameter_dict.items() :
            search[k] = v
        vcms_db_agent = VcmsDbAgent()
        csv_data = vcms_db_agent._get_company_service_product_csv_data(company_sn,service_sn,search)
        str = "sku,barcode,product_name,abbreviation,image_totals,enabled,ct\r\n"
        if len(csv_data) > 0 :
            for key, value in csv_data.items() :
                str += ("%s,%s,%s,%s,%s,%s,%s\r\n") % (value["sku"],value["barcode"],value["product_name"],value["abbreviation"],value["image_totals"],value["enabled"],value["ct"])
        self.return_value["data"] = str
        self.return_value["message"] = page_settings["success_text"]
        self.return_value["code"] = 1
        return self.return_value

    def download_company_product_error_csv_log(self,page_settings,parameter_dict) :
        self.__reset_return_value()
        company_sn = int(session["company_sn"])
        service_sn = int(parameter_dict.get("service_sn"))
        csv_sn = int(parameter_dict.get("csv"))
        csv_manage = Csvmanage()
        error_data = csv_manage.get_product_csv_error_log(company_sn,service_sn,csv_sn)
        if len(error_data) :
            str = "sku,barcode,product_name,message\r\n"
            for key, value in error_data.items() :
                str += ("%s,%s,%s,%s\r\n") % (value["sku"],value["barcode"],value["product_name"],value["message"])
            sucess_data = csv_manage.get_product_csv_sucess_log(company_sn,service_sn,csv_sn)
            for k2,v2 in sucess_data.items() :
                str += ("%s,%s,%s,%s\r\n") % (v2["sku"],v2["barcode"],v2["product_name"],v2["message"])
            self.return_value["data"] = str
            self.return_value["code"] = 1
        return self.return_value

    def __allowed_file(self,filename) :
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in self.ALLOWED_EXTENSIONS

    def __reset_return_value(self) :
        self.return_value["code"] = 0
        self.return_value["message"] = ""
        self.return_value["data"] = {}
