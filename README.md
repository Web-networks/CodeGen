Кодогенерация на базе jinja2

Как это работает:

```sh
# Setting up environment
virtualenv -p python3 venv
. venv/bin/activate
pip install -r requirements.txt

# Take yaml from schemas repo
cp ../schemas/definitions.yaml .

# Running parsers codegen
python3 gen_parsers.py > generated/neurogen_parsers.py

# Formatting
black generated/neurogen_parsers.py
```

Вывод шаблонизатора дополнительно обрабатывается. Это нужно, т.к. Python целиком
и полностью построен на правильных отступах, а при кодогенерации они сбиваются.

Для обхода проблемы предлагаю писать в шаблоне в начале строки специальные маркеры:
- `<` означает, что с этой строчки начинается новый блок кода, и надо увеличить отступ
- `>` означает, что блок кода закончился
- `|` означает, что это новая строчка с тем же отступом

Пример того, что можно написать:
```
| if something:
    < neurogen.train(
      < param1,
      | param2,
      {% if foo %}
        | param3,
      {% endif %}
      | )
> else:
    < something.
      that.
      {% if we_like_future %}
        will.
        generate.
      {% else %}
        generates.
      {% endif %}
      one.
      line()
    >
| print('done')
```

Во что это можно превратить:
- валидация приходящих данных, выдача осмысленных ошибок
- упрощение следующих шагов кодогенерации (например можно
  прикрутить к нагенеренным объектам вспомогательных методов)
- документирование основных объектов, на базе которых работает
  кодеген

Пример, того, как оно может быть:
```py
init = Initializer({'type': 'Constant', 'params': {'value': 42}})
init.render() # -> keras.initializers.Constant(value=42)

Initializer({'type': 'Ololo'})
# -> Exception: Ololo is not valid initializer
```

Генерящийся сейчас код можно использовать для парсинга на следующем этапе кодегена:
спаршенная в питонячий объект Model входная модель будет подаваться jinja-шаблону,
который уже будет генерировать год ввода-вывода, слои, обучение модели и так далее.

Стоит обдумать и вариант, что конкретно этот шаг кодегена не очень-то и нужен, и
можно напрямую подавать распаршенный JSON кодегену, который будет делать питонячий
файл с нейронкой.

Еще пример кодогенерации на jinja можно глянуть тут: https://github.com/lnunno/jinja-codegen
