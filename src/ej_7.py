from collections import Counter

import random

def amigo_invisible():

    amigos = input("Ingrese una lista de nombres separados por coma: ")

    lista_amigos = amigos.split(", ")

    output = []
    for amigo in lista_amigos:
        output.append(amigo.strip(" "))


    counter = Counter(output)

    input_valido = True

    for item in counter:
        if counter[item] > 1:
            print("Ingreso un nombre mas de una vez")
            input_valido = False
    if len(output) < 3:
        print("Ingrese al menos 3 nombres")
        input_valido = False


    if input_valido:




        shuffle = output[:]
        random.shuffle(shuffle)



        valido = False

        while not valido:
            random.shuffle(shuffle)

            valido = True
            for i in range(len(output)):

                if shuffle[i] == output[i]:
                    valido = False
                    break







        for i in range(len(output)):
            print(f"{output[i]} -> {shuffle[i]}")



amigo_invisible()