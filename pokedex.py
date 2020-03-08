from func_pokedex import *

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
    print ("6.Ayuda (listado de tipos)")
    print ("0.Salir")
    print ("")

    opcion = input("opcion: ")
    print ("")

    if opcion == "1":
        print ("Listados de pokemons: ")
        print ("")
        for pokemon in Lista(datos):
            print (pokemon[0],"-",pokemon[1])
    
    if opcion == "2":
        tipo = input("Introduce un tipo de pokemon: " )

        print (Contar(tipo,datos))

    if opcion == "3":
        print ("Los siquientes pokemons nacen de huevo:")
        print ("")
        for huevo in Filtrar(datos):
            print ("*",huevo[0],"-",huevo[1])

    if opcion == "4":
        estadistica = input("Introduce la estadistica que quieras comprobar: ")
        base = int(input("Introduce el valor de la estadistica: "))

        for estadistica in Buscar(estadistica,base,datos):
            print (estadistica)
    
    if opcion == "5":
        pokemon1 = input("Introduce el nombre de tu pokemon: ")
        pokemon2 = input("Introduce el nombre del pokemon rival: ")

        for i in Combate(pokemon1,pokemon2,datos):
            for j in i:
                print (j)

    if opcion == "6":
        print ("Tipos de pokemon:")
        print ("")
        print ("Water,Fire,Ice,Flying,Psychic,Poison,Grass,Ground,Rock,Electric,Bug,Normal,Fighting,Fairy,Dark,Ghost")

    if opcion == "0":
        break;