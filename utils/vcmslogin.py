import os,sys,traceback
import datetime,time
import collections,math,hashlib
from flask import render_template,session
from utils.vcmsdbagent import VcmsDbAgent

class VcmsLogin : 

    service = "app"
    return_value = {"code":0,"message":"","data":{}}

    def __init__(self) :
        pass

    def login_by_account(self,account,password) :
        self.__reset_return_value()
        hash = hashlib.md5()
        hash.update(password.encode('utf-8'))
        pwd = str(hash.hexdigest())
        vcms_db_agent = VcmsDbAgent()
        return_data = vcms_db_agent._get_login_user_data(account,pwd)
        if "admin_id" in return_data :
            if int(return_data["enabled"]) == 1 :
                if int(return_data["lock_mark"]) == 0 :
                    self.return_value["code"] = 1
                    self.return_value["data"] = return_data
            vcms_db_agent._set_user_last_login_time(int(return_data["admin_id"]))
        return self.return_value

    def get_change_self_pwd(self,page_settings) :
        if "admin_id" in session :
            page_settings["admin_id"] = session["admin_id"]
            page_settings["account"] = session["account"]
        return render_template("tab_ui/vcms_change_self_pwd.tpl",data = page_settings)

    def change_self_pwd(self,page_settings,parameter_dict) :
        self.__reset_return_value()
        data_check = {
                      "current_password_error" : "",
                      "new_password_error" : "",
                      "confirm_password_error" : ""
                     }
        password = parameter_dict.get("old_password")
        new_password = parameter_dict.get("new_password")
        confirm_password = parameter_dict.get("confirm_password")
        hash = hashlib.md5()
        hash.update(password.encode('utf-8'))
        pwd = str(hash.hexdigest())
        vcms_db_agent = VcmsDbAgent()
        return_data = vcms_db_agent._get_user_pwd_data(pwd)
        error_check = 0
        if "admin_id" not in return_data :
            data_check["current_password_error"] = page_settings["current_pwd_error"] 
            error_check = 1
        if new_password is not None and password == new_password :
            data_check["new_password_error"] = page_settings["same_as_current_pwd_error"]
            error_check = 1
        if confirm_password is not None and confirm_password != new_password :
            data_check["confirm_password_error"] = page_settings["confirm_pwd_error"]
            error_check = 1
        self.return_value["data"] = data_check
        if error_check == 0 :
            hash2 = hashlib.md5()
            hash2.update(new_password.encode('utf-8'))
            pwd = str(hash2.hexdigest())
            if vcms_db_agent._upd_self_pwd(pwd) == 1 :
                self.return_value["data"] = self.get_change_self_pwd(page_settings)
                self.return_value["message"] = page_settings["success_text"]
                self.return_value["code"] = 1
        return self.return_value

    def __reset_return_value(self) :
        self.return_value["code"] = 0
        self.return_value["message"] = ""
        self.return_value["data"] = {}
