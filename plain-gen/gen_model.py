import json
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--case')
args = parser.parse_args()

case = args.case

def read_input(filename):
    with open("models/{}/model.json".format(case)) as json_file:
        data = json.load(json_file)
        return data

def create_list_imports(json_data):
    layers = set()
    layers_info = json_data["layers"]
    for item in layers_info:
        layers.add(item["type"])
    return layers

def create_model_imports_file(json_data, layers):
    output = "from tensorflow.keras.models import Sequential\n"
    for item in layers:
        output = output + "from tensorflow.keras.models import {}\n".format(item)
    return output

def create_init_model_func(json_data):
    output = "def init_model():\n    model = Sequential()\n"
    for item in json_data["layers"]:
        output = output + "    model.add({}(".format(item["type"])
        if "params" not in item:
            output = output + "))\n"
        else:
            for key, value in item["params"].items():
                if type(value) is str:
                    output = output + "{}=\"{}\",".format(key,value)
                else:
                    output = output + "{}={},".format(key,value)
            output = output + ")\n"
    output = output + "    return model"
    return output


inp = read_input("model.json")
l = create_list_imports(inp)
imports = create_model_imports_file(inp, l)
result = create_init_model_func(inp)
to_file = imports + "\n" + result

with open(f'models/{case}/generated-p/model.py', 'w') as f:
    f.write(to_file)
#f = open('../generated/model.py', 'w')
#f.write(to_file)
#f.close()
