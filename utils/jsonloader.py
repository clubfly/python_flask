try :
    import json
except ImportError :
    import simplejson as json

class Jsonloader :

    data_mapping = {}

    def __init__(self,json_data_list) :
        file_open = open(json_data_list,encoding='utf-8')
        self.data_mapping = json.load(file_open)
        file_open.close()

    def getJsonDataMapping(self) :
        return self.data_mapping
