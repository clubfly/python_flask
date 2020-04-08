import os,sys,traceback
import datetime,time,uuid
import collections,math,re,hashlib
from flask import render_template,session
from utils.jsonloader import Jsonloader
from utils.htmlbuilder import HtmlBuilder
from utils.vcmslogin import VcmsLogin
from utils.vcmsdbagent import VcmsDbAgent
from utils.vcmslicensedbagent import VcmsLicenseDbAgent

class VcmsRootFunction :

    return_value = {"code":0,"message":"","data":{}}
    detection_api_suffix = "/vcms_api/DetectionModule"
    feature_api_suffix = "/vcms_api/FeatureModule"
    pkl_update_api_suffix = "/vcms_update_api/CheckoutModule"
    __max_show_data = 100
    lock_token = "ee1aecfff2a34b1ab95198572337820e"

    def __init__(self) :
        pass

    def get_main_ui(self,page_settings) :
        self.__reset_return_value()
        tab_list = [VcmsLogin().get_change_self_pwd(page_settings),
                    self.get_company_list(page_settings),
                    self.get_system_recognition_service_list(page_settings),
                    self.get_edit_company(page_settings,0),
                    self.get_company_profile_list(page_settings,0),
                    self.get_company_service_list(page_settings,0),
                    self.get_company_account_list(page_settings,0),
                    self.get_company_license_list(page_settings,None),
                    self.get_edit_company_service(page_settings,0),
                    self.get_edit_company_account(page_settings,0),
                    self.get_change_account_pwd(page_settings,0),
                    self.get_bind_service_account_list(page_settings,0),
                    self.get_company_license_request_list(page_settings,0),
                    self.get_edit_company_license_request(page_settings,0),
                    self.get_system_announcement_list(page_settings,1),
                    self.get_edit_system_announcement(page_settings,None)]
        return tab_list

    def get_company_list(self,page_settings) :
        self.__reset_return_value()
        page_settings["company_list"] = VcmsDbAgent()._get_all_company_data()
        page_settings["page_back_tab"] = 4
        page_settings["company_profile_tab"] = 5
        page_settings["company_service_tab"] = 6
        page_settings["company_account_tab"] = 7
        page_settings["company_license_request_tab"] = 8
        return render_template("tab_ui/vcms_company.tpl",data = page_settings)

    def get_system_recognition_service_list(self,page_settings) :
        self.__reset_return_value()
        page_settings["service_list"] = VcmsDbAgent()._get_system_service_data()
        return render_template("tab_ui/vcms_recognition_service.tpl",data = page_settings)

    def get_edit_company(self,page_settings,company_sn = 0) :
        self.__reset_return_value()
        page_settings["company_sn"] = company_sn
        return render_template("tab_ui/vcms_edit_company.tpl",data = page_settings)

    def get_company_profile_list(self,page_settings,company_sn = 0) :
        self.__reset_return_value()
        html = ""
        page_settings["company_profile_tab"] = 5
        if company_sn > 0 :
            page_settings["company_sn"] = company_sn
            page_settings["company_profile_list"] = VcmsDbAgent()._get_company_profile_data(int(company_sn))
            html = render_template("tab_ui/vcms_company_profile.tpl",data = page_settings)
        return html

    def get_company_service_list(self,page_settings,company_sn = 0) :
        self.__reset_return_value()
        html = ""
        page_settings["company_service_tab"] = 6
        if company_sn > 0 :
            page_settings["company_sn"] = company_sn
            page_settings["service_list"] = VcmsDbAgent()._get_company_service_data(company_sn)
            html = render_template("tab_ui/vcms_company_service.tpl",data = page_settings)
        return html

    def get_company_account_list(self,page_settings,company_sn = 0) :
        self.__reset_return_value()
        html = ""
        page_settings["add_company_account"] = 10
        page_settings["company_account_tab"] = 7
        page_settings["account_password_tab"] = 11
        page_settings["bind_service_account_tab"] = 12
        if company_sn > 0 :
            page_settings["company_sn"] = company_sn
            page_settings["account_list"] = VcmsDbAgent()._get_company_account_data(company_sn)
            html = render_template("tab_ui/vcms_company_account.tpl",data = page_settings)
        return html

    def get_company_license_list(self,page_settings,parameters=None) :
        self.__reset_return_value()
        html = ""
        page_settings["company_license_request_tab"] = 13
        page_settings["company_license_tab"] = 8
        if parameters is not None :
            parameter_list = self.__split_parameters(parameters)
            page_settings["company_sn"] = int(parameter_list[0])
            page_settings["license_list"] = VcmsLicenseDbAgent()._get_company_license_request_license_data(int(parameter_list[1]))
            html = render_template("tab_ui/vcms_company_license.tpl",data = page_settings)
        return html

    def get_company_license_detail(self,page_settings,sn = 0) :
        self.__reset_return_value()
        html = ""
        page_settings["company_license_tab"] = 8
        if sn > 0 :
            page_settings["license_list"] = VcmsLicenseDbAgent()._get_company_license_detail_data(sn)[sn]
            page_settings["company_sn"] = page_settings["license_list"]["company_sn"]
            html = render_template("tab_ui/vcms_company_license_detail.tpl",data = page_settings)
        return html

    def get_edit_company_service(self,page_settings,company_sn = 0) :
        self.__reset_return_value()
        html = ""
        if company_sn > 0 :
            vcms_db_agent = VcmsDbAgent()
            page_settings["company_sn"] = company_sn
            system_service = vcms_db_agent._get_system_service_data()
            company_service = vcms_db_agent._get_company_service_data(company_sn)
            service = {}
            for k,v in company_service.items() :
                service[int(v["service_sn"])] = int(v["service_sn"])
            return_data = collections.OrderedDict()
            for k,v in system_service.items() :
                if k not in service :
                    return_data[k] = v
            page_settings["per_product_image_cnt_list"] = reversed(range(1,(int(page_settings["per_product_image_cnt_setting"])+1)))
            page_settings["service_list"] = return_data
            page_settings["company_name"] = vcms_db_agent._get_all_company_data()[company_sn]["company_name"]
            html = render_template("tab_ui/vcms_edit_company_service.tpl",data = page_settings)
        return html

    def get_edit_company_account(self,page_settings,company_sn = 0) :
        self.__reset_return_value()
        html = ""
        page_settings["company_account_tab"] = 7
        if company_sn > 0 :
            return_data = collections.OrderedDict()
            vcms_db_agent = VcmsDbAgent()
            user_rank_list = vcms_db_agent._get_all_system_user_ranks()
            for k,v in user_rank_list.items() :
                if int(k) == 3 :
                    return_data[k] = v
            page_settings["company_sn"] = company_sn
            page_settings["company_name"] = vcms_db_agent._get_all_company_data()[company_sn]["company_name"]
            page_settings["user_rank_list"] = return_data
            html = render_template("tab_ui/vcms_edit_company_account.tpl",data = page_settings)
        return html

    def get_change_account_pwd(self,page_settings,user_sn = 0) :
        self.__reset_return_value()
        html = ""
        page_settings["user_sn"] = user_sn
        page_settings["company_account_tab"] = 7
        if user_sn > 0 :
            user_info = VcmsDbAgent()._get_account_data(user_sn)
            page_settings["company_sn"] = user_info["company_sn"]
            page_settings["account"] = user_info["account"]
            html = render_template("tab_ui/vcms_edit_company_account_pwd.tpl",data = page_settings)
        return html

    def get_bind_service_account_list(self,page_settings,user_sn = 0) :
        self.__reset_return_value()
        html = ""
        page_settings["user_sn"] = user_sn
        page_settings["bind_service_tab"] = 12
        if int(user_sn) > 0 :
            vcms_db_agent = VcmsDbAgent()
            user_info = vcms_db_agent._get_account_data(int(user_sn))
            page_settings["company_sn"] = int(user_info["company_sn"])
            company_service_info = vcms_db_agent._get_company_service_data(int(user_info["company_sn"]))
            user_service_info = vcms_db_agent._get_user_service_data(int(user_sn))
            enabled_service = {}
            for k1,v1 in user_service_info.items() :
                 if int(v1["enabled"]) == 1 :
                     enabled_service[int(v1["company_service_sn"])] = v1
            for k1,v1 in company_service_info.items() :
                if k1 in enabled_service :
                    company_service_info[k1]["user_enabled"] = 1
                else :
                    company_service_info[k1]["user_enabled"] = 0 
            page_settings["company_service_list"] = company_service_info
            html = render_template("tab_ui/vcms_bind_service_account.tpl",data = page_settings)
        return html

    def set_company_data(self,page_settings,parameter_dict) :
        self.__reset_return_value()
        company_sn = parameter_dict.get("company_sn")
        company_name = parameter_dict.get("company_name")
        if int(company_sn) == 0 :
            vcms_db_agent = VcmsDbAgent()
            data_check = {
                          "company_name_error" : ""
                         }
            if vcms_db_agent._check_company_data(company_name) == 1 :
                data_check["company_name_error"] = page_settings["duplication_error_text"]
            else :
                max_admin_cnt = int(page_settings["company_max_admin_cnt"])
                max_branch_user_cnt = int(page_settings["company_max_branch_user_cnt"])
                max_branch_cnt = int(page_settings["company_max_branch_cnt"])
                company_sn = vcms_db_agent._add_company_data(company_name,max_admin_cnt,max_branch_user_cnt,max_branch_cnt)
                if company_sn > 0 : # commit success
                    if vcms_db_agent._add_company_profile_data(company_sn,company_name) > 0 :
                        self.return_value["data"] = self.get_company_list(page_settings)
                        self.return_value["message"] = page_settings["success_text"]
                        self.return_value["code"] = 1
                        return self.return_value
                else :
                    data_check["company_name_error"] = page_settings["commit_error_text"]
            self.return_value["data"] = data_check
        return self.return_value

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
        company_sn = parameter_dict.get("company_sn")
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

    def set_company_service(self,page_settings,parameter_dict) :
        self.__reset_return_value()
        data_check = {
                      "service_sn_error" : page_settings["empty_cnt_error"],
                      "per_product_image_cnt_error" : page_settings["empty_cnt_error"],
                      "max_user_cnt_error" : page_settings["empty_cnt_error"],
                      "max_product_cnt_error" : page_settings["empty_cnt_error"],
                      "min_training_cnt_error" : page_settings["empty_cnt_error"],
                      "detection_api_ip_error" : page_settings["empty_error"],
                      "feature_api_ip_error" : page_settings["empty_error"],
                      "pkl_update_api_ip_error" : page_settings["empty_error"]
                     }
        company_sn = parameter_dict.get("company_sn")
        if company_sn is not None and int(company_sn) > 0 :
            vcms_db_agent = VcmsDbAgent()
            error_data = 0
            service_sn = parameter_dict.get("service_sn")
            if service_sn is not None and service_sn != "" :
                system_service = vcms_db_agent._get_system_service_data()
                data_check["service_sn_error"] = ""
                if int(service_sn) not in system_service :
                    error_data += 1
                    data_check["service_sn_error"] = page_settings["service_error_text"]
                    company_service = vcms_db_agent._get_company_service_data(company_sn)
                    if int(service_sn) in company_service :
                        error_data += 1
                        data_check["service_sn_error"] = page_settings["same_as_service_error"]
            else :
                error_data += 1
            per_product_image_cnt = parameter_dict.get("per_product_image_cnt")
            if per_product_image_cnt is not None and per_product_image_cnt != "" :
                data_check["per_product_image_cnt_error"] = ""
                if int(per_product_image_cnt) <= 0 or int(per_product_image_cnt) > int(page_settings["per_product_image_cnt_setting"]) :
                    error_data += 1
                    data_check["per_product_image_cnt_error"] = page_settings["invalid_per_product_image_cnt_error"] + \
                                                                page_settings["per_product_image_cnt_setting"]
            else :
                error_data += 1
            max_product_cnt = parameter_dict.get("max_product_cnt")
            if max_product_cnt is not None and max_product_cnt != "" :
                data_check["max_product_cnt_error"] = ""
                if re.compile("^[+]?\\d+$").match(max_product_cnt) is None :
                    error_data += 1
                    data_check["max_product_cnt_error"] = page_settings["invalid_cnt_error"]
                else :
                    if int(max_product_cnt) <= 0 or int(max_product_cnt) > int(page_settings["max_product_cnt_setting"]) :
                        error_data += 1
                        data_check["max_product_cnt_error"] = page_settings["invalid_product_cnt_error"] + \
                                                              page_settings["max_product_cnt_setting"]
            else :
                error_data += 1
            min_training_cnt = parameter_dict.get("min_training_cnt")
            if min_training_cnt is not None and min_training_cnt != "" :
                data_check["min_training_cnt_error"] = ""
                if re.compile("^[+]?\\d+$").match(min_training_cnt) is None :
                    error_data += 1
                    data_check["min_training_cnt_error"] = page_settings["invalid_cnt_error"]
                else :
                    if int(min_training_cnt) <= 0 or int(min_training_cnt) < int(page_settings["min_training_cnt_setting"]) :
                        error_data += 1
                        data_check["min_training_cnt_error"] = page_settings["invalid_training_cnt_error"] + \
                                                               page_settings["min_training_cnt_setting"]
            else :
                error_data += 1
            detection_api = parameter_dict.get("detection_api")
            if detection_api is not None and detection_api != "" :
                data_check["detection_api_ip_error"] = ""
                if re.compile("^(?:http(s)?:\/\/)?[\w.-]+(?:\.[\w\.-]+)+[\w\-\._~:/?#[\]@!\$&'\(\)\*\+,;=.]+$").match(detection_api) is None :
                    error_data += 1
                    data_check["feature_api_ip_error"] = page_settings["empty_error"]
            else :
                error_data += 1
            feature_api = parameter_dict.get("feature_api")
            if feature_api is not None and feature_api != "" :
                data_check["feature_api_ip_error"] = ""
                if re.compile("^(?:http(s)?:\/\/)?[\w.-]+(?:\.[\w\.-]+)+[\w\-\._~:/?#[\]@!\$&'\(\)\*\+,;=.]+$").match(feature_api) is None :
                    error_data += 1
                    data_check["feature_api_ip_error"] = page_settings["empty_error"] 
            else :
                error_data += 1
            pkl_update_api = parameter_dict.get("pkl_update_api")
            if pkl_update_api is not None and pkl_update_api != "" :
                data_check["pkl_update_api_ip_error"] = ""
                if re.compile("^(?:http(s)?:\/\/)?[\w.-]+(?:\.[\w\.-]+)+[\w\-\._~:/?#[\]@!\$&'\(\)\*\+,;=.]+$").match(pkl_update_api) is None :
                    error_data += 1
                    data_check["pkl_update_api_ip_error"] = page_settings["empty_error"]
            self.return_value["data"] = data_check
            if error_data == 0 :
                detection_real_api = str(detection_api) + self.detection_api_suffix
                feature_real_api = str(feature_api) + self.feature_api_suffix
                pkl_update_real_api = None
                if pkl_update_api is not None and pkl_update_api != "" :
                    pkl_update_real_api = str(pkl_update_api) + self.pkl_update_api_suffix
                if vcms_db_agent._add_company_service_data(company_sn,per_product_image_cnt,service_sn,
                                                           max_product_cnt,min_training_cnt,detection_real_api,feature_real_api,pkl_update_real_api) > 0 :
                    self.return_value["data"] = self.get_company_service_list(page_settings,int(company_sn))
                    self.return_value["message"] = page_settings["success_text"]
                    self.return_value["code"] = 1
        return self.return_value

    def set_company_account(self,page_settings,parameter_dict) :
        self.__reset_return_value()
        data_check = {
                      "account_error" : page_settings["empty_cnt_error"],
                      "new_pwd_error" : page_settings["empty_cnt_error"],
                      "confirm_pwd_error" : page_settings["empty_cnt_error"]
                     }
        company_sn = parameter_dict.get("company_sn")
        if company_sn is not None and int(company_sn) > 0 :
            vcms_db_agent = VcmsDbAgent()
            error_data = 0
            account = parameter_dict.get("account")
            if account is not None and account != "" :
                data_check["account_error"] = ""
                #if re.compile("^[\w]+$").match(account) is None :
                if re.compile("^[a-zA-Z0-9_\.\-]{1,63}@[a-zA-Z0-9\-]{2,63}\\.[a-zA-Z]{2,63}(\\.[a-zA-Z]{2,63})?$").match(account) is None :
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
            user_rank_sn = 3
            max_cnt = int(page_settings["company_max_admin_cnt"])
            current_cnt = vcms_db_agent._get_company_rank_user_cnt(int(company_sn),int(user_rank_sn))
            if current_cnt >= max_cnt :
                error_data += 1
                data_check["account_error"] = page_settings["limitation_error"]
            self.return_value["data"] = data_check
            if error_data == 0 :
                hash = hashlib.md5()
                hash.update(new_password.encode('utf-8'))
                pwd = str(hash.hexdigest())
                if vcms_db_agent._add_company_account_data(company_sn,account,pwd,user_rank_sn,0) > 0 :
                    self.return_value["data"] = self.get_company_account_list(page_settings,int(company_sn))
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
        company_sn = 0
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
                    company_sn = int(user_info["company_sn"])
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
                self.return_value["data"] = self.get_company_account_list(page_settings,company_sn)
                self.return_value["message"] = page_settings["success_text"]
                self.return_value["code"] = 1
        return self.return_value        

    def set_bind_service_account(self,page_settings,parameter_dict) :
        self.__reset_return_value()
        data_check = {
                      "service_sn_1_error" : page_settings["empty_cnt_error"]
                     }
        company_sn = parameter_dict.get("company_sn")
        user_sn = parameter_dict.get("user_sn")
        error_data = 0
        vcms_db_agent = VcmsDbAgent()
        if company_sn is not None and company_sn != "" :
            data_check["service_sn_1_error"] = ""
            if re.compile("^[0-9]*$").match(company_sn) is None :
                error_data += 1
                data_check["service_sn_1_error"] = page_settings["invalid_company_sn_error"]
            else : 
                company_info = vcms_db_agent._get_all_company_data()
                if int(company_sn) not in company_info :
                    error_data += 1
                    data_check["service_sn_1_error"] = page_settings["empty_company_sn_error"]
        else :
            error_data += 1
            data_check["service_sn_1_error"] = page_settings["company_sn_error"]
        if user_sn is not None and user_sn != "" :
            if re.compile("^[\d]*$").match(user_sn) is None :
                error_data += 1
                data_check["service_sn_1_error"] = page_settings["user_sn_format_error"]
            else :
                user_info = vcms_db_agent._get_account_data(user_sn)
                if "admin_id" not in user_info :
                    error_data += 1
                    data_check["service_sn_1_error"] = page_settings["none_user_sn_error"]
                else :
                    company_sn = int(user_info["company_sn"])
        else :
            error_data += 1
        self.return_value["data"] = data_check
        if error_data == 0 :
            if "company_service_sn" in parameter_dict :
                company_service_info = vcms_db_agent._get_company_service_data(int(company_sn))
                user_permission = vcms_db_agent._get_user_service_data(int(user_sn))
                user_permission_list = {}
                for k,v in user_permission.items() :
                    user_permission_list[int(v["company_service_sn"])] = v
                vcms_db_agent._upd_all_user_service_permission_data(int(user_sn),0)
                for row in parameter_dict.getlist("company_service_sn") :
                    if int(row) in user_permission_list :
                        vcms_db_agent._upd_user_service_permission_data(int(user_sn),int(row),1)
                    else :
                        service_sn = company_service_info[int(row)]["service_sn"]
                        vcms_db_agent._add_user_service_permission_data(int(company_sn),int(user_sn),int(row),int(service_sn))
            else :
                vcms_db_agent._upd_all_user_service_permission_data(int(user_sn),0)
            self.return_value["data"] = self.get_bind_service_account_list(page_settings,int(user_sn))
            self.return_value["message"] = page_settings["success_text"]
            self.return_value["code"] = 1        
        return self.return_value

    def get_company_license_request_list(self,page_settings,company_sn = 0) :
        self.__reset_return_value()
        html = ""
        page_settings["company_license_tab"] = 8
        page_settings["company_license_request_tab"] = 13
        page_settings["add_company_license_request"] = 14
        if company_sn > 0 :
            page_settings["company_sn"] = company_sn
            page_settings["license_request_list"] = VcmsLicenseDbAgent()._get_company_license_request_data(company_sn)
            html = render_template("tab_ui/vcms_company_license_request.tpl",data = page_settings)
        return html

    def get_company_license_request_detail(self,page_settings,sn = 0) :
        self.__reset_return_value()
        html = ""
        page_settings["company_license_request_tab"] = 13
        if sn > 0 :
            #print(VcmsLicenseDbAgent()._get_company_license_request_detail_data(sn))
            page_settings["license_request_list"] = VcmsLicenseDbAgent()._get_company_license_request_detail_data(sn)[sn]
            page_settings["company_sn"] = page_settings["license_request_list"]["company_sn"]
            html = render_template("tab_ui/vcms_company_license_request_detail.tpl",data = page_settings)
        return html

    def get_edit_company_license_request(self,page_settings,company_sn = 0) :
        self.__reset_return_value()
        html = ""
        page_settings["company_license_request_tab"] = 13
        page_settings["add_company_license_request"] = 14
        if company_sn > 0 :
            vcms_db_agent = VcmsDbAgent()
            vcms_license_db_agent = VcmsLicenseDbAgent()
            page_settings["company_sn"] = company_sn
            system_service = vcms_db_agent._get_system_service_data()
            company_service = vcms_db_agent._get_company_service_data(company_sn)
            license_encrypt_types = vcms_license_db_agent._get_all_license_encrypt_type_data()
            license_trial_types = vcms_license_db_agent._get_all_license_trial_type_data()
            license_id_types = vcms_license_db_agent._get_all_license_id_type_data()
            # company bind service list
            service = {}
            for k,v in company_service.items() :
                service[int(v["service_sn"])] = int(v["service_sn"])
            return_data = collections.OrderedDict()
            for k,v in system_service.items() :
                if k in service :
                    return_data[k] = v
            page_settings["service_list"] = return_data
            # all license encrypt types
            license_encrypt_list = {}
            for k,v in license_encrypt_types.items() :
                license_encrypt_list[str(v["sn"])] = v
            page_settings["license_encrypt_list"] = license_encrypt_list
            # all license trial types
            license_trial_list = {}
            for k,v in license_trial_types.items() :
                license_trial_list[str(v["sn"])] = v
            page_settings["license_trial_list"] = license_trial_list
            # all license id types
            license_id_type_list = {}
            for k,v in license_id_types.items() :
                license_id_type_list[str(v["sn"])] = v
            page_settings["license_id_type_list"] = license_id_type_list
            # set default start date , expire date
            _today = datetime.datetime.today().strftime("%Y-%m-%d")
            page_settings["version"] = "1.0.0"
            page_settings["start_date"] = _today
            page_settings["expire_date"] = _today
            page_settings["batch_license_count"] = 0
            page_settings["company_name"] = vcms_db_agent._get_all_company_data()[company_sn]["company_name"]
            html = render_template("tab_ui/vcms_edit_company_license_request.tpl", data = page_settings)
        return html

    def set_company_license_request_data(self,page_settings,parameter_dict) :
        self.__reset_return_value()
        data_check = {
                        "company_name_error" : ""
        }
        vcms_db_agent = VcmsDbAgent()
        vcms_license_db_agent = VcmsLicenseDbAgent()
        data_parameter = {}
        data_parameter["company_sn"] = int(parameter_dict.get("company_sn"))
        data_parameter["company_name"] = vcms_db_agent._get_company_profile_data(data_parameter["company_sn"])["company_name"]
        data_parameter["encrypt_sn"] = int(parameter_dict.get("encrypt_sn"))
        data_parameter["encrypt_type"] = vcms_license_db_agent._get_all_license_encrypt_type_data()[data_parameter["encrypt_sn"]]["encrypt_type"]
        data_parameter["service_sn"] = int(parameter_dict.get("service_sn"))
        data_parameter["service_name"] = vcms_db_agent._get_system_service_data()[data_parameter["service_sn"]]["service_name"]
        data_parameter["service_type"] = vcms_db_agent._get_system_service_data()[data_parameter["service_sn"]]["service_type"]
        data_parameter["license_feature"] = data_parameter["service_sn"]
        data_parameter["version"] = parameter_dict.get("version")
        data_parameter["trial_sn"] = int(parameter_dict.get("trial_sn"))
        data_parameter["trial_type"] = vcms_license_db_agent._get_all_license_trial_type_data()[data_parameter["trial_sn"]]["trial_type"]
        data_parameter["trial_days"] = int(vcms_license_db_agent._get_all_license_trial_type_data()[data_parameter["trial_sn"]]["trial_days"])
        data_parameter["id_sn"] = int(parameter_dict.get("id_sn"))
        data_parameter["id_type"] = vcms_license_db_agent._get_all_license_id_type_data()[data_parameter["id_sn"]]["id_type"]
        data_parameter["hostid"] = parameter_dict.get("hostid")
        data_parameter["start_date"] = parameter_dict.get("start_date")[0:10]
        data_parameter["expire_date"] = parameter_dict.get("expire_date")[0:10]
        data_parameter["connect_count"] = parameter_dict.get("connect_count")
        data_parameter["server"] = parameter_dict.get("server")
        data_parameter["port"] = parameter_dict.get("port")
        data_parameter["license_count"] = int(parameter_dict.get("license_count"))
        data_parameter["batch_license_count"] = int(parameter_dict.get("batch_license_count"))
        # trial process
        if (data_parameter["trial_sn"] != 1):
            data_parameter["hostid"] = data_parameter["trial_type"]
            data_parameter["expire_date"] = str(datetime.datetime.strptime(data_parameter["start_date"], '%Y-%m-%d') + datetime.timedelta(data_parameter["trial_days"] - 1))[0:10]
        # id_type = 1 and hostid process
        if (data_parameter["id_sn"] == 1 and data_parameter["hostid"] == ''):
            data_parameter["hostid"] = uuid.uuid5(uuid.NAMESPACE_DNS, str(datetime.datetime.now()))

        request_sn = vcms_license_db_agent._add_company_license_request_data(data_parameter)
        if request_sn > 0 : # commit success
            self.return_value["data"] = self.get_company_license_request_list(page_settings, int(parameter_dict.get("company_sn")))
            self.return_value["message"] = page_settings["success_text"]
            self.return_value["code"] = 1
            return self.return_value
        else :
            data_check["company_name_error"] = page_settings["commit_error_text"]
        self.return_value["data"] = data_check
        return self.return_value

    def __split_parameters(self, parameters):
        parameter_list = parameters.split(",")
        return parameter_list

    def get_system_announcement_list(self,page_settings,pages = 1) :
        self.__reset_return_value()
        html = ""
        company_sn = int(session["company_sn"])
        page_settings["company_sn"] = company_sn
        page_settings["current_language"] = session["language"]
        page_settings["system_announcement_tab"] = 15
        page_settings["add_system_announcement_tab"] = 16
        page_settings["pages"] = pages
        if company_sn == 0 :
            max_page_show_data = self.__max_show_data
            max_pages = 1 
            vcms_db_agent = VcmsDbAgent()
            db_data_cnt = vcms_db_agent._get_all_system_announcement_cnt()
            if db_data_cnt > 0 :
                max_pages = math.ceil(db_data_cnt/max_page_show_data)
            if int(pages) == 0 :
                pages = 1
            if int(pages) >= max_pages :
                pages = max_pages
            offset = (int(pages) - 1) * max_page_show_data
            page_settings["announcement_list"] = vcms_db_agent._get_all_system_announcement_data(max_page_show_data,offset)
            base_url = page_settings["system_announcement_url"]
            pagination_setting = {
                                  "base_url" : page_settings["system_announcement_url"],
                                  "tab_sn" : 15,
                                  "data_sn" : "0",
                                  "bind_class" : "add_system_announcement",
                                  "direct_page" : pages,
                                  "max_page" : max_pages,
                                  "go_text" : page_settings["go_text"]
                                 }
            page_settings["pagination"] = HtmlBuilder().pagination(base_url,pagination_setting)
            html = render_template("tab_ui/vcms_system_announcement.tpl",data = page_settings)
        return html

    def get_edit_system_announcement(self,page_settings,parameter_dict) :
        self.__reset_return_value()
        html = ""
        pages = 1
        company_sn = int(session["company_sn"])
        page_settings["company_sn"] = company_sn
        page_settings["current_language"] = session["language"]
        page_settings["system_announcement_tab"] = 15
        page_settings["add_system_announcement_tab"] = 16
        page_settings["pages"] = pages
        return_data = collections.OrderedDict()
        if parameter_dict is not None :
            pages = parameter_dict.get("pages")
            data_sn = parameter_dict.get("data_sn")
            if str(data_sn) != "0" :
                vcms_db_agent = VcmsDbAgent()
                return_data = vcms_db_agent._get_all_system_announcement_detail_data(data_sn)
                page_settings["publish_time"] = str(vcms_db_agent._get_system_announcement_data_by_board_hash(data_sn)["publish_time"]).replace(" 00:00:00","") 
            if not return_data :
                for k,v in page_settings["language_support"].items() :
                    return_data[k] = {"titles" : "", "contents" : ""}
            page_settings["announcement_list"] = return_data
            page_settings["board_hash"] = data_sn
            page_settings["pages"] = pages
            html = render_template("tab_ui/vcms_edit_system_announcement.tpl",data = page_settings)
        return html

    def get_system_announcement_by_board_hash(self,page_settings,parameter_dict) :
        self.__reset_return_value()
        pages = 1
        if parameter_dict.get("pages") is not None :
            pages = parameter_dict.get("pages")
        vcms_db_agent = VcmsDbAgent()
        page_settings["system_announcement_tab"] = 15
        page_settings["add_system_announcement_tab"] = 16
        page_settings["pages"] = pages
        page_settings["announcement_list"] = vcms_db_agent._get_all_system_announcement_detail_data(parameter_dict.get("data_sn"))[session["language"]]
        page_settings["publish_time"] = str(vcms_db_agent._get_system_announcement_data_by_board_hash(parameter_dict.get("data_sn"))["publish_time"]).replace(" 00:00:00","")
        return render_template("tab_ui/vcms_system_announcement_detail.tpl",data = page_settings)

    def set_system_announcement(self,page_settings,parameter_dict) :
        self.__reset_return_value()
        vcms_db_agent = VcmsDbAgent()
        board_hash = parameter_dict.get("board_hash")
        publish_time = parameter_dict.get("publish_time")
        if publish_time is not None and publish_time != "" :
            publish_time = str(parameter_dict.get("publish_time")) + " 00:00:00"
        else :
            publish_time = None
        new_data = 0
        if str(board_hash) == "0" : 
            board_hash = str(uuid.uuid4()).replace("-","")
            new_data = 1
            announcement_sn = vcms_db_agent._add_system_announcement_data(board_hash,publish_time)
        else :
            announcement_sn = vcms_db_agent._upd_system_announcement_data(board_hash,publish_time)
        if announcement_sn > 0 :
            data_check = 0
            for row in parameter_dict.getlist("languages") :
                language_type = row
                titles = parameter_dict.get("title[" + row + "]")
                contents = parameter_dict.get("contents[" + row + "]")
                if new_data == 1 :
                    rs = vcms_db_agent._add_system_announcement_detail_data(board_hash,language_type,titles,contents)
                else :
                    rs = vcms_db_agent._upd_system_announcement_detail_data(board_hash,language_type,titles,contents)
                if int(rs) > 0 :
                    data_check += 1
            if data_check > 0 :
                self.return_value["data"] = self.get_system_announcement_list(page_settings,1)
                self.return_value["message"] = page_settings["success_text"]
                self.return_value["code"] = 1
        return self.return_value

    def set_system_announcement_status(self,page_settings,parameter_dict):
        self.__reset_return_value()
        vcms_db_agent = VcmsDbAgent()
        pages = 1
        board_hash = parameter_dict.get("data_sn")
        publish_mark = parameter_dict.get("enabled")
        publish_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if int(publish_mark) == 0 :
            publish_time = None
        page = parameter_dict.get("page_sn")
        if page is not None and int(page) > 0 :
            pages = int(page)
        rs = vcms_db_agent._set_system_announcement_status(board_hash,publish_mark,publish_time)
        if rs > 0 :
            self.return_value["data"] = self.get_system_announcement_list(page_settings,pages)
            self.return_value["message"] = page_settings["success_text"]
            self.return_value["code"] = 1
        return self.return_value

    def set_uploading_images_lock_status(self,page_settings,lock_token,parameter_dict) :
        self.__reset_return_value()
        vcms_db_agent = VcmsDbAgent()
        lock_mark = parameter_dict.get("lock_mark")
        rs = vcms_db_agent._set_system_lock_for_uploading_images(lock_token,lock_mark)
        if rs > 0 :
            self.return_value["data"] = vcms_db_agent._get_system_lock_for_uploading_images(lock_token)
            self.return_value["code"] = 1
        return self.return_value

    def __reset_return_value(self) :
        self.return_value["code"] = 0
        self.return_value["message"] = ""
        self.return_value["data"] = {}
