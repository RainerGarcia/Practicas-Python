import os

agenda = {
	"Jose": 302944,
	"Mario": 829455,
	"Angel": 829405,
	"Luis": 930594
}

opcion = 0
sesion = "si"
nombre = "nombre"
resultado = "resultado"

while sesion == "si":
	print("******* Agenda Telefonica *******")
	print("OPCION 1, Consulta de contacto")
	print("OPCION 2, Añadir un nuevo contacto")
	print("OPCION 3, Modificar un contacto")
	print("OPCION 4, Eliminar un contacto")
	print("OPCION 5, Salir de la agenda")
	opcion = int(input("opcion: "))
	os.system("cls")

	if opcion == 1:
		nombre = input("Escriba el nombre del contacto a consultar: ")
		resultado = agenda.get(nombre,"No se encuentra agendado")
		print(f" {nombre}, numero del contacto {resultado}\n\n")
		os.system("pause")
		os.system("cls")

	elif opcion == 2:
		nombre = input("Escriba el nombre del nuevo contacto: ")

		if nombre in agenda:
			print("El contacto ya existe en tu agenda\n\n")
			os.system("pause")
			os.system("cls")
		else:
			agenda[nombre] = int(input("Ingrese el numero de telefono: "))

			print("Contacto agregado con exito!\n\n")

			os.system("pause")
			os.system("cls")

	elif opcion == 3:
		nombre = input("Ingrese el nombre del contacto: ")

		if nombre in agenda:
			agenda[nombre] = int(input(f"Ingrese el nuevo numero telefonico de {nombre}: "))
			print(f"El numero de {nombre} fue modificado con exito! \n\n")
			os.system("pause")
			os.system("cls")

		else:
			print("El contanto no se encuentra agendado\n\n")
			os.system("pause")
			os.system("cls")

	elif opcion == 4:

		nombre = input("Ingrese el nombre del contacto: ")
			
		if nombre not in agenda:
			print("El contacto no se encuentra agendado!\n\n")
			print(agenda)
			os.system("pause")
			os.system("cls")

		else:
			del agenda[nombre]
			print("Contacto eliminado con exito!\n\n")
			print(agenda)
			os.system("pause")
			os.system("cls")

	elif opcion == 5:
		sesion = 0

		print("Cerrando sesion, hasta luego!\n\n")

	else:
		print("OPCION INCORRECTA\n\n")
		os.system("pause")
		os.system("cls")



pass


