import json

import black

import jinja2py

output_dir = 'sample/generated/'

generate_names = [
  'model',
  'train',
]

model = json.load(open('sample/model.json'))

for name in generate_names:
  tpl = jinja2py.get_template(name + '.py.jinja2')
  code = jinja2py.render_with_indents(tpl, model=model, str=str, repr=repr)
  code = black.format_str(code, mode=black.FileMode())
  with open(output_dir + name + '.py', 'w') as f:
    f.write(code)
