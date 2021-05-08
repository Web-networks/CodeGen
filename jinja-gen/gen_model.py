import argparse
import json
import sys
import os

import black

import jinja2py
from pathlib import Path


def render_template(model, template_name):
    input_template = template_name + '.py.jinja2'
    code = jinja2py.render_with_indents(
        input_template, model=model, str=str, repr=repr,
        layer_types=set(map(lambda x: x['type'], model['layers'])),
    )
    return code


def format_and_write(template_name, code, output_dir):
    try:
        code = black.format_str(code, mode=black.FileMode())
    except:
        print('black had error formatting code:', file=sys.stderr)
        print(code, file=sys.stderr)
        raise
    with open(output_dir + template_name + '.py', 'w') as f:
        f.write(code)

parser = argparse.ArgumentParser()
parser.add_argument('--case')
args = parser.parse_args()

case = args.case

model = json.load(open(f'/home/ekaterina/documents/diploma/CodeGen/models/{case}/model.json'))

list_of_module = []
if case == "sample_alex_net":
    list_of_module = ['model', 'ng_input_alex_net', 'train', 'ng_bus', 'cli-alex-net']
    print("LIST FOR ALEX_NET")
    
else:
    list_of_module = ['model', 'ng_input', 'train', 'ng_bus', 'cli']
    print("ANOTHER LIST")

for module in list_of_module:
    naive_path = f'/home/ekaterina/documents/diploma/CodeGen/jinja-gen/templates/{module}.py'
    if os.path.exists(naive_path):
        print("FILE EXISTS")
        print(naive_path)
        code = open(naive_path).read()
    else:
        print("GENERATING")
        code = render_template(model, module)
    format_and_write(module, code, f'/home/ekaterina/documents/diploma/CodeGen/models/{case}/generated/')