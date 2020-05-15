import json
import os
import os.path
import shutil

def dict_to_json(dict_model):
    with open('sample/model2.json', 'w') as file:
        d = json.dump(dict_model, file)
        #print(d)
		
try_dict={'model_id':1, 'user_id':1}
dict_to_json(try_dict)
#def integration(model_dict, jenv, path_to_generated):
  