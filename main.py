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
	print ("------------1-Selecciona una opción--------------")
	print ("\t1 - Ingresar Ruta")
	print ("\t2 - Ingresar Direccion")
	print ("\t3 - Ver Datos")
	print ("\t4 - Enviar datos")
	print ("\t5 - salir")
	print ("-------------------------------------------------")

while True:
	ruta = 'documento.txt'
	balanceador = 'http://104.198.56.138/'
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
			response = requests.post('http://pythonscraping.com/pages/processing.php', data = clave)
			print("Envio Dato")
			print(response)

	elif opcionMenu=="5":
		break
	else:
		print ("Seleccionar opcion valida")
