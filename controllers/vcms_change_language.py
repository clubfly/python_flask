from flask import jsonify,render_template,session,escape,redirect,request
from utils.htmlbuilder import HtmlBuilder
import requests,json

def vcms_change_language(self,functions,actions,html_template,page_settings,parameter_dict) :
    return_data = {"code":0,"message":"","data":{}}
    if actions in page_settings["language_elements"] :
        session["language"] = actions
        return_data["code"] = 1
    return jsonify(return_data)
