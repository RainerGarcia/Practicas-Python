#indice de masa corpolar by rainer 

sesion = input("desea iniciar el programa de indice de masa corporal? (si/no)")

if sesion == "si":
	print("**** bienvenido al sistema del indice de masa corporal **** \n")
	while  sesion == "si":

		sexo = input("indique si usted es masculino o femenino: ")
		edad = int(input("indique aqui su edad: "))
		estatura = float(input("ingrese el numero de su estatura en mts: "))
		masa = float(input("ingrese el numero de su peso en kg: "))
		IMC = round(masa/(estatura ** 2),1)

		if IMC < 18.5:
			print(f" IMC {IMC}, usted tiene esta bajo de peso")

		elif IMC > 18.5 and IMC < 24.5:
			print(f" IMC {IMC}, usted tiene un peso normal")

		elif IMC > 25 and IMC < 30:
			print(f" IMC {IMC}, usted tiene sobrepeso")

		elif IMC > 30 and IMC < 35:
			print(f" IMC {IMC}, usted tiene obesidad tipo I, leve")

		elif IMC > 35 and IMC < 40:
			print(f" IMC {IMC}, usted tiene obesidad tipo II, media")

		elif IMC > 40:
			print(f" IMC {IMC}, usted tiene obesidad tipo III, grave")

		print("usted debe consumir diariamente:")
		if sexo == "masculino":
			print(f"{((10*masa)+(6.25*(estatura*100))-(5*edad))+5} calorias")
			print("30 a 38 gramos de fibra")
		else:
			print(f"{((10*masa)+(6.25*(estatura*100))-(5*edad))-161} calorias")
			print("30 a 38 gramos de fibra")

		print(f"{2*masa} gramos de proteina")
		print(f"{5*masa} gramos de carbohidratos")
	
		sesion = input("desea realizar otro calculo de IMC? (si/no)")	
		pass

print("hasta pronto!!!")

