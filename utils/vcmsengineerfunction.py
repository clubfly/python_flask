import os,sys,traceback
import datetime,time
import collections,math,re
from flask import render_template,session
from utils.vcmslogin import VcmsLogin
from utils.vcmsdbagent import VcmsDbAgent

class VcmsEngineerFunction :

    return_value = {"code":0,"message":"","data":{}}

    def __init__(self) :
        pass

    def get_main_ui(self,page_settings) :
        self.__reset_return_value()
        tab_list = [
                   VcmsLogin().get_change_self_pwd(page_settings)
                   ]
        return tab_list

    def __reset_return_value(self) :
        self.return_value["code"] = 0
        self.return_value["message"] = ""
        self.return_value["data"] = {}
