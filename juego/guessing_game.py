import random
import os

contador = 0
partida = 0
mejor_partida = 0
media_partidas = 0
globalcontador = 0
mejorpartida = 10000
numero1 = random.randint(1,101)
end = False
def banner():
    print("Estic pensant en un numero del 1 al 100")

def adivina():
    numero = int(input("Prueba un numero: "))
    random_numer(numero)

def random_n():
    global numero1
    random.seed(numero1)
    numero_correcto = (random.randint(1,101))
    return numero_correcto

def random_numer(intento):
    numero_correcto = random_n()
    global contador, globalcontador
    if intento == numero_correcto:
        global mejorpartida
        contador += 1
        globalcontador += contador
        if contador < mejorpartida:
            mejorpartida = contador
        print(f"Perfecto lo has adivinado {numero_correcto}, has hecho {contador} intentos")
    elif intento > numero_correcto:
        print("El numero es menor")
        contador += 1
        adivina()
    elif intento < numero_correcto:
        print("El numero es mayor")
        contador += 1
        adivina()
    else:
        print("Algo fallo")


def juego():
    global end, numero1, contador, partida, globalcontador,mejorpartida
    
    while end != True:
        numero1 = random.randint(1,101)
        contador = 0
        partida += 1


        adivina()
        print("Quieres jugar de nuevo?")
        opinion = input("")
        os.system("cls")
        if "yes" not in opinion.lower() or "y" not in opinion.lower():
            print(f"Has jugado un total de {partida} partida")
            print(f"Total de intentos {globalcontador} intentos")
            total = globalcontador / partida
            print(f"Media total de intentos con partidas: {round(total,1)}")
            print(f"Mejor partida: {mejorpartida}")
            
            end = True      
        else:
            contador += 1