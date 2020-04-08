import csv

class Csvloader :

    data_mapping = {}

    def __init__(self) :
        pass

    def getCsvDataMapping(self,csv_data_path) :
        self.data_mapping = {}
        with open(csv_data_path,encoding='utf-8',newline="") as csvfile :
            data_mapping = csv.reader(csvfile,delimiter=",")
            i = 0
            for row in data_mapping :
                if i > 0 :
                    self.data_mapping[i] = row
                i += 1
        return self.data_mapping
