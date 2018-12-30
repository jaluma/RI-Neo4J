from __future__ import print_function

import json
import pprint
import sys
import os

import util
import db
import queries

def main():
    menu_principal()

def menu_principal():
    while True:
        print("--- Neo4J ---")
        print(" 1 - Consultas elemental")
        print(" 2 - Consultas intermedias")
        print(" 3 - Consultas avanzadas")
        print(" 4 - Salir")
        print("Escoja una opcion (1-4):")

        opcionMenu = raw_input("Inserta un numero >> ")
        print()
        if opcionMenu == "1":   
            menu_consultas_elementales()
        elif opcionMenu == "2":
            menu_consultas_intermedias()
        elif opcionMenu == "3":
            menu_consultas_avanzadas()
        elif opcionMenu == "4":
            return;
        else:
            print("Opcion incorrecta")

def menu_consultas_elementales():
    while True:
        print("--- Consultas elementales ---")
        print(" 1 - Consultas 1")
        print(" 2 - Consultas 2")
        print(" 3 - Volver")
        print("Escoja una opcion (1-3):")

        opcionMenu = raw_input("Inserta un numero >> ")
        print()
        if opcionMenu == "1":   
            consulta_elemental_1()
        elif opcionMenu == "2":
            consulta_elemental_2()
        elif opcionMenu == "3":
            return
        else:
            print("Opcion incorrecta")

def menu_consultas_intermedias():
    while True:
        print("--- Consultas intermedias ---")
        print(" 1 - Consultas 1")
        print(" 2 - Consultas 2")
        print(" 3 - Volver")
        print("Escoja una opcion (1-3):")

        opcionMenu = raw_input("Inserta un numero >> ")
        print()
        if opcionMenu == "1":   
            consulta_intermedias_1()
        elif opcionMenu == "2":
            consulta_intermedias_2()
        elif opcionMenu == "3":
            return
        else:
            print("Opcion incorrecta")

def menu_consultas_avanzadas():
    while True:
        print("--- Consultas avanzadas ---")
        print(" 1 - Consultas 1")
        print(" 2 - Consultas 2")
        print(" 3 - Volver")
        print("Escoja una opcion (1-3):")

        opcionMenu = raw_input("Inserta un numero >> ")
        print()
        if opcionMenu == "1":   
            consulta_avanzadas_1()
        elif opcionMenu == "2":
            consulta_avanzadas_2()
        elif opcionMenu == "3":
            return
        else:
            print("Opcion incorrecta")

def consulta_elemental_1():
    print_info_consultas("Edad del concursante mayor")

    print_results(db.db_manager().query(queries.get_concursante_con_mayor_edad))

def consulta_elemental_2():
    print_info_consultas("Concursantes alemanes con toda la informacion de cada uno")
    
    print_results(db.db_manager().query(queries.get_concursantes_alemanes))

def consulta_intermedias_1():
    print_info_consultas("Fecha de la gala en la que fue expulsado el concursante Dave Zulueta")
    
    print_results(db.db_manager().query(queries.get_fecha_expulsion_dave))

def consulta_intermedias_2():
    print_info_consultas("Concursantes que colaboran con otros participantes tantas veces como el concursante con mas colaboraciones")
    
    print_results(db.db_manager().query(queries.get_concursantes_mas_colaboraciones))

def consulta_avanzadas_1():
    print_info_consultas("---")
    pass

def consulta_avanzadas_2():
    print_info_consultas("---")
    pass

def print_info_consultas(str):
    print("--------------------")
    print(str)
    print("--------------------")
    print()

def print_results(str):
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(str)
    print()

# script
if __name__ == '__main__':
    main()
