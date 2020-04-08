import json
import os
import logging
from pathlib import Path
from utils.logger import Logger

os_path = os.getcwd() 
#os.path.abspath(os.path.dirname(__file__))

class SettingCheck :
 
    check_list = ["check_config","check_controllers"]
    check_result = []
    project_setting = None
    project_config_check = ["method_setting","pgsql_setting"]
    project_check_path = None

    def __init__(self) :
        pass

    def check_config(self) :
        configs = os_path + "/conf/default.conf"
        config_file = Path(configs)
        if not config_file.exists() :   
           self.check_result.append("the file named [default.conf] missed!")
        else : 
            file_open = open(configs)        
            config_setting = json.load(file_open)
            file_open.close()

            if config_setting["project_name"] == "" :
                self.check_result.append("project_name missed!")

            project_conf = ("%s/conf/%s/") % (os_path,config_setting["project_name"])
            self.project_check_path = project_conf
            self.project_setting = config_setting[config_setting["env"]]       
       
            for row in self.project_config_check : 
                project_setting = project_conf + self.project_setting[row]
                project_setting_file = Path(project_setting)
                if not project_setting_file.exists() :
                    self.check_result.append("the file named ["+ self.project_setting[row] +"] missed!")

        return None

    def check_controllers(self) :
        controller_path = "%s%s" % (self.project_check_path,self.project_setting["method_setting"]) 
        file_open = open(controller_path)
        controller_setting = json.load(file_open)
        file_open.close()
        controller_file_path = os_path + "/controllers/"
        for row in controller_setting :
            if int(controller_setting[row]["allow_tag"]) == 0 :
                continue
            controller_file = Path(controller_file_path + row + ".py")
            if not controller_file.exists() :
                controller_file2 = Path(controller_file_path + row + ".pyc")
                if not controller_file2.exists() :
                    self.check_result.append("the file named ["+ row +".pyc] missed!")
        return None

    def run(self) :
        check_point = self.check_list
        for row in check_point :
            getattr(self,row)()

        if len(self.check_result) > 0 :
            for row in self.check_result :
                Logger(logging.DEBUG).logger.error(row) 
            exit("setting error! see the details in log")

