import json

def Lista(datos):
    num = []
    pokedex = []
    for id in datos["pokemon"]:
        num.append(id["id"])

    for info in datos["pokemon"]:
        pokedex.append(info["name"])
    return zip(num,pokedex)

def Contar(tipo,datos):
    pokedex = []
    for info in datos["pokemon"]:
        if tipo in info["type"]:
            pokedex.append(info["name"])
    return len(pokedex)

with open("pokedex.json") as fichero:
    datos = json.load(fichero)

while True:
    print ("")
    print ("Menu Principal:")
    print ("")
    print ("1.Listar Informacion: Mostrar los pokemons que hay.")
    print ("2.Contar informacion: Contar pokemons que hay de un tipo especifico.")
    print ("3.Buscar o Filtrar informacion: Buscar los pokemons que pueden salir de un huevo.")
    print ("4.Buscar informacion relacionada: Meter por teclado una caracteristica de un pokemon y decir que pokemons superan esa estadistica.")
    print ("5.Ejercicio Libre: Proponer un combate, pedir por teclado el nombre de dos pokemons y decir quien ganaria.")
    print ("0.Salir")
    print ("")

    opcion = input("opcion: ")
    print ("")

    if opcion == "1":
        for datos in Lista(datos):
            print (datos[0],"-",datos[1])
    
    if opcion == "2":
        tipo = input("Introduce un tipo de pokemon: " )

        print (Contar(tipo,datos))

    if opcion == "0":
        break;