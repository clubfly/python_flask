#-*- coding:utf-8 -*-
import sys
import os
os_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(os_path + '/lib/')
sys.path.append(os_path + '/controllers/')
sys.path.append(os_path + '/utils/')
sys.path.append(os_path + '/core/')
sys.path.append(os_path + '/conf/')
from types import MethodType
from utils.jsonloader import Jsonloader
from utils.returncode import Returncode
import json
import traceback
import collections
from core.projectcore import ProjectCore
from flask import Flask,request,session,escape,redirect
from datetime import timedelta
from utils.settingcheck import SettingCheck
from gevent import monkey
monkey.patch_all()
from gevent import pywsgi

SettingCheck().run()
config_path = os_path + "/conf/"
try :
    config = Jsonloader(config_path + "default.conf").getJsonDataMapping()
    config_setting = config[config["env"]]
    web_url_config = Jsonloader(config_path + config["project_name"] + "/web_url.conf").getJsonDataMapping()
    Factory = ProjectCore()
    app = Flask(__name__)
    #app.secret_key = os.urandom(24)
    app.secret_key = "05299cc3da53891ffc0d491cf8d8a7a68929aaf855b3081e"
    app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=1)
    #app.config.update(language_config)
    controllerList = "%s%s/%s" % (config_path,config["project_name"],config[config["env"]]["method_setting"])
    method_list = Jsonloader(controllerList).getJsonDataMapping()
    for element in method_list :
        if int(method_list[element]["allow_tag"]) == 0 :
            continue
        try :
            Factory.logger.info("Method : " + method_list[element]["ReturnMethod"] + " Is Setting....")
            setattr(Factory,
                    method_list[element]["ReturnMethod"],
                    MethodType(getattr(__import__(method_list[element]["ReturnMethod"]),
                                       method_list[element]["ReturnMethod"]),
                                       Factory))
        except :
            Factory.logger.debug("data error")
            Factory.logger.error(traceback.format_exc())

    @app.route("/<string:functions>/<string:actions>",
               methods=['GET', 'POST'])
    def callback(functions, actions) :
        language_config = Jsonloader(config_path + config["project_name"] + "/language.conf").getJsonDataMapping()
        language_support = []
        language_file = collections.OrderedDict()
        language_name = collections.OrderedDict()
        sop_map = {}
        for k,v in language_config.items() :
            if int(v["accept"]) == 0 :
                continue
            for row in v["alias"] :
                language_support.append(row)
                language_file[row] = v["file"]
                language_name[row] = v["name"]
                sop_map[row] = k
        if "language" not in session :
            session["language"] = sop_map[request.accept_languages.best_match(language_support)]
        if functions not in method_list :
            Factory.logger.debug("function error")
            return json.JSONEncoder().encode(Returncode().getReturnErrorCode("404"))
        if int(method_list[functions]["login_check"]) == 1:
            if 'admin_id' not in session :
                return redirect(web_url_config["login_url"]) 
        try :
            parameter_dict = {}
            if request.method == "POST" :
                parameter_dict = request.form
            else :
                parameter_dict = request.args
            html_template = method_list[functions]["html_template_name"]+".tpl"
            page_settings = {}
            #page_settings = app.config[method_list[functions]["ReturnMethod"]]
            languages = Jsonloader(config_path + config["project_name"] + "/" + language_file[session["language"]]).getJsonDataMapping()
            page_settings = languages[method_list[functions]["ReturnMethod"]]
            if method_list[functions]["type"] == "web" :
                web_style = collections.OrderedDict()
                web_style["css"] = collections.OrderedDict()
                web_style["js"] = collections.OrderedDict()
                css_cnt = len(method_list[functions]["css"])
                if css_cnt > 0 :
                    for i in range(0,css_cnt) :
                        web_style["css"].update({str(i) : method_list[functions]["css"][str(i)]})
                js_cnt = len(method_list[functions]["js"])
                if js_cnt > 0 :
                    for i in range(0,js_cnt) :
                        web_style["js"].update({str(i) : method_list[functions]["js"][str(i)]})
                page_settings["css"] = web_style["css"]
                page_settings["js"] = web_style["js"]
            page_settings["project_name"] = config["project_name"]
            page_settings["publish_pkl"] = config[config["env"]]["publish_pkl"]
            page_settings["company_max_admin_cnt"] = config[config["env"]]["company_max_admin_cnt"]
            page_settings["company_max_branch_user_cnt"] = config[config["env"]]["company_max_branch_user_cnt"]
            page_settings["company_max_branch_cnt"] = config[config["env"]]["company_max_branch_cnt"]
            page_settings["per_product_image_cnt_setting"] = config[config["env"]]["per_product_image_cnt"]
            page_settings["max_branch_user_setting"] = config[config["env"]]["max_branch_user_cnt"]
            page_settings["max_product_cnt_setting"] = config[config["env"]]["max_product_cnt"]
            page_settings["min_training_cnt_setting"] = config[config["env"]]["min_training_cnt"]
            page_settings.update(web_url_config)
            page_settings["language_support"] = language_config
            page_settings["language_name"] = language_name[session["language"]]
            page_settings["language_elements"] = language_support
            page_settings["sop_map"] = sop_map[session["language"]]
            return getattr(Factory,functions)(functions,actions,html_template,page_settings,parameter_dict)
        except :
            Factory.logger.error(traceback.format_exc())
            return redirect(web_url_config["error_url"])

    @app.route("/")
    def redirect_to_menu() :
        redirect_url = web_url_config["main_url"]
        if int(config_setting["login_check"]) :
            if 'user_id' not in session :
                redirect_url = web_url_config["login_url"]
        return redirect(redirect_url)

    @app.errorhandler(404)
    def page_not_found(e):
        return redirect(web_url_config["error_url"])

    if __name__ == "__main__" :
        server = pywsgi.WSGIServer((config[config["env"]]["domain"], int(config[config["env"]]["port"])), app)
        server.serve_forever()
        #app.run(host=config[config["env"]]["domain"],
        #        port=config[config["env"]]["port"],
        #        debug=config[config["env"]]["debug_mode"],
        #        use_reloader=False)
except :
    Factory.logger.error(traceback.format_exc())
    Factory.logger.debug("Data Setting Error")
