def conversor(actual,dinero,final,peso,yuan,libra):

	if actual == "dolar":
		if final == "peso colombiano":
			print(f"Con {dinero} dolares puedes obtener {(dinero*peso):.2f} pesos colombianos \n")
		elif final == "yuan":
			print(f"Con {dinero} dolares puedes obtener {(dinero*yuan):.2f} yuanes \n")
		if final == "libra esterlina":
			print(f"Con {dinero} dolares puedes obtener {(dinero*libra):.2f} libras esterlinas \n")

	if actual == "euro":
		if final == "peso colombiano":
			print(f"Con {dinero} euros puedes obtener {(dinero*peso):.2f} pesos colombianos \n")
		elif final == "yuan":
			print(f"Con {dinero} euros puedes obtener {(dinero*yuan):.2f} yuanes \n")
		if final == "libra esterlina":
			print(f"Con {dinero} euros puedes obtener {(dinero*libra):.2f} libras esterlinas \n")
		

print("****** Bienvenido al sistema de conversion internacional (SCI) ****** \n")
sesion = "si"

while sesion == "si":
	moneda_actual = input("Indique aqui su moneda a convertir(dolar/euro): ")
	cantidad = float(input("¿Que cantidad desea convertir?: "))

	if moneda_actual == "dolar":
		moneda_final = input("¿A que moneda desea convertir sus dolares?(peso colombiano/yuanes/libra esterlina): ")
		validador = 1
	elif moneda_actual == "euro":
		moneda_final = input("¿A que moneda desea convertir sus euros?(peso colombiano/yuan/libra esterlina): ")
		validador = 1
	else: 
		print("moneda no valida")
		validador = 0
	if validador == 1:
		if moneda_final == "peso colombiano" or moneda_final == "yuan" or moneda_final == "libra esterlina":
			if moneda_actual == "dolar":
				conversor(moneda_actual, cantidad,moneda_final,3750,6.37,0.76)
			elif moneda_actual == "euro":
				conversor(moneda_actual, cantidad,moneda_final,4000,6.93,0.83)
		else: 
			print("la moneda solicitada a cambiar no se encuentra dentro del registro del sistema\n")

	i = 1
	while i == 1:
		sesion = input("Desea realizar otra conversion? (si/no): ")

		if sesion == "si" or sesion == "no":

			i = 0
		else: 
			print("entrada invalida")
		pass
	pass

print("\n Hasta pronto!!!")
