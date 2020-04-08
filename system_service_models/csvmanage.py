import os,sys,traceback
import datetime,time
import collections,math,re,hashlib,shutil,uuid,base64
import zipfile
from utils.csvloader import Csvloader
from werkzeug.utils import secure_filename
from utils.vcmscsvdbagent import VcmsCsvDbAgent

class Csvmanage :

    os_path = None
    ALLOWED_EXTENSIONS = set(['csv','zip'])
    ALLOWED_EXTENSIONS2 = set(['bmp', 'tif', 'png', 'jpg', 'jpeg', 'gif'])

    def __init__(self) :
        sys_path = os.getcwd() + "/uploads"
        if not os.path.exists(sys_path) :
            os.makedirs(sys_path)
        folder_path = sys_path + "/csv"
        if not os.path.exists(folder_path) :
            os.makedirs(folder_path)
        self.os_path = folder_path

    def product_csv_uploads(self,product_file,company_sn,service_sn,user_sn) :
        vcms_csv_db_agent = VcmsCsvDbAgent()
        csv_path = self.os_path + "/"
        return_value = 0
        for row in product_file.getlist("csv_products") :
            if row and self.__allowed_file(row.filename) :
                ori_csv_file_name = str(row.filename)
                filename = secure_filename(row.filename)
                row.save(os.path.join(csv_path, filename))
                sys_csv_file_name = str(uuid.uuid4()).replace("-","") + os.path.splitext(row.filename)[1]
                csv_file = os.path.join(csv_path,sys_csv_file_name)
                shutil.move(os.path.join(csv_path, filename),csv_file)
                csv_sn = vcms_csv_db_agent._set_product_csv_file(company_sn,ori_csv_file_name,sys_csv_file_name,service_sn,user_sn,0)
                return_value = self.product_csv_format_checking(csv_path+sys_csv_file_name , csv_sn)
        return return_value

    def product_csv_format_checking(self,csv_path,csv_sn) :
        return_value = 0
        vcms_csv_db_agent = VcmsCsvDbAgent()
        csv_loader = Csvloader()
        product_data = csv_loader.getCsvDataMapping(csv_path) 
        if len(product_data) > 0 :
            vcms_csv_db_agent._set_csv_enabled_for_importing_products(csv_sn)
            return_value = 1
        return return_value

    def product_image_csv_uploads(self,product_file,company_sn,service_sn,user_sn) :
        vcms_csv_db_agent = VcmsCsvDbAgent()
        csv_path = self.os_path + "/"
        return_value = 0
        check_csv = 0
        for row in product_file.getlist("csv_images") :
            if row and self.__allowed_file(row.filename) :
                ori_csv_file_name = str(row.filename)
                filename = secure_filename(row.filename)
                row.save(os.path.join(csv_path, filename))
                sys_csv_file_name = str(uuid.uuid4()).replace("-","") + os.path.splitext(row.filename)[1]
                csv_file = os.path.join(csv_path,sys_csv_file_name)
                shutil.move(os.path.join(csv_path, filename),csv_file)
                check_csv = 1
        check_zip = 0
        for row in product_file.getlist("zip_images") :
            if row and self.__allowed_file(row.filename) :
                zip_user_file_name = str(row.filename)
                filename = secure_filename(row.filename)
                row.save(os.path.join(csv_path, filename))
                zip_sys_file_name = str(uuid.uuid4()).replace("-","") + os.path.splitext(row.filename)[1]
                zip_file = os.path.join(csv_path,zip_sys_file_name)
                shutil.move(os.path.join(csv_path, filename),zip_file)
                check_zip = 1
        if check_csv == 1 and check_zip == 1 : 
            csv_sn = vcms_csv_db_agent._set_product_image_csv_file(company_sn,ori_csv_file_name,sys_csv_file_name,service_sn,
                                                                   user_sn,0,zip_user_file_name,zip_sys_file_name)
            return_value = self.product_image_csv_format_checking(csv_path+sys_csv_file_name , csv_sn)
        return return_value

    def product_image_csv_format_checking(self,csv_path,csv_sn) :
        return_value = 0
        vcms_csv_db_agent = VcmsCsvDbAgent()
        csv_loader = Csvloader()
        image_data = csv_loader.getCsvDataMapping(csv_path)
        if len(image_data) > 0 :
            vcms_csv_db_agent._set_csv_enabled_for_importing_product_images(csv_sn)
            return_value = 1
        return return_value

    def import_product_by_csv(self) :
        vcms_csv_db_agent = VcmsCsvDbAgent()
        product_csv_list = vcms_csv_db_agent._get_csv_for_importing_products(10)
        csv_loader = Csvloader()
        base_upload_path = "%s/%s/%s" % (os.getcwd(),"static","uploads")
        if not os.path.exists(base_upload_path) :
            os.makedirs(base_upload_path)
        for key,value in product_csv_list.items() :
            product_data = csv_loader.getCsvDataMapping(self.os_path + "/" + value["sys_file_name"])
            company_upload_path = "%s/%s" % (base_upload_path,value["company_sn"])
            if not os.path.exists(company_upload_path) :
                os.makedirs(company_upload_path)
            image_file_path = "%s/%s" % (company_upload_path,value["service_sn"])
            if not os.path.exists(image_file_path) :
                os.makedirs(image_file_path)
            vcms_csv_db_agent._set_file_manage_time_for_importing_products(value["sn"])
            cnt = 0
            for k,v in product_data.items() :
                try :
                    company_sn = int(value["company_sn"])
                    product_csv_sn = value["sn"]
                    sku = v[0]
                    barcode = v[1]
                    product_name = v[2]
                    ori_file_path = None#v[3]
                    sys_file_path = None#image_file_path + "/" + str(uuid.uuid4()).replace("-","") + ".jpg"
                    url = None
                    service_sn = value["service_sn"]
                    ct_user_sn = value["ct_user_sn"]
                    rs_sn = vcms_csv_db_agent._set_product_csv_contents(company_sn,product_csv_sn,sku,barcode,product_name,
                                                                        ori_file_path,sys_file_path,url,service_sn,ct_user_sn)
                    if rs_sn > 0 :
                        cnt += 1
                        #if os.path.exists(ori_file_path) :
                        #    shutil.copy(ori_file_path,sys_file_path)
                        #    print ("product image file copied!")
                except :
                    print ("empty dataset !")
                    continue
            vcms_csv_db_agent._set_file_manage_mark_for_importing_products(value["sn"],cnt)
            self.create_products_by_importing_data(value["sn"])
        return 0

    def create_products_by_importing_data(self,product_csv_sn) :
        vcms_csv_db_agent = VcmsCsvDbAgent()
        product_csv_list = vcms_csv_db_agent._get_product_csv_contents_for_creating_products(product_csv_sn)
        for key,value in product_csv_list.items() :
            vcms_csv_db_agent._set_product_created_time_for_importing_products(value["sn"])
            company_sn = int(value["company_sn"])
            service_sn = int(value["service_sn"])
            barcode = value["barcode"]
            sku = value["sku"]
            product_name = value["product_name"]
            abbreviation = ""
            thumbnail = ""#str(value["sys_file_path"]).replace(os.getcwd(),"")
            ct_user_sn = int(value["ct_user_sn"])
            product_csv_sn = int(value["product_csv_sn"])
            product_check = vcms_csv_db_agent._check_product_by_sku(company_sn,service_sn,sku)
            if product_check == 0 :
                rs_sn = vcms_csv_db_agent._add_company_product_data(company_sn,service_sn,barcode,sku,product_name,
                                                                    abbreviation,thumbnail,ct_user_sn,product_csv_sn)
                if rs_sn > 0 :
                    print ("product created : " + str(rs_sn))
                    vcms_csv_db_agent._set_product_created_mark_for_importing_products(value["sn"])
                else :
                    print ("product ignored : " + str(rs_sn))
                    vcms_csv_db_agent._set_fail_for_importing_products(value["sn"])
        return 0

    def import_product_image_by_csv(self) :
        vcms_csv_db_agent = VcmsCsvDbAgent()
        product_csv_list = vcms_csv_db_agent._get_csv_for_importing_product_images(10)
        csv_loader = Csvloader()
        base_upload_path = "%s/%s/%s" % (os.getcwd(),"static","uploads")
        if not os.path.exists(base_upload_path) :
            os.makedirs(base_upload_path)
        for key,value in product_csv_list.items() :
            product_data = csv_loader.getCsvDataMapping(self.os_path + "/" + value["sys_file_name"])
            company_upload_path = "%s/%s" % (base_upload_path,value["company_sn"])
            if not os.path.exists(company_upload_path) :
                os.makedirs(company_upload_path)
            image_file_path = "%s/%s" % (company_upload_path,value["service_sn"])
            if not os.path.exists(image_file_path) :
                os.makedirs(image_file_path)
            vcms_csv_db_agent._set_file_manage_time_for_importing_product_images(value["sn"])
            cnt = 0
            #print (self.os_path)
            #print (value["zip_user_file_name"])
            #print (value["zip_sys_file_name"])
            zip_path = self.os_path + "/" + value["zip_sys_file_name"]
            unzip_path = self.os_path + "/" + value["zip_sys_file_name"][:-4]
            self.__zip_unzip_file(zip_path,unzip_path)
            for k,v in product_data.items() :
                try :
                    company_sn = int(value["company_sn"])
                    product_image_csv_sn = int(value["sn"])
                    sku = v[0]
                    barcode = v[1]
                    product_name = v[2]
                    ori_file_path = unzip_path + "/" + v[3]
                    sys_file_path = image_file_path + "/" + str(uuid.uuid4()).replace("-","") + ".jpg"
                    url = None
                    service_sn = int(value["service_sn"])
                    ct_user_sn = int(value["ct_user_sn"])
                    enabled = 0
                    if os.path.exists(ori_file_path) and self.__allowed_image_file(ori_file_path) :
                        enabled = 1
                    rs_sn = vcms_csv_db_agent._set_product_image_csv_contents(company_sn,product_image_csv_sn,sku,product_name,
                                                                              ori_file_path,sys_file_path,url,service_sn,ct_user_sn,
                                                                              barcode,enabled)
                    if rs_sn > 0 :
                        cnt += 1
                        if os.path.exists(ori_file_path) :
                            shutil.copy(ori_file_path,sys_file_path)
                            print ("image file copied!")
                except :
                    print ("empty dataset !")
                    continue
            vcms_csv_db_agent._set_file_manage_mark_for_importing_product_images(value["sn"],cnt)
            self.create_product_images_by_importing_data(value["sn"],value["company_sn"],value["service_sn"])
        return 0

    def create_product_images_by_importing_data(self,product_image_csv_sn,company_sn,service_sn) :
        vcms_csv_db_agent = VcmsCsvDbAgent()
        product_csv_list = vcms_csv_db_agent._get_product_image_csv_contents_for_creating_product_images(product_image_csv_sn)
        for key,value in product_csv_list.items() :
            vcms_csv_db_agent._set_image_created_time_for_importing_product_images(value["sn"])
            company_sn = int(value["company_sn"])
            service_sn = int(value["service_sn"])
            product_sn = 0
            #if str(value["product_name"]) in product_sn_list :
            #    product_sn = int(product_sn_list[str(value["product_name"])])
            #sku = value["sku"]
            #product_name = value["product_name"]
            thumbnail = str(value["sys_file_path"]).replace(os.getcwd(),"")
            ct_user_sn = int(value["ct_user_sn"])
            image_csv_sn = int(value["product_image_csv_sn"])
            product_sn_list = vcms_csv_db_agent._get_prod_sku_mapping_data(company_sn,service_sn,value["sku"],value["barcode"],value["product_name"])
            if product_sn_list :
                for k,v in product_sn_list.items() :
                    rs_sn = vcms_csv_db_agent._add_company_product_image_data(company_sn,service_sn,k,thumbnail,ct_user_sn,image_csv_sn)
                    if rs_sn > 0 :
                        print ("product image created : " + str(rs_sn))
                vcms_csv_db_agent._set_image_created_mark_for_importing_product_images(value["sn"])
        vcms_csv_db_agent._reset_product_image_cnt()
        return 0

    def set_product_image(self) :
        vcms_csv_db_agent = VcmsCsvDbAgent()
        product_data = vcms_csv_db_agent._get_empty_main_product_image()
        for k,v in product_data.items() :
            image_data = vcms_csv_db_agent._get_product_images_by_uploading(int(v["company_sn"]),int(v["service_sn"]),int(k))
            if image_data :
                vcms_csv_db_agent._set_main_product_image(int(v["company_sn"]),int(v["service_sn"]),int(k),str(image_data["thumbnail"]))
        return 0

    def __zip_unzip_file(self,zip_path,unzip_path) :
        if os.path.exists(zip_path) :
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(unzip_path)
            folder_list = os.listdir(unzip_path)
            for row in folder_list :
                if not os.path.isdir(unzip_path + "/" + row) :
                    continue
                sub_folder_list = os.listdir(unzip_path + "/" + row)
                for row2 in sub_folder_list :
                     move_file = unzip_path + "/" + row + "/" + row2
                     print (move_file)
                     if not os.path.isdir(move_file) :
                         if not os.path.exists(unzip_path + "/" + row2) : 
                             shutil.move(move_file,unzip_path)
                shutil.rmtree(unzip_path + "/" + row)

    def get_product_csv_log(self,company_sn,service_sn) :
        return VcmsCsvDbAgent()._get_csv_for_importing_products_log(company_sn,service_sn)

    def get_product_csv_error_log(self,company_sn,service_sn,csv_sn) :
        return VcmsCsvDbAgent()._get_download_error_csv_content(company_sn,service_sn,csv_sn)

    def get_product_csv_sucess_log(self,company_sn,service_sn,csv_sn) :
        return VcmsCsvDbAgent()._get_download_success_csv_content(company_sn,service_sn,csv_sn)

    def __allowed_file(self,filename) :
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in self.ALLOWED_EXTENSIONS

    def __allowed_image_file(self,filename) :
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in self.ALLOWED_EXTENSIONS2
