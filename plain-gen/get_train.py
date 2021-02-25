import json
import os

def read_input(filename):
    with open('model.json') as json_file:
        data = json.load(json_file)
        return data

def read_prepared_train_file(filename):
	file = open("train_to_gen.py", "r")
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


inp = read_input("model.json")
res2 = generate_do_compile_method(inp)
info = read_prepared_train_file("train_to_gen.py")
source = replace_in_res_file(info, res2)
f = open('train.py', 'w')
f.write(source)
f.close()