import json
import sys
import os

import black

import jinja2py

output_dir = 'sample/generated/'

generate_names = [
  'cli',
  'model',
  'ng_bus',
  'ng_input',
  'train',
]

model = json.load(open('sample/model.json'))

for name in generate_names:
  input_name = name + '.py'
  if not os.path.exists('templates/' + input_name):
    input_name += '.jinja2'
    code = jinja2py.render_with_indents(input_name, model=model, str=str, repr=repr)
  else:
    code = open('templates/' + input_name).read()
  try:
    code = black.format_str(code, mode=black.FileMode())
  except:
    print('black had error formatting code:', file=sys.stderr)
    print(code, file=sys.stderr)
    raise
  with open(output_dir + name + '.py', 'w') as f:
    f.write(code)
