import os,sys,traceback
import datetime,time
import collections,math,re,hashlib,shutil,uuid,base64,glob,base64
from utils.vcmshrsdbagent import VcmsHrsDbAgent

class Hrs :

    token = "c8337e80cf4149e7a11ef2ed83c92447"
    __max_show_data = 200

    def __init__(self) :
        pass

    def get_token(self) :
        return self.token

    def get_company_info(self,company_sn) :
        return_data = {}
        return_data = VcmsHrsDbAgent()._get_all_company_data()
        return return_data[company_sn]

    def get_company_list(self,token) :
        return_data = {}
        if str(self.token) == str(token) : 
            system_path = os.getcwd()
            return_data = VcmsHrsDbAgent()._get_all_company_data()
            for key,value in return_data.items() :
                image_folder = system_path + "/static/uploads/self_test/" + str(key)
                return_data[key]["folder_list"] = []
                return_data[key]["image_total_list"] = {}
                if os.path.exists(image_folder) :
                    folder_list = os.listdir(image_folder)
                    return_data[key]["folder_list"] = folder_list
                    return_data[key]["folder_list"].sort()
                    for row in return_data[key]["folder_list"] : 
                        image_list = glob.glob(image_folder + "/" + row + "/*.jpg")
                        image_total = len(image_list)
                        return_data[key]["image_total_list"].update({row : row + " (" + str(image_total) + ")"})
        return return_data

    def get_company_product_list(self,token,parameter_dict,pages = 1) :
        return_data = {
                       "product_list" : {},
                       "max_pages" : 1,
                       "pages" : 1,
                       "product_totals" : 0,
                       "service_sn" : 0
                      }
        if str(self.token) == str(token) :
            max_page_show_data = self.__max_show_data
            max_pages = 1
            vcms_hrs_db_agent = VcmsHrsDbAgent()
            service_sn = parameter_dict.get("service_sn")
            search_key = parameter_dict.get("search")
            db_data_cnt = vcms_hrs_db_agent._get_company_service_product_cnt(int(service_sn),search_key)
            if db_data_cnt > 0 :
                max_pages = math.ceil(db_data_cnt/max_page_show_data)
            if int(pages) == 0 :
                pages = 1
            if int(pages) >= max_pages :
                pages = max_pages
            offset = (int(pages) - 1) * max_page_show_data
            company_sn = 0
            product_list = vcms_hrs_db_agent._get_company_service_product_data(int(service_sn),search_key,max_page_show_data,offset)
            return_data["product_list"] = product_list
            return_data["max_pages"] = max_pages
            return_data["pages"] = pages
            return_data["service_sn"] = int(service_sn)
            return_data["product_totals"] = db_data_cnt
            try :
                for k,v in product_list.items() :
                    company_sn = int(v["company_sn"])
                return_data["company_name"] = self.get_company_info(int(company_sn))["company_name"]
            except :
                return_data["company_name"] = ""
        return return_data

    def get_company_self_test_images(self,token,company_sn,parameter_dict,pages = 1) :
        return_data = []
        image_total = 0
        if str(self.token) == str(token) :
            folder = parameter_dict.get("folder")
            system_path = os.getcwd()
            image_folder = system_path + "/static/uploads/self_test/" + str(company_sn) +"/" + folder + "/*.jpg"
            image_list = glob.glob(image_folder)
            image_total = len(image_list)
            for row in image_list : 
                b64 = base64.encodestring(open(row,"rb").read())
                return_data.append({
                                    "b64" : b64.decode("utf8"),
                                    "file_name" : os.path.basename(row)
                                   })
        return image_total,return_data
