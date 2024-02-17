import json

archivo_json = 'datos.json'
with open(archivo_json, 'r') as f:
        contenido = json.load(f)
    
for caracter in json.dumps(contenido):
    print(caracter)
