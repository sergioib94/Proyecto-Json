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

def Filtrar(datos):
    pokemon = []
    huevos = []
    for info in datos["pokemon"]:
        if info["egg"] != "Not in Eggs":
            huevos.append(info["egg"])
            pokemon.append(info["name"])
    return zip (pokemon,huevos)

def Buscar(estadistica,base,datos):
    pokemon = []
    if estadistica == "HP":
        for info in datos["pokemon"]:
            if info["base"]["HP"] > base:
                pokemon.append(info["name"])

    elif estadistica == "Attack":
        for info in datos["pokemon"]:
            if info["base"]["Attack"] > base:
                pokemon.append(info["name"])

    elif estadistica == "Defense":
        for info in datos["pokemon"]:
            if info["base"]["Defense"] > base:
                pokemon.append(info["name"])

    elif estadistica == "Speed":
        for info in datos["pokemon"]:
            if info["base"]["Speed"] > base:
                pokemon.append(info["name"])
    return pokemon

def Combate(pokemon1,datos):
    tipo1 = []
    debilidad1 = []
    tipo2 = []
    debilidad2 = []

    for pokemon in datos["pokemon"]:
        if pokemon["name"] == pokemon1:
            tipo1.append(pokemon["type"])

    for pokemon2 in datos["pokemon"]:
        if pokemon2["name"] == pokemon2:
            tipo2.append(pokemon2["type"])

    return zip(tipo1,tipo2)