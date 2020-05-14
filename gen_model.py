import json
import sys
import os

import black

import jinja2py
        
def integration(model, template_name, output_dir):
    input_template = template_name + '.py.jinja2'
    code = jinja2py.render_with_indents(input_template, model=model, str=str, repr=repr)
    try:
        code = black.format_str(code, mode=black.FileMode())
    except:
        print('black had error formatting code:', file=sys.stderr)
        print(code, file=sys.stderr)
        raise
    with open(output_dir + template_name + '.py', 'w') as f:
        f.write(code)
        
# Example how to run such function      
model = json.load(open('sample/vgg.json'))
integration(model, 'model', 'sample/generated/')
integration(model, 'ng_input', 'sample/generated/')
integration(model, 'train', 'sample/generated/')