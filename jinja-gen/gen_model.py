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
print ("AAAA")
print(model)

print("File      Path:", Path(__file__).absolute())
print("Directory Path:", Path().absolute()) # Directory of current working directory, not __file__  
for module in ['model', 'ng_input', 'train', 'ng_bus', 'cli']:
    naive_path = f'/home/ekaterina/documents/diploma/CodeGen/jinja-gen/templates/{module}.py'
    if os.path.exists(naive_path):
        print("FILE EXISTS")
        code = open(naive_path).read()
    else:
        print("GENERATING")
        code = render_template(model, module)
    format_and_write(module, code, f'/home/ekaterina/documents/diploma/CodeGen/models/{case}/generated/')