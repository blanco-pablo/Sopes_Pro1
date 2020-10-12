# python -m pip install --upgrade pip
# pip install -U nltk
# pip install requests

import nltk.data 
import nltk.tokenize 
import random
import requests

nltk.download('punkt')
data = {}
data['clients'] = []
listaNombres = ['Pedro','Raul','Emilio','Pepe','Julio','Marco']

def menu():
	print ("-------------Selecciona una opción--------------")
	print ("\t1 - Ingresar Ruta Archivo")
	print ("\t2 - Ingresar Direccion Balanceador")
	print ("\t3 - Ver Datos Cagados ")
	print ("\t4 - Enviar datos")
	print ("\t5 - Salir")
	print ("-------------------------------------------------")

while True:
	ruta = 'documento.txt'
	balanceador = 'http://104.198.56.138/imp'
	#balanceador = 'http://localhost:8080/imp'
	lista = {}
	menu()
	opcionMenu = input("inserta un numero valor >> ")
	if opcionMenu=="1":
		ruta = input("Ingrese la ruta >> ")

	elif opcionMenu=="2":
		balanceador = input("Ingrese la Direccion >> ")
		
	elif opcionMenu=="3":
		f = open(ruta) 
		doc = f.read() 
		token = nltk.sent_tokenize(doc) 
		for oracion in token: 
			data['clients'].append({ 
				'Nombre': random.choice(listaNombres),
				"Oracion":oracion
			})
		print("\n")
		print("Canitdad de Oraciones: "+str(len(data)))
		print(*data['clients'], sep = "\n") 
		print("\n")

	elif opcionMenu=="4":
		for clave in data['clients']:
			response = requests.post(balanceador, data = clave)
			if response.text == 'OK': 
				print("DATO ENVIADO")
			else:
				print("ERROR en ENVIO")
					

	elif opcionMenu=="5":
		break
	else:
		print ("Seleccionar opcion valida")
