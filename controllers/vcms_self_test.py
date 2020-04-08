from flask import jsonify,render_template,session,escape,redirect,request
from utils.htmlbuilder import HtmlBuilder
from utils.jsonloader import Jsonloader
from utils.vcmsadminfunction import VcmsAdminFunction
from utils.vcmsfeaturedbagent import VcmsFeatureDbAgent
from system_service_models.embedding import Embedding
import requests,json,base64,sys,os

def vcms_self_test(self,functions,actions,html_template,page_settings,parameter_dict) :
    return_data = {}
    service_sn = int(actions)
    vcms_db_agent = VcmsFeatureDbAgent()
    api_settings = vcms_db_agent._get_company_all_api_settings()
    #os_path = os.getcwd()
    #config_path = os_path + "/conf/"
    #config = Jsonloader(config_path + "default.conf").getJsonDataMapping()
    #api_setting = config_path + config["project_name"] + "/" +config[config["env"]]["api_setting"]
    #api_config = Jsonloader(api_setting).getJsonDataMapping()
    if session["user_rank_sn"] == 3 :
        test = Embedding({})
        #recognition_api = api_config["validate_url"]
        #recognition_api = api_settings[int(session["company_sn"])][service_sn]["self_test_api"]
        if request.files.get('thumbnail') is None :
            #recognition_data = {"image" : request.form['image']}
            base64_image = request.form['image'].split(",")[1]
        else :
            #base64_image_prefix = "data:image/jpeg;base64,"
            f = request.files['thumbnail']
            b64 = base64.encodebytes(f.stream.read())
            #recognition_data = {"image" :  base64_image_prefix + b64.decode("utf8") }
            base64_image = b64.decode("utf8")
        #return_data = json.loads((requests.post(recognition_api, data=recognition_data).content).decode("utf-8"))
        return_data = test._set_image_detection_for_search(int(session["company_sn"]),int(service_sn),base64_image)
    return jsonify(return_data)
