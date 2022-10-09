""" Python marshal contain funtion that can read and write values in binary format"""

import marshal #python module for marshal

dictionary = {
    'Name': 'Bata',
    'Age': 10,
    'Weight': 20.0,
    'Motto' : 'Eate code and slwwp'

}


# serilizing using the dump method using the write-binary(wb)
with open('dictionary.marshal', 'wb') as dict_dump:
    marshal.dump(dictionary, dict_dump)
data = marshal.dumps(dictionary)

# deserialing using the loads  methos using read binary
with open('dictionary.marshal', 'rb') as dict_marsh:
    marshal.load(dict_marsh)
marsh = marshal.loads(dictionary)
     