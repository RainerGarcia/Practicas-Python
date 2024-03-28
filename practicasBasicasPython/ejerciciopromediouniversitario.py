nombre = input("Buenos dias estudiando, porfavor indique su nombre y apellido: ")
semestre = int(input("Numero de semestre culminado: "))
agregar_otro = 1
num_materia = 0
lista_materia = []
lista_nota = []
nota_final = 0 

while agregar_otro == 1:

	lista_materia.append( input(f"Coloque aqui el nombre de su materia numero {num_materia+1}: "))
	lista_nota.append(float(input("Coloque aqui su calificacion de la materia: ")))

	validador = input("Tiene alguna otra materia que agregar? (si/no): ")

	if validador == "no":
		agregar_otro = 0
		print("\n")
	else:
		num_materia += 1
		print("\n")

print("\n Nombre del estudiante: " + nombre)
print(f"{semestre}° semestre")
print("################################################")
for i in range(num_materia+1):
	print(f"materia: {lista_materia[i]}, nota: {lista_nota[i]}")
	nota_final += lista_nota[i]
print("################################################")
print(f"\n Promedio acumulado: {nota_final/(num_materia+1)}")


