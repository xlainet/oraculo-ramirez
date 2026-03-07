# Oráculo Ramírez
# Programa de consola en Python que simula un oráculo interactivo.
# Permite hacer preguntas, elegir entre dos opciones, ver historial,
# ver fecha y hora actual y recordar la última pregunta u opción.
# Autor: xlainet

import random
import datetime
import json
from colorama import Fore, Style, init

init()

archivo_json = "oraculo.json" #creamos el archivo oraculo.json

try:                                                        
    with open(archivo_json, "r") as archivo:
        el_historial = json.load(archivo)
except:
    el_historial = []
    with open(archivo_json, "w") as archivo:
        json.dump(el_historial, archivo, indent=4)


def guardar_historial():
    with open(archivo_json, "w") as archivo:
        json.dump(el_historial, archivo, indent=4)


def limpiar(texto): #funcion para eliminar los signos de pregunta
    texto = texto.replace("?", "")
    texto = texto.replace("¿", "")
    return texto


def respuesta_oraculo(): #funcion para las respuestas que dara el oraculo
    respuestas = [
        "si",
        "no",
        "probablemente si",
        "yo digo que no",
        "Le pregunte a mis huevos y me dijieron simon",
        "Depende"
        "Quien sabe",
        "Solo mi creador/a podria responder eso"
    ]

    return random.choice(respuestas)


def dos_opciones(opcion1, opcion2): #funcion para las dos opciones que eligira aleatoriamente el oraculo
    opciones = [opcion1, opcion2]
    return random.choice(opciones)


def ver_historial(historial): #funcion para ver el historial
    if not historial:
        print(Fore.GREEN + "Aun no hay historial")
    else:
        print(Fore.GREEN + "\n--- HISTORIAL ---")
        for elemento in historial:
            print(Fore.GREEN + elemento)


def mostrar_fecha_hora(): #funcion para mostrar fecha y hora actual
    fecha_hora_actual = datetime.datetime.now()
    print(Fore.GREEN + f"Fecha y hora actual: {fecha_hora_actual}")


def adivinar_ultima(): #funcion para saber lo ultimo que hizo el usuario
    if not el_historial:
        print(Fore.GREEN + "RAMIREZ dice: no hay historial aun...")
    else:
        ultima = el_historial[-1]
        print(Fore.GREEN + "RAMIREZ intenta recordar...")
        print(Fore.GREEN + f"Creo que lo ultimo fue: {ultima}")


def logo(): #funcion del logo ramirez
    print(Fore.GREEN + """
██████╗  █████╗ ███╗   ███╗██╗██████╗ ███████╗███████╗
██╔══██╗██╔══██╗████╗ ████║██║██╔══██╗██╔════╝╚══███╔╝
██████╔╝███████║██╔████╔██║██║██████╔╝█████╗    ███╔╝ 
██╔══██╗██╔══██║██║╚██╔╝██║██║██╔══██╗██╔══╝   ███╔╝  
██║  ██║██║  ██║██║ ╚═╝ ██║██║██║  ██║███████╗███████╗
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝╚═╝  ╚═╝╚══════╝╚══════╝

        ORACULO RAMIREZ
        creador: xlainet
""")


def menu(): #funcion para mostrar el menu con sus opcioens del 1-6
    while True:

        print(Fore.GREEN + "\n---Menu---")
        print(Fore.GREEN + "1. Hacer una pregunta al ramirez")
        print(Fore.GREEN + "2. Elegir entre dos opciones")
        print(Fore.GREEN + "3. Ver historial")
        print(Fore.GREEN + "4. Ver fecha y hora")
        print(Fore.GREEN + "5. Adivinar ultima accion")
        print(Fore.GREEN + "6. Salir")

        try: #prevenimos que alguien escriba una palabra en vez de un numero
            opcion = int(input(Fore.GREEN + "Elige una opcion(1-6): "))
        except ValueError:
            print(Fore.GREEN + "Escribe un numero")
            continue 
        
        if opcion == 1:
            pregunta = input(Fore.GREEN + "Haz tu pregunta: ")
            pregunta_limpia = limpiar(pregunta)
            respuesta = respuesta_oraculo()
            # Hacer pregunta al oraculo

            print(Fore.GREEN + f"Pregunta: {pregunta_limpia}")
            print(Fore.GREEN + f"Respuesta: {respuesta}")

            registro = f"Pregunta: {pregunta_limpia} - Respuesta: {respuesta}"
            el_historial.append(registro)

            guardar_historial()

        elif opcion == 2:
            op1 = input(Fore.GREEN + "Ingresa la primera opcion: ")
            op2 = input(Fore.GREEN + "Ingresa la segunda opcion: ")

            decision = dos_opciones(op1, op2)

            print(Fore.GREEN + f"La decision es: {decision}")

            registro = f"Opcion elegida entre: {op1} / {op2} -> {decision}"
            el_historial.append(registro)

            guardar_historial()
            # El oraculo eligira entre las dos opciones que le proporciones de forma aleatoria
        
        elif opcion == 3:
            ver_historial(el_historial)
            #Ver el historial
        
        elif opcion == 4:
            mostrar_fecha_hora()
            #Mostrar fecha y hora actual
        
        elif opcion == 5:
            adivinar_ultima()
            #Adivinar lo ultimo que hizo el usuario
        
        elif opcion == 6:
            print(Fore.GREEN + "Ramirez se va...")
            break
        #Termina el programa

        else:
            print(Fore.GREEN + "Opcion no valida")
            #Caso hipotetico donde ninguna opcion es invalida o no responde como quieras

logo()
menu()