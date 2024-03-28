"""
import math

def raizcuadrada(numero):
	return math.sqrt(numero)



print(f" el resultado es {raizcuadrada(float(input("ingrese un numero: ")))
"""
"""
def resta(a=None,b=None):
	if a == None or b == None:
		return print("error, debes ingresar dos numeros")

	else:
		return a-b

print(resta())
"""

def suma(*args):
	su = 0

	for i in args:
		su+=i

	return su

print(suma(1,2,3))