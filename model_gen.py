import json

string_to_write = "import keras\n"
string_to_write += "    model = Sequential()\n"

with open("model.json", "r") as read_file:
    data = json.load(read_file)
    
layer = data['layers']
for i in range(len(layer)):
    type = layer[i]['type']
    if (type == 'Dense'):
        params = layer[i]['params']
        string_to_write += "    model.add({}(".format(type)
        for key, value in params.items():
            string_to_write += "{}={},".format(key, value)
        string_to_write += "))"
        string_to_write = string_to_write.replace(",))", "))")

print (string_to_write)
