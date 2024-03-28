""" 
esta es una prueba de los distintos operadores en python
tanto operadores aritmeticos como booleanos entre otros
porfavot sientese a gusto con el código
gracias :)
"""

#ingreso de valores colocados por el usuario, se coloca float al inicio para especificar que es un float 
numero1 = float(input("porfavor ingrese el numero 1: "))
numero2 = float(input("porfavor ingrese el numero 2: "))

#operaciones aritméticas, el :.2f se usa para especificar un maximo de 2 decimales

print(f"la suma es {numero1+numero2:.2f}")
print(f"la resta es {numero1-numero2:.2f}")
print(f"la multiplicacion es {numero1*numero2:.2f}")
print(f"la division es {numero1/numero2:.2f}")
print(f"el modulo es {numero1%numero2:.2f}")

a = True
b = False
print(a and b)
print(a or b)
print(not a)
print(not b)