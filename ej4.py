"""
Cargar una lista con N numeros y 
luego hallar el promedio de los elementos en él que no sean cero.
"""
N = int(input("Ingrese la cantidad de numeros para el listado: "))
listado = []
for x in range(N):
    nro = int(input("Ingrese un numero: "))
    listado.append(nro)
print("Hemos cargado:", listado)

""" contador = 0
suma = 0
for numero in listado:
    if(numero != 0):
        contador=contador+1
        suma = suma + numero
print("El promedio de ",suma,"/",contador, "es: ", suma/contador) """
""" no_ceros = []
for numero in listado:
    if numero != 0:
        no_ceros.append(numero)
        print("listado actual:", no_ceros)
print("*El promedio de ",sum(no_ceros),"/",len(no_ceros), "es: ", sum(no_ceros)/len(no_ceros)) """

# Con diccionarios:
sin_cero = {
    "suma": 0,
    "contador": 0
}
for numero in listado:
    if numero != 0:
        sin_cero["suma"] = sin_cero["suma"] + numero
        sin_cero["contador"] = sin_cero["contador"] + 1
print("El promedio de ",sin_cero["suma"],"/",sin_cero["contador"], "es: ", sin_cero["suma"]/sin_cero["contador"]) 






