persona = {
    "nombre": "Jose",
    "apellido": "Aquino",
    "sexo": "Masculino",
    "edad": 25,
    "hermanos": [],
    "licenciado": False
}

for clave in persona:
    if type(persona[clave]) is list:
        for hermano in persona[clave]:
            print("Hermano/a:", hermano)
    else:
        if(clave == "licenciado" and persona[clave] == True):
            print("Se encuentra licenciado para dar una clase")
        else:
            print("Clave", clave, "valor:", persona[clave])
