import os

"""
		os.system("pause")
		os.system("cls")
"""

class persona():
	def __init__(self,nombre,edad):
		self.nombre = nombre
		self.edad = edad

	def imprimir(self):

		print(f"nombre: {self.nombre}")
		print(f"edad: {self.edad}")

class ciudadano(persona):

	def __init__(self,nombre,edad,deposito):

		super().__init__(nombre,edad)
		self.deposito = deposito

	def imprimirlo(self):
		super().imprimir()
		print(f"deposito: {self.deposito}$")

	def impuesto(self):

		if self.deposito > 4000:
			print("Usted debe pagar impuestos")
		else:
			print("Usted no debe pagar impuestos")


#________main__________

i = "si"
nombre1 = ""
edad1 = 0
deposito1 = 0

while i == "si":

	print("**** Bienvenido al sistema del banco central del pais ****")
	print("Registrese para poder anexarlo al sistema bancario")
	os.system("pause")
	os.system("cls")

	nombre1 = input("Porfavor ingrese aqui su nombre y apellido: ")
	os.system("cls")
	edad1 = int(input("Porfavor indiquenos su edad: "))
	os.system("cls")
	deposito1 = int(input("Ahora ingrese el monto de su deposito en $: "))
	os.system("cls")

	#instancias
	ciudadano1 = ciudadano(nombre1,edad1,deposito1)

	ciudadano1.imprimirlo()
	ciudadano1.impuesto()
	os.system("pause")
	os.system("cls")

	i = input("Desea realizar otro registro?(si/no): ")
		
	if i == "no":
		print("Hasta luego!!!")
	else:
		os.system("cls")

	pass
