import os,sys,base64,json,requests,datetime,collections,uuid,pickle,numpy,shutil
from easydict import EasyDict as edict
from dateutil.relativedelta import relativedelta
from system_service_models.servicetemplate import ServiceTemplate
from utils.jsonloader import Jsonloader
from utils.vcmsfeaturedbagent import VcmsFeatureDbAgent

class Embedding(ServiceTemplate) :

    detection_url = ""
    feature_url = ""
    update_pkl_url = ""
    base64_image_prefix = "data:image/jpeg;base64,"
    production_domain = "https://vcms.viscovery.com"
    company_name = ""

    def __init__(self,api_config) :
        pass

    def request_post(self,api_url,data,json_post = 0) :
        return_content = None
        if json_post == 1 :
            return requests.post(api_url, json.dumps(data), headers={'content-type': 'application/json'}, verify=False)
        else :
            return requests.post(api_url, data=data, verify=False)

    def create_company_pkl_file_for_deployment(self) :
        vcms_db_agent = VcmsFeatureDbAgent()
        rs = vcms_db_agent._get_all_company_data()
        for k1,v1 in rs.items() :
            self.company_name = ""
            rs2 = vcms_db_agent._get_company_service_data(k1)
            for k2,v2 in rs2.items() :
                self.company_name = v2["company_name"]
                print (self.company_name + " is exporting ..... service_sn : " + str(k2))
                rs3 = self.create_pkl_file_data(int(k1),int(k2),0)
                print (rs3)

    def create_single_company_pkl_file_for_deployment(self,company_sn) :
        vcms_db_agent = VcmsFeatureDbAgent()
        rs = vcms_db_agent._get_all_company_data()
        for k1,v1 in rs.items() :
            if int(company_sn) != int(k1) :
                continue
            self.company_name = ""
            rs2 = vcms_db_agent._get_company_service_data(k1)
            for k2,v2 in rs2.items() :
                self.company_name = v2["company_name"]
                print (self.company_name + " is exporting ..... service_sn : " + str(k2))
                rs3 = self.create_pkl_file_data(int(k1),int(k2),0)
                print (rs3)

    def create_pkl_file(self,company_sn,pkl_key,pkl_content,service_sn) :
        #vcms_db_agent = VcmsFeatureDbAgent()
        #pkl_data = vcms_db_agent._get_output_pkl_file_data(pkl_key)
        #output_path = os.getcwd() + "/uploads"
        #if not os.path.exists(output_path) :
        #    os.makedirs(output_path)
        #file_path = output_path + "/pkl"
        #if not os.path.exists(file_path) :
        #    os.makedirs(file_path)
        #file_path = output_path + "/pkl/" + str(company_sn)
        #if not os.path.exists(file_path) :
        #    os.makedirs(file_path)
        deploy_path = os.getcwd() + "/static/uploads"
        if not os.path.exists(deploy_path) :
            os.makedirs(deploy_path)
        deploy_output_path = deploy_path + "/" + self.company_name
        if not os.path.exists(deploy_output_path) :
            os.makedirs(deploy_output_path)
        #service_sn = 0
        #for k,v in pkl_data.items() :
            #output = self.__set_output_pkl_file_content(k,v)
        #new_pkl_path = "%s/%s%s" % (file_path,pkl_key,".pkl")
        new_pkl_path = "%s/%s%s" % (deploy_output_path,pkl_key,".pkl")
        fp_new_pkl = open(new_pkl_path, 'wb')
        pickle.dump(pkl_content, fp_new_pkl)
        fp_new_pkl.close()
            #vcms_db_agent._set_output_mark_for_pkl_file(v["pkl_key"])
            #service_sn = v["service_sn"]
        #pkl = str(company_sn)  + "/" + pkl_key + ".pkl"
        #data = {
        #        "db_path" : pkl,
        #       }
        #vcms_db_agent.set_pkl_upd_send_mark_to_test_server(pkl_key)
        #api_settings = vcms_db_agent._get_company_all_api_settings()
        #api = api_settings[int(company_sn)][int(service_sn)]["pkl_update_api"]
        #content = json.loads((self.request_post(api,data,0).content).decode("utf-8"))
        #vcms_db_agent.set_pkl_upd_finish_mark_to_test_server(pkl_key)
        #return content
        yesterday = datetime.datetime.now() + relativedelta(days=-1)
        copy_output_path = deploy_output_path + "/" + yesterday.strftime('%Y%m%d')
        if not os.path.exists(copy_output_path) :
            os.makedirs(copy_output_path)
        copy_pkl_path = "%s/%s_%s%s" % (copy_output_path,service_sn,self.company_name,".pkl")
        shutil.copy(new_pkl_path,copy_pkl_path)
        print ("copy files from " + new_pkl_path + " to " + copy_pkl_path)
        output_path = os.getcwd() + "/uploads"
        if not os.path.exists(output_path) :
            os.makedirs(output_path)
        file_path = output_path + "/pkl"
        if not os.path.exists(file_path) :
            os.makedirs(file_path)
        file_path = output_path + "/pkl/" + str(company_sn)
        if not os.path.exists(file_path) :
            os.makedirs(file_path)
        copy_pkl_path2 = file_path
        shutil.copy(copy_pkl_path,copy_pkl_path2)
        print ("copy files from " + new_pkl_path + " to " + copy_pkl_path2)
        pkl_url = self.production_domain + "/static/uploads/" + \
                  self.company_name + "/" + yesterday.strftime('%Y%m%d') + "/" + \
                  str(service_sn) + "_" + self.company_name + ".pkl"
        return {"pkl_url" : pkl_url}

    def deploy_pkl_file(self,company_sn,service_sn) :
        vcms_db_agent = VcmsFeatureDbAgent()
        rs = vcms_db_agent._get_all_company_data()
        for k1,v1 in rs.items() :
            if int(company_sn) != int(k1) :
                continue
            self.company_name = ""
            rs2 = vcms_db_agent._get_company_service_data(k1)
            for k2,v2 in rs2.items() :
                if int(service_sn) != int(k2) :
                    continue
                self.company_name = v2["company_name"]
                print (self.company_name + " is exporting ..... service_sn : " + str(k2))
                rs3 = self.create_pkl_file_data(int(k1),int(k2),0)
                if rs3["pkl_url"] != "" :
                    api_settings = vcms_db_agent._get_company_all_api_settings()
                    api = api_settings[int(company_sn)][int(service_sn)]["pkl_update_api"]
                    pkl = str(company_sn)  + "/" + str(service_sn) + "_" + self.company_name + ".pkl"
                    print (api + " : " + pkl)
                    data = {"db_path" : pkl}
                    return json.loads((self.request_post(api,data,0).content).decode("utf-8"))

    def __set_output_pkl_file_content(self,k,v) :
        pkl_content = edict({})
        pkl_content["meta"] = {}
        pkl_content["meta"]["image_sn"] = []
        pkl_content["meta"]["sku"] = []
        pkl_content["meta"]["instance_sn"] = []
        pkl_content["meta"]["label_name"] = []
        pkl_content["meta"]["barcode"] = []
        pkl_content["embeddings"] = []
        pkl_content["pkl_key"] = v["pkl_key"]
        pkl_content["company_sn"] = v["company_sn"]
        pkl_content["service_sn"] = v["service_sn"]
        pkl_content["branch_sn"] = v["branch_sn"]
        #vcms_db_agent = VcmsFeatureDbAgent()
        #pkl_feature_data = vcms_db_agent._get_pkl_file_content_data(k)
        for key,val in pkl_feature_data.items() :
            pkl_content["meta"]["image_sn"].append(val["image_sn"])
            pkl_content["meta"]["sku"].append(val["sku"])
            pkl_content["meta"]["instance_sn"].append(val["sn"])
            pkl_content["meta"]["label_name"].append(val["product_name"])
            pkl_content["meta"]["barcode"].append(val["barcode"])
            pkl_content["embeddings"].append(val["feature"])
        for each_key in pkl_content['meta']:
            pkl_content["meta"][each_key] = numpy.asarray(pkl_content["meta"][each_key])[:,numpy.newaxis]
        pkl_content["embeddings"] = numpy.asarray(pkl_content["embeddings"],dtype=numpy.float32)
        return pkl_content

    def create_pkl_file_data(self,company_sn = 0,service_sn = 0,branch_sn = 0) :
        pkl_key = "%s_%s_%s_%s" % (company_sn,service_sn,branch_sn,str(uuid.uuid4()).replace("-",""))
        if int(branch_sn) > 0 :
            rs = self.__get_branch_product_features(pkl_key,company_sn,service_sn,branch_sn)
        else :
            rs = self.__get_all_product_features(pkl_key,company_sn,service_sn,0)
        return rs #pkl_key

    def __get_all_product_features(self, pkl_key, company_sn = 0,service_sn = 0, branch_sn = 0) :
        vcms_db_agent = VcmsFeatureDbAgent()
        vcms_db_agent._del_company_service_pkl_data(company_sn,service_sn,branch_sn)
        feature_pkl_sn = vcms_db_agent._add_company_service_pkl_data(company_sn,service_sn,branch_sn,pkl_key)
        #vcms_db_agent._reset_feature_enabled_by_product_status(company_sn,service_sn)
        product_enabled_data = vcms_db_agent._get_company_service_product_enabled_status_data(company_sn,service_sn,1)
        print ("data start : " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        feature_data = vcms_db_agent._get_company_service_product_features(company_sn,service_sn)
        print ("data end : " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        #print ("file data start : " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        pkl_content = edict({})
        pkl_content["meta"] = {}
        pkl_content["meta"]["image_sn"] = []
        pkl_content["meta"]["sku"] = []
        pkl_content["meta"]["instance_sn"] = []
        pkl_content["meta"]["label_name"] = []
        pkl_content["meta"]["barcode"] = []
        pkl_content["meta"]["product_sn"] = []
        pkl_content["meta"]["category"] = []
        pkl_content["meta"]["bounding_box"] = []
        #pkl_content["meta"]["contour"] = [] 
        pkl_content["embeddings"] = []
        pkl_content["pkl_key"] = pkl_key
        pkl_content["company_sn"] = company_sn
        pkl_content["service_sn"] = service_sn
        pkl_content["branch_sn"] = branch_sn
        for k, v in feature_data.items() :
            if v["product_sn"] in product_enabled_data :
                pkl_content["meta"]["image_sn"].append(v["image_sn"])
                pkl_content["meta"]["sku"].append(product_enabled_data[v["product_sn"]]["sku"])
                pkl_content["meta"]["instance_sn"].append(k)
                pkl_content["meta"]["label_name"].append(product_enabled_data[v["product_sn"]]["product_name"])
                pkl_content["meta"]["barcode"].append(product_enabled_data[v["product_sn"]]["barcode"])
                pkl_content["meta"]["product_sn"].append(v["product_sn"])
                pkl_content["meta"]["category"].append(product_enabled_data[v["product_sn"]]["category"])
                pkl_content["meta"]["bounding_box"].append({"x" : v["x"], "y" : v["y"], "w" : v["w"], "h" : v["h"]})
                #pkl_content["meta"]["contour"].append({"contour" : v["contour"]})
                pkl_content["embeddings"].append(v["feature"]) 
                sku = product_enabled_data[v["product_sn"]]["sku"]
                feature_sn = k
                product_name = product_enabled_data[v["product_sn"]]["product_name"]
                barcode = product_enabled_data[v["product_sn"]]["barcode"]
                rs = vcms_db_agent._add_company_service_pkl_content_data(feature_pkl_sn,company_sn,service_sn,branch_sn,
                                                                         pkl_key,v["image_sn"],sku,feature_sn,
                                                                         v["product_sn"],product_name,barcode,v["feature"])            
        #print ("file data end : " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        for each_key in pkl_content['meta']:
            pkl_content["meta"][each_key] = numpy.asarray(pkl_content["meta"][each_key])[:,numpy.newaxis]
        pkl_content["embeddings"] = numpy.asarray(pkl_content["embeddings"],dtype=numpy.float32)
        return self.create_pkl_file(company_sn,pkl_key,pkl_content,service_sn)

    def __get_branch_product_features(self, pkl_key, company_sn = 0,service_sn = 0, branch_sn = 0) :
        vcms_db_agent = VcmsFeatureDbAgent()
        vcms_db_agent._del_company_service_pkl_data(company_sn,service_sn,branch_sn)
        feature_pkl_sn = vcms_db_agent._add_company_service_pkl_data(company_sn,service_sn,branch_sn,pkl_key)
        #vcms_db_agent._reset_feature_enabled_by_product_status(company_sn,service_sn)
        product_enabled_data = vcms_db_agent._get_company_service_product_enabled_status_data(company_sn,service_sn,1)
        branch_product_data = vcms_db_agent._get_company_service_branch_product_enabled_status_data(company_sn,service_sn,branch_sn,1)
        feature_data = vcms_db_agent._get_company_service_product_features(company_sn,service_sn)
        for k, v in feature_data.items() :
            if int(v["product_sn"]) not in branch_product_data :
                continue
            sku = product_enabled_data[v["product_sn"]]["sku"]
            feature_sn = k
            product_name = product_enabled_data[v["product_sn"]]["product_name"]
            barcode = product_enabled_data[v["product_sn"]]["barcode"]
            rs = vcms_db_agent._add_company_service_pkl_content_data(feature_pkl_sn,company_sn,service_sn,branch_sn,
                                                                     pkl_key,v["image_sn"],sku,feature_sn,
                                                                     v["product_sn"],product_name,barcode,v["feature"])
        return 0

    def run(self,detection = 1) :
        if detection == 1 :
            self.__get_image_for_detections()
        else :
            self.__get_images_for_features()
        return 0

    def __get_image_for_detections(self) :
        vcms_db_agent = VcmsFeatureDbAgent()
        locker = vcms_db_agent._get_system_lock_for_uploading_images()["lock_mark"]
        if int(locker) == 1 :
            print ("image uploading is locked,please unlock or use batch mode commands.")
            exit()
        image_list = vcms_db_agent._get_image_for_detections()
        api_settings = vcms_db_agent._get_company_all_api_settings()
        for key,value in image_list.items() :
            vcms_db_agent._set_processing_time_for_detections(value["sn"])
            if not os.path.exists(os.getcwd() + value["thumbnail"]) :
                print ("detection ignore : " + os.getcwd() + value["thumbnail"])
                continue
            b64 = base64.encodebytes(open(os.getcwd() + value["thumbnail"],"rb").read())
            base64_image = self.base64_image_prefix + b64.decode("utf8")
            data = {"image" : base64_image}
            if int(value["company_sn"]) in api_settings :
                if int(value["service_sn"]) in api_settings[int(value["company_sn"])] :
                    api = api_settings[int(value["company_sn"])][int(value["service_sn"])]["detection_api"]
                    print (api + " sending")
                    image_detections = json.loads((self.request_post(api,data,0).content).decode("utf-8"))
                    self.get_respond_detection_data(value,image_detections)
                else :
                    print (api + " service sn error! [detection]")
            else :
                print (api + " company sn error! [detection]")
        return 0

    def __get_images_for_features(self) :
        vcms_db_agent = VcmsFeatureDbAgent()
        locker = vcms_db_agent._get_system_lock_for_uploading_images()["lock_mark"]
        if int(locker) == 1 :
            print ("image uploading is locked,please unlock or use batch mode commands.")
            exit()
        image_list = vcms_db_agent._get_image_for_features()
        api_settings = vcms_db_agent._get_company_all_api_settings()
        for key,value in image_list.items() :
            vcms_db_agent._set_processing_time_for_features(value["sn"])
            if not os.path.exists(os.getcwd() + value["thumbnail"]) :
                print ("feature ignore : " + os.getcwd() + value["thumbnail"])
                continue
            detection_data = vcms_db_agent._get_image_detection_for_feature(value["sn"])
            b64 = base64.encodebytes(open(os.getcwd() + value["thumbnail"],"rb").read())
            base64_image = b64.decode("utf8")
            feature = collections.OrderedDict()
            feature["image"] = [{
                                 "image_data" : base64_image,
                                 "image_key": str(value["sn"]),
                                 "instance": [] 
                                }]
            instance = []
            for k,v in detection_data.items() :
                instance.append({
                                 "bounding_box" : {
                                                   "x" : v["x"],
                                                   "y" : v["y"],
                                                   "w" : v["w"],
                                                   "h" : v["h"]
                                                  },
                                 "contour" : v["contour"],
                                 "instance_key" : str(v["sn"])
                                })
            feature["image"][0]["instance"] = instance
            if int(value["company_sn"]) in api_settings :
                if int(value["service_sn"]) in api_settings[int(value["company_sn"])] :
                    api = api_settings[int(value["company_sn"])][int(value["service_sn"])]["feature_api"]
                    print (api + " sending")
                    image_features = json.loads((self.request_post(api,feature,1).content).decode("utf-8"))
                    self.get_respond_feature_data(value,image_features)
                else :
                    print (api + " service sn error! [feature]")
            else :
                    print (api + " company sn error! [feature]")
        return 0
 
    def get_respond_detection_data(self,image_data,detection_data) :
        #print (detection_data)
        vcms_db_agent = VcmsFeatureDbAgent()
        image_sn = image_data["sn"]
        #vcms_db_agent._set_processing_time_for_detections(image_sn)
        if detection_data["code"] == "0001" :
            company_sn = image_data["company_sn"] 
            service_sn = image_data["service_sn"]
            product_sn = image_data["product_sn"]
            #vcms_db_agent._set_processing_time_for_detections(image_sn)
            i = 0
            for row in detection_data["data"]["detection"] :
                if i == 0 :
                    vcms_db_agent._reset_result_for_detections(image_sn)
                for row2 in row["instance"] :
                    i += 1  
                    x = row2["bounding_box"]["x"]
                    y = row2["bounding_box"]["y"]
                    w = row2["bounding_box"]["w"]
                    h = row2["bounding_box"]["h"]
                    contour = row2["contour"][0]
                    vcms_db_agent._set_result_for_detections(company_sn,service_sn,product_sn,
                                                             image_sn,x,y,w,h,contour)
            vcms_db_agent._set_finish_time_for_detections(image_sn,i)
        return 0

    def get_respond_feature_data(self,image_data,feature_data) :
        #print(feature_data)
        vcms_db_agent = VcmsFeatureDbAgent()
        image_sn = image_data["sn"]
        #vcms_db_agent._set_processing_time_for_features(image_sn)
        if feature_data["code"] == "0001" :
            for row in feature_data["data"]["feature"][0]["instance"] :
                vcms_db_agent._set_result_for_features(int(row["instance_key"]),row["feature"])
            vcms_db_agent._set_finish_time_for_features(image_sn) 
        return 0

    def _set_image_detection_for_search(self,company_sn,service_sn,base64_image) :
        save_image_path = os.getcwd() + "/static/uploads/self_test"
        if not os.path.exists(save_image_path) :
            os.makedirs(save_image_path)
        save_folder_path = save_image_path + "/" + str(company_sn)
        if not os.path.exists(save_folder_path) :
            os.makedirs(save_folder_path)
        folder_name = datetime.datetime.now().strftime("%Y-%m-%d")
        final_save_path = save_folder_path + "/" + folder_name
        if not os.path.exists(final_save_path) :
            os.makedirs(final_save_path)
        system_file_name = str(uuid.uuid4()).replace("-","")
        sys_image_file_name = system_file_name + ".jpg"
        thumbnail = os.path.join(final_save_path,sys_image_file_name)
        with open(thumbnail,"wb") as f:
            f.write(base64.decodebytes(base64_image.encode("utf8")))
        f.close()
        vcms_db_agent = VcmsFeatureDbAgent()
        api_settings = vcms_db_agent._get_company_all_api_settings()
        data = {"image" : self.base64_image_prefix + base64_image}
        api = api_settings[company_sn][service_sn]["detection_api"]
        image_detections = json.loads((self.request_post(api,data,0).content).decode("utf-8"))
        #print (image_detections)
        return self._set_images_for_features_for_search(base64_image,api_settings,image_detections,company_sn,service_sn,final_save_path,system_file_name)

    def _set_images_for_features_for_search(self,base64_image,api_settings,detection_data,company_sn,service_sn,final_save_path,system_file_name) :
        return_data = collections.OrderedDict()
        return_data["code"] = "0001"
        return_data["message"] = ""
        return_data["data"] = collections.OrderedDict()
        return_data["data"]["checkout"] = []
        if detection_data["code"] == "0001" :
            feature = collections.OrderedDict()
            feature["image"] = [{
                                 "image_data" : base64_image,
                                 "image_key": "self_test",
                                 "instance": []
                                }]
            instance = []
            box = {}
            i = 0
            for row in detection_data["data"]["detection"][0]["instance"] :
                instance.append({
                                 "bounding_box" : {
                                                   "x" : row["bounding_box"]["x"],
                                                   "y" : row["bounding_box"]["y"],
                                                   "w" : row["bounding_box"]["w"],
                                                   "h" : row["bounding_box"]["h"]
                                                  },
                                 "contour" : row["contour"][0],
                                 "instance_key" : str(i)
                                })
                box[i] = {
                          "bounding_box" : {
                                            "x" : row["bounding_box"]["x"],
                                            "y" : row["bounding_box"]["y"],
                                            "w" : row["bounding_box"]["w"],
                                            "h" : row["bounding_box"]["h"]
                                           }
                         }
                i += 1
            feature["image"][0]["instance"] = instance
            api = api_settings[company_sn][service_sn]["feature_api"]
            image_features = json.loads((self.request_post(api,feature,1).content).decode("utf-8"))
            return self.get_respond_feature_data_for_search(image_features,box,company_sn,service_sn,final_save_path,system_file_name)
        return return_data

    def get_respond_feature_data_for_search(self,feature_data,box,company_sn,service_sn,final_save_path,system_file_name) :
        #print(feature_data)
        return_data = collections.OrderedDict()
        return_data["code"] = "0001"
        return_data["message"] = ""
        return_data["data"] = collections.OrderedDict()
        return_data["data"]["checkout"] = []
        instance = []
        if feature_data["code"] == "0001" :
            vcms_db_agent = VcmsFeatureDbAgent()
            i = 1
            for row in feature_data["data"]["feature"][0]["instance"] :
                return_data["data"]["checkout"].append({
                                                        "bounding_box" : box[int(row["instance_key"])]["bounding_box"],
                                                        "instance_key" : row["instance_key"],
                                                        "data_map" : i
                                                       })
                i += 1
            if feature_data["data"]["feature"][0]["instance"] :
                rs = vcms_db_agent._get_search_product_by_binding_feature(company_sn,service_sn,feature_data["data"]["feature"][0]["instance"])
                for row2 in return_data["data"]["checkout"] :
                    if int(row2["data_map"]) in rs :
                        row2.update(rs[int(row2["data_map"])])
        service_list = vcms_db_agent._get_company_service_data(company_sn)
        if service_sn in service_list :
            if service_list[int(service_sn)]["system_service_sn"] == 9 :
                anchor_data = self._get_all_product_features_for_area("test",company_sn,service_sn,0)
                output_data = return_data["data"]["checkout"]
                compare_result = self.compare_area(output_data, anchor_data)
                return_data["data"]["checkout"] = compare_result
        #print (return_data)
        #print(json.dumps(return_data))
        json_path = final_save_path + "/" + system_file_name + ".json"
        try :
            with open(json_path, "w") as f:
                json.dump(return_data,f,ensure_ascii=False)
        except :
            print("json error")
        return return_data

    def _reset_all_detection_feature(self) :
        VcmsFeatureDbAgent()._reset_all_detection_feature_data()
        return 0

    def _batch_all_detection_feature(self,company_sn = 0) :
        vcms_db_agent = VcmsFeatureDbAgent()
        locker = vcms_db_agent._get_system_lock_for_uploading_images()["lock_mark"]
        if int(locker) == 0 :
            print ("image uploading is unlocked,please lock image uploading.")
            exit()
        company_list = vcms_db_agent._get_all_company_data()
        if int(company_sn) > 0 :
            print ("for single company : " + str(company_sn))
            if int(company_sn) in company_list :
                print (company_list[int(company_sn)])
                service_list = vcms_db_agent._get_company_service_data(company_sn)
                print (service_list)
                for key,value in service_list.items() :
                    if int(value["deprecated"]) == 1 :
                        continue
                    if int(value["enabled"]) == 0 :
                        continue
                    self.__get_company_image_for_detections(int(value["company_sn"]),int(value["sn"]))
                    self.__get_company_image_for_features(int(value["company_sn"]),int(value["sn"]))
                    self.__reset_company_feature_status_by_product_and_image(int(value["company_sn"]),int(value["sn"]))
        else :
            for key,value in company_list.items() :
                if int(value["sn"]) == 1 :
                    #ignore viscovery
                    continue
                if int(value["enabled"]) == 0 :
                    continue
                service_list = vcms_db_agent._get_company_service_data(int(value["sn"]))
                print (service_list)
                for key2,value2 in service_list.items() :
                    if int(value2["deprecated"]) == 1 :
                        continue
                    if int(value2["enabled"]) == 0 :
                        continue
                    self.__get_company_image_for_detections(int(value2["company_sn"]),int(value2["sn"]))
                    self.__get_company_image_for_features(int(value2["company_sn"]),int(value2["sn"]))
                    self.__reset_company_feature_status_by_product_and_image(int(value2["company_sn"]),int(value2["sn"]))
        return 0

    def __get_company_image_for_detections(self,company_sn = 0,service_sn = 0) :
        print ("company : " + str(company_sn) + " service_sn : " + str(service_sn) + " detection  start !")
        vcms_db_agent = VcmsFeatureDbAgent()
        image_list = vcms_db_agent._get_company_service_image_for_detections(company_sn,service_sn)
        api_settings = vcms_db_agent._get_company_all_api_settings()
        for key,value in image_list.items() :
            vcms_db_agent._set_processing_time_for_detections(value["sn"])
            if not os.path.exists(os.getcwd() + value["thumbnail"]) :
                print ("detection ignore : " + os.getcwd() + value["thumbnail"])
                continue
            b64 = base64.encodebytes(open(os.getcwd() + value["thumbnail"],"rb").read())
            base64_image = self.base64_image_prefix + b64.decode("utf8")
            data = {"image" : base64_image}
            if int(value["company_sn"]) in api_settings :
                if int(value["service_sn"]) in api_settings[int(value["company_sn"])] :
                    api = api_settings[int(value["company_sn"])][int(value["service_sn"])]["detection_api"]
                    print (api + " sending")
                    image_detections = json.loads((self.request_post(api,data,0).content).decode("utf-8"))
                    self.get_respond_detection_data(value,image_detections)
                else :
                    print (api + " service sn error! [detection]")
            else :
                print (api + " company sn error! [detection]")
        return 0
 
    def __get_company_image_for_features(self,company_sn = 0,service_sn = 0) :
        print ("company : " + str(company_sn) + " service_sn : " + str(service_sn) + " feature start !")
        vcms_db_agent = VcmsFeatureDbAgent()
        image_list = vcms_db_agent._get_company_service_image_for_features(company_sn,service_sn)
        api_settings = vcms_db_agent._get_company_all_api_settings()
        for key,value in image_list.items() :
            vcms_db_agent._set_processing_time_for_features(value["sn"])
            if not os.path.exists(os.getcwd() + value["thumbnail"]) :
                print ("feature ignore : " + os.getcwd() + value["thumbnail"])
                continue
            detection_data = vcms_db_agent._get_image_detection_for_feature(value["sn"])
            b64 = base64.encodebytes(open(os.getcwd() + value["thumbnail"],"rb").read())
            base64_image = b64.decode("utf8")
            feature = collections.OrderedDict()
            feature["image"] = [{
                                 "image_data" : base64_image,
                                 "image_key": str(value["sn"]),
                                 "instance": []
                                }]
            instance = []
            for k,v in detection_data.items() :
                instance.append({
                                 "bounding_box" : {
                                                   "x" : v["x"],
                                                   "y" : v["y"],
                                                   "w" : v["w"],
                                                   "h" : v["h"]
                                                  },
                                 "contour" : v["contour"],
                                 "instance_key" : str(v["sn"])
                                })
            feature["image"][0]["instance"] = instance
            if int(value["company_sn"]) in api_settings :
                if int(value["service_sn"]) in api_settings[int(value["company_sn"])] :
                    api = api_settings[int(value["company_sn"])][int(value["service_sn"])]["feature_api"]
                    print (api + " sending")
                    image_features = json.loads((self.request_post(api,feature,1).content).decode("utf-8"))
                    self.get_respond_feature_data(value,image_features)
                else :
                    print (api + " service sn error! [feature]")
            else :
                    print (api + " company sn error! [feature]")
        return 0

    def __reset_company_feature_status_by_product_and_image(self,company_sn = 0,service_sn = 0) :
        print ("company : " + str(company_sn) + " service_sn : " + str(service_sn) + " reset status start !")
        vcms_db_agent = VcmsFeatureDbAgent()
        disabled_product_list = vcms_db_agent._get_company_service_product_enabled_status_data(int(company_sn),int(service_sn),0)
        for key,value in disabled_product_list.items() :
            vcms_db_agent._reset_feature_by_product_status(int(value["company_sn"]),int(value["service_sn"]),int(value["product_sn"]),0)
        disabled_product_image_list = vcms_db_agent._get_company_service_product_image_enabled_status_data(int(company_sn),int(service_sn),0) 
        for key,value in disabled_product_image_list.items() :
            vcms_db_agent._reset_feature_by_product_image_status(int(value["company_sn"]),int(value["service_sn"]),int(value["image_sn"]),0) 
        deprecated_product_image_list = vcms_db_agent._get_company_service_product_image_deprecated_status_data(int(company_sn),int(service_sn),1)
        for key,value in deprecated_product_image_list.items() :
            vcms_db_agent._reset_feature_by_product_image_status(int(value["company_sn"]),int(value["service_sn"]),int(value["image_sn"]),0)
        return 0

    def clean_empty_image_file(self,company_sn) :
        vcms_db_agent = VcmsFeatureDbAgent()
        company_list = vcms_db_agent._get_all_company_data()
        for key,value in company_list.items() :
            if int(value["enabled"]) == 0 :
                continue
            if int(company_sn) != int(value["sn"]) :
                continue
            service_list = vcms_db_agent._get_company_service_data(int(value["sn"]))
            for key2,value2 in service_list.items() :
                if int(value2["deprecated"]) == 1 :
                    continue
                if int(value2["enabled"]) == 0 :
                    continue
                check_list = vcms_db_agent._get_company_service_product_image_deprecated_status_data(int(value2["company_sn"]),int(value2["sn"]),0)
                i = 0
                for key3,value3 in check_list.items() :
                    image_path = os.getcwd() + value3["thumbnail"]
                    if not os.path.exists(image_path) :
                        i += 1
                        print (image_path + " clean!")
                        vcms_db_agent._set_image_status_by_file_status(int(value3["sn"]),0,1)
                        vcms_db_agent._reset_feature_by_product_image_status(int(value3["company_sn"]),int(value3["service_sn"]),int(value3["sn"]),0)
                    else :
                        if os.stat(image_path).st_size <= 0 :
                            i += 1
                            print (image_path + " clean!")
                            vcms_db_agent._set_image_status_by_file_status(int(value3["sn"]),0,1)
                            vcms_db_agent._reset_feature_by_product_image_status(int(value3["company_sn"]),int(value3["service_sn"]),int(value3["sn"]),0)
                print ("comapny " + str(value2["company_sn"]) + " service : " + str(value2["sn"]) + " clean : " + str(i) )
        return 0

    def calculate_area(self,bbox):
        return bbox[2] * bbox[3]

    def compare_area(self,output_datas, anchor_data):
        try:
            for i, output_data in enumerate(output_datas):
                difference_dict = {}
                output_bbox = [output_data["bounding_box"]["x"], output_data["bounding_box"]["y"],
                              output_data["bounding_box"]["w"], output_data["bounding_box"]["h"]]
                output_area = self.calculate_area(output_bbox)
                output_label_name = output_data["name"]
                output_label_name_index = anchor_data["meta"]["label_name"].tolist().index([output_label_name])
                output_cate_name = anchor_data["meta"]["category"].tolist()[output_label_name_index]
                if output_cate_name == [None]:
                    continue
                match_anchor_index = numpy.where(anchor_data["meta"]["category"] == [output_cate_name])[0]
                for j, anchor_index in enumerate(match_anchor_index):
                    bbox = [anchor_data["meta"]["bounding_box"][anchor_index][0]["x"], anchor_data["meta"]["bounding_box"][anchor_index][0]["y"],
                            anchor_data["meta"]["bounding_box"][anchor_index][0]["w"], anchor_data["meta"]["bounding_box"][anchor_index][0]["h"]]
                    area = self.calculate_area(bbox)
                    difference_dict[anchor_index] = abs(output_area - area)
                min_difference = min(difference_dict.values())
                min_difference_index = list(difference_dict.keys())[list(difference_dict.values()).index(min_difference)]
                output_data["name"] = anchor_data["meta"]["label_name"][min_difference_index][0]
                output_data["product_sn"] = int(anchor_data["meta"]["product_sn"][min_difference_index][0])
                output_data["product_name"] = anchor_data["meta"]["label_name"][min_difference_index][0]
                output_data["sku"] = anchor_data["meta"]["sku"][min_difference_index][0]
                output_data["barcode"] = anchor_data["meta"]["barcode"][min_difference_index][0]
                output_datas[i] = output_data
        except Exception as ex:
            print('{}'.format(ex))
        return output_datas

    def _get_all_product_features_for_area(self, pkl_key, company_sn = 0,service_sn = 0, branch_sn = 0) :
        vcms_db_agent = VcmsFeatureDbAgent()
        vcms_db_agent._del_company_service_pkl_data(company_sn,service_sn,branch_sn)
        feature_pkl_sn = vcms_db_agent._add_company_service_pkl_data(company_sn,service_sn,branch_sn,pkl_key)
        #vcms_db_agent._reset_feature_enabled_by_product_status(company_sn,service_sn)
        product_enabled_data = vcms_db_agent._get_company_service_product_enabled_status_data(company_sn,service_sn,1)
        print ("data start : " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        feature_data = vcms_db_agent._get_company_service_product_features(company_sn,service_sn)
        print ("data end : " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        #print ("file data start : " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        pkl_content = edict({})
        pkl_content["meta"] = {}
        pkl_content["meta"]["image_sn"] = []
        pkl_content["meta"]["sku"] = []
        pkl_content["meta"]["instance_sn"] = []
        pkl_content["meta"]["label_name"] = []
        pkl_content["meta"]["barcode"] = []
        pkl_content["meta"]["product_sn"] = []
        pkl_content["meta"]["category"] = []
        pkl_content["meta"]["bounding_box"] = []
        #pkl_content["meta"]["contour"] = []
        pkl_content["embeddings"] = []
        pkl_content["pkl_key"] = pkl_key
        pkl_content["company_sn"] = company_sn
        pkl_content["service_sn"] = service_sn
        pkl_content["branch_sn"] = branch_sn
        for k, v in feature_data.items() :
            if v["product_sn"] in product_enabled_data :
                pkl_content["meta"]["image_sn"].append(v["image_sn"])
                pkl_content["meta"]["sku"].append(product_enabled_data[v["product_sn"]]["sku"])
                pkl_content["meta"]["instance_sn"].append(k)
                pkl_content["meta"]["label_name"].append(product_enabled_data[v["product_sn"]]["product_name"])
                pkl_content["meta"]["barcode"].append(product_enabled_data[v["product_sn"]]["barcode"])
                pkl_content["meta"]["product_sn"].append(v["product_sn"])
                pkl_content["meta"]["category"].append(product_enabled_data[v["product_sn"]]["category"])
                pkl_content["meta"]["bounding_box"].append({"x" : v["x"], "y" : v["y"], "w" : v["w"], "h" : v["h"]})
                #pkl_content["meta"]["contour"].append({"contour" : v["contour"]})
                pkl_content["embeddings"].append(v["feature"])
                sku = product_enabled_data[v["product_sn"]]["sku"]
                feature_sn = k
                product_name = product_enabled_data[v["product_sn"]]["product_name"]
                barcode = product_enabled_data[v["product_sn"]]["barcode"]
                rs = vcms_db_agent._add_company_service_pkl_content_data(feature_pkl_sn,company_sn,service_sn,branch_sn,
                                                                         pkl_key,v["image_sn"],sku,feature_sn,
                                                                         v["product_sn"],product_name,barcode,v["feature"])
        #print ("file data end : " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        for each_key in pkl_content['meta']:
            pkl_content["meta"][each_key] = numpy.asarray(pkl_content["meta"][each_key])[:,numpy.newaxis]
        pkl_content["embeddings"] = numpy.asarray(pkl_content["embeddings"],dtype=numpy.float32)
        return pkl_content
