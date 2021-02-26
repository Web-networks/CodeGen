import json
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--case')
args = parser.parse_args()

case = args.case

def read_input(filename):
    with open(filename) as json_file:
        data = json.load(json_file)
        return data

def read_prepared_train_file(filename):
	file = open(filename, "r")
	info = file.read()
	return info

def generate_do_compile_method(json_data):
	loss = json_data["loss"]
	optimizer = json_data["optimizer"]
	metrics = json_data["metrics"]
	output = ("    def do_compile(self):\n"
		      "        self.model.compile(loss=\"{}\",".format(loss))
	output = output + "optimizer=\"{}\",".format(optimizer)
	output = output + "metrics=[\"{}\"],)\n".format(metrics)
	return output

def replace_in_res_file(source, target):
	source = source.replace("    def do_compile(self):", target)
	return source


inp = read_input("models/{}/model.json".format(case))
res2 = generate_do_compile_method(inp)
info = read_prepared_train_file("plain-gen/train_to_gen.py")
source = replace_in_res_file(info, res2)
f = open(f'models/{case}/generated-p/train.py', 'w')
f.write(source)
f.close()