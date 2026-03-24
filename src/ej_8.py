

def cifrado_cesar():
    msj = input("Ingrese un mensaje: ")
    offset = int(input("Ingrese un desplazamiento: "))

    cifrado = ""

    for letra in msj:
        output = ord(letra) + offset
        cifrado += chr(output)


    print(cifrado)

    desifrado = ""

    for letra in cifrado:
        output = ord(letra) - offset
        desifrado += chr(output)

    print(desifrado)

cifrado_cesar()