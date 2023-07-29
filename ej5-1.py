"""
Cargar una lista de N componentes. Hallar e imprimir el promedio de los valores impares.
"""
componentes = []
componentes2 = []
N = int(input("Ingresa un numero de componentes: "))
for nro in range(0,N):
    n = int(input("Ingresa un numero: "))
    componentes.append(n)
    if n % 2 == 1 : # Es numero impar?
        componentes2.append(n)
print("Componentes:", componentes)
print("Promedio:", sum(componentes2)/len(componentes2))
#print("componentes:", componentes)
