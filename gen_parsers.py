import jinja2py
import yaml

schemas = yaml.safe_load(open('definitions.yaml'))['components']['schemas']

tpl = jinja2py.get_template('neurogen_parsers.py.jinja2')

for name in schemas:
  print(jinja2py.render_with_indents(tpl, name=name, schema=schemas[name], print=print))
