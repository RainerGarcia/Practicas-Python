"""
Programa descuentos en python
"""

#variables a utilizar y datos suministrados por el usuario
cliente = input("Ingrese su nombre y apellido: ")
compra = int(input("ingrese el monto de su compra($): "))
descuento = 0

if compra > 0 and compra < 500:
	
	if compra < 500 and compra > 300:
		descuento = 20
	
	elif compra <= 300 and compra >= 150:
		descuento = 15

	elif compra < 150 and compra >= 80:
		descuento = 10

	else:
		print("")

elif compra > 500:
	print("su compra excede a los montos permitidos por la promocion\n")

else:
	print("usted no ha comprado nada \n")

if compra > 0:
	print("Nombre del Cliente: " + cliente + "\n")
	print(f"monto de la compra: {compra}$")
	print(f"descuento: {descuento}%")
	print(f"total a pagar: {compra-(compra*(descuento/100)):.0f}$")