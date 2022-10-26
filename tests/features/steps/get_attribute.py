import json
import time

class GetAttribute(object):
  
    def get_data(self, call: str):
        
        self.f = open('./../tools/generic_conf.json', "r")
               
        data = json.loads(self.f.read())

        time.sleep(3)
        
        data_back = (data[call])
        self.f.close()


        return data_back
  
    
        