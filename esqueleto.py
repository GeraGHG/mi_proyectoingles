import time
import os
import pandas as pd
import numpy as np

pausa = lambda x: time.sleep(x)

def limpieza():
    os.system('cls')

def enter():
    return input("Presione \"enter\" para continuar")

def pronouns():
    pronouns = np.array([["I am", "I'm"], ["You are", "You're"], ["He is", "He's"], ["She is", "She's"], ["It is", "It's"], ["We are", "We're"], ["They are", "They're"]])
    tabla_pronouns = pd.DataFrame(pronouns, index=range(1, 8), columns=["Pronoums/Verb to be", "Contraction"])
    print(tabla_pronouns)

def lista_palabras():
    return {"mom": "mamá", "friend": "amigo/amiga", "friends": "amigos/amigas", "sister": "hermana", "brother": "hermano"}


def ejercicios_1():
    return ["Ella es mamá", "Él es papá", "Amigos", "Hermana", "Hermano"]
def respuestas_1():
    return [["She's mom", "she's mom", "She is mom", "she is mom"], ["He's dad", "he's dad", "He is dad", "he is dad"], ["Friends", "friends"], ["Sister", "sister"], ["Brother", "brother"]]

def lista_palabras2():
    return {"walk": "caminar", "talk": "hablar", "eat": "comer", "dance": "bailar"}

def ejercicios_2():
    return ["Marco está hablando", "Ella está hablando", "Eso está bailando", "Marta está caminando"]
def respuestas_2():
    return [["Marco is talking", "marco is talking"], ["She's talking", "she is talking", "she's talking", "She is talking"], ["It's dancing", "it is dancing"], ["Marta is walking", "marta is walking"]]

def main():

    # limpieza()

    # print("******************************")
    # print("******** Ingles Básico *******")
    # print("******************************")

    # pausa(2)

    # print("Vamos a empezar...")

    # pausa(2)
    # limpieza()

    # print("Pronouns")
    # pronouns()  # mostrar tabla

    # pausa(2)

    # while True:
    #         opcion = input("Precione \"c\" para (continuar): ")
    #         if opcion.lower() == "c":  break

    # limpieza()

    # print("\nTiempo de vocabulario")
    # palabras = lista_palabras()
    # for ingles, español in palabras.items():
    #     print(f"- {ingles} -> {español}")
    
    # while True: 
    #     c = input("Presione \"c\" para continuar")
    #     if c.lower() == "c": break
    #     limpieza()

    # print("\nEjercicios\n")
    # lista_ejercicios = ejercicios_1()
    # correctas = respuestas_1()
    # print("Intrucciones: Traducir la oración o palabra al ingles (respetar las mayúsculas y minúsculas)\n")
    # for i in range(len(lista_ejercicios)):
    #     while True:
    #         print("Oración:", lista_ejercicios[i])
    #         respuesta = input("Respuesta (o escriba \"salir\" si desea finalizar): ")
    #         if respuesta.lower() == "salir":
    #             print("Ejercicio finalizado. ¡Hasta luego!")
    #             limpieza()
    #             break
    #         if respuesta in correctas[i]: 
    #             print("✔ Correcto") 
    #             pausa(1)
    #             limpieza()
    #             break
    #         else: print("Intentalo de nuevo recuerda usar bien las mayúsculas y minúsculas")
    # print("Bien hecho!\n")

    # NUEVA SECCIÓN
    enter() 
    time.sleep(1)
    print("\nPresent continuos\n")
    pronouns()
    print("\nTiempo de Vocabulario")
    palabras2 = lista_palabras2()
    for español, ingles in palabras2.items():
        print(f"{español} - {ingles}")
    
    print("\nVamos a practicar")
    ejercicios_aplicado_2 = ejercicios_2()
    resulados_2 = respuestas_2()

    for i in range(len(ejercicios_aplicado_2)):
        print("Sí desea salir (presione \"s\")")
        while True:
            print(ejercicios_aplicado_2[i])
            respuesta = input("Traducción: ")
            if respuesta == "s": 
                print("Saliendo del problema")
                time.sleep(2)
                break
            if respuesta in resulados_2[i]:
                print("✔ Correcto")
                time.sleep(2)
                break
            else:
                print("Intentalo de nuevo\n")



        
              
         

if __name__ == '__main__':
    main()


