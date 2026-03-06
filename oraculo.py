import random
import datetime
import json
from colorama import Fore, Style, init

init()

archivo_json = "oraculo.json"

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


def limpiar(texto):
    texto = texto.replace("?", "")
    texto = texto.replace("¿", "")
    return texto


def respuesta_oraculo():
    respuestas = [
        "si",
        "no",
        "probablemente si",
        "yo digo que no"
    ]

    return random.choice(respuestas)


def dos_opciones(opcion1, opcion2):
    opciones = [opcion1, opcion2]
    return random.choice(opciones)


def ver_historial(historial):
    if not historial:
        print(Fore.GREEN + "Aun no hay historial")
    else:
        print(Fore.GREEN + "\n--- HISTORIAL ---")
        for elemento in historial:
            print(Fore.GREEN + elemento)


def mostrar_fecha_hora():
    fecha_hora_actual = datetime.datetime.now()
    print(Fore.GREEN + f"Fecha y hora actual: {fecha_hora_actual}")


def adivinar_ultima():
    if not el_historial:
        print(Fore.GREEN + "RAMIREZ dice: no hay historial aun...")
    else:
        ultima = el_historial[-1]
        print(Fore.GREEN + "RAMIREZ intenta recordar...")
        print(Fore.GREEN + f"Creo que lo ultimo fue: {ultima}")


def logo():
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


def menu():
    while True:

        print(Fore.GREEN + "\n---Menu---")
        print(Fore.GREEN + "1. Hacer una pregunta al ramirez")
        print(Fore.GREEN + "2. Elegir entre dos opciones")
        print(Fore.GREEN + "3. Ver historial")
        print(Fore.GREEN + "4. Ver fecha y hora")
        print(Fore.GREEN + "5. Adivinar ultima accion")
        print(Fore.GREEN + "6. Salir")

        try:
            opcion = int(input(Fore.GREEN + "Elige una opcion(1-6): "))
        except ValueError:
            print(Fore.GREEN + "Escribe un numero")
            continue
        
        if opcion == 1:
            pregunta = input(Fore.GREEN + "Haz tu pregunta: ")
            pregunta_limpia = limpiar(pregunta)

            respuesta = respuesta_oraculo()

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
        
        elif opcion == 3:
            ver_historial(el_historial)
        
        elif opcion == 4:
            mostrar_fecha_hora()
        
        elif opcion == 5:
            adivinar_ultima()
        
        elif opcion == 6:
            print(Fore.GREEN + "Ramirez se va...")
            break

        else:
            print(Fore.GREEN + "Opcion no valida")


logo()
menu()