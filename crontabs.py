import sys,os,inspect,traceback
import json,collections,datetime,time
os_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(os_path + '/lib/')
sys.path.append(os_path + '/utils/')
sys.path.append(os_path + '/conf/')
sys.path.append(os_path + '/system_service_models/')
from utils.jsonloader import Jsonloader
from system_service_models.embedding import Embedding
from system_service_models.classification import Classification
from system_service_models.csvmanage import Csvmanage

config_path = os_path + "/conf/"
try :
    config = Jsonloader(config_path + "default.conf").getJsonDataMapping()
    cron_enabled = int(config[config["env"]]["cron_enabled"])
    if cron_enabled == 1 :
        api_setting = config_path + config["project_name"] + "/" +config[config["env"]]["api_setting"]
        api_config = Jsonloader(api_setting).getJsonDataMapping()
        start = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if sys.argv[1] == "embedding_detection" :
            print ("embedding... detection")
            for i in range(4) :
                print ("cnt : " + str(i))
                Embedding(api_config).run(1)
                time.sleep(15)
        if sys.argv[1] == "embedding_feature" :
            print ("embedding... feature")
            for i in range(4) :
                print ("cnt : " + str(i))
                Embedding(api_config).run(2)
                time.sleep(15)
        if sys.argv[1] == "classification" :
            print ("classification...")
            Classification().run()
        if sys.argv[1] == "csv_product" :
            print ("importing product")
            Csvmanage().import_product_by_csv()
        if sys.argv[1] == "csv_image" :
            print ("importing images")
            Csvmanage().import_product_image_by_csv()
        if sys.argv[1] == "pkl" :
            print ("export pkl ...")
            Embedding(api_config).create_company_pkl_file_for_deployment()
        if sys.argv[1] == "single_pkl" :
            print ("export single pkl ...")
            Embedding(api_config).create_single_company_pkl_file_for_deployment(int(sys.argv[2]))
        if sys.argv[1] == "set_product_image" :
            Csvmanage().set_product_image() 
        if sys.argv[1] == "reset_detection_feature" :
            print ("reset detection feature !")
            Embedding(api_config)._reset_all_detection_feature()
        if sys.argv[1] == "batch_detection_feature" :
            print ("batch detection feature !")
            Embedding(api_config)._batch_all_detection_feature(int(sys.argv[2]))
        if sys.argv[1] == "clean_image" :
            print ("clean image !")
            Embedding(api_config).clean_empty_image_file(int(sys.argv[2]))
        end = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print (start + " - " + end)
    else :
        print ("crontab is disabled!")
except :
    print (traceback.format_exc())

#def get_data() :
#    permission = inspect.currentframe().f_code.co_name
#    print (permission)

