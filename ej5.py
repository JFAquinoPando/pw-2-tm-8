"""
Cargar una lista de N componentes. Hallar e imprimir el promedio de los valores impares.
"""
componentes = []
N = int(input("Ingresa un numero de componentes: "))
for nro in range(0,N):
    n = int(input("Ingresa un numero: "))
    componentes.append(n)
print("componentes:", componentes)

contador = 0
suma = 0
for componente in componentes:
    if componente % 2 == 1: # Pregunto si el numero es impar!
        suma = suma + componente
        contador = contador + 1
print("El promedio es:", suma/contador)

