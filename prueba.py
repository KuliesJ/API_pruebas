import requests

BASE = "http://127.0.0.1:5000/"

entrada_datos_nombre = str(input("Nombre de usuario: "))
entrada_datos_edad = str(input("Edad de usuario: "))

res = BASE + "usuario_info/" + entrada_datos_nombre + "/" +entrada_datos_edad
print(res)

response = requests.get(BASE + "usuario_info/Kulies/18")

print(response.json())

response = requests.get(res)

print(response.json())
