import string

def validar_email():

    email = input("ingrese un email para validar: ")
    contiene_arroba = email.count("@") == 1

    tiene_char_antes = len(email.split("@")[0]) > 0

    tiene_punto_despues = email.split("@")[1].count(".") == 1
    

    no_empieza_con = not email.startswith("@") and not email.startswith(".")

    dos_char_despues = True if "." in email and len(email.split(".")[1]) >= 2 else False


    if contiene_arroba and tiene_char_antes and tiene_punto_despues and no_empieza_con and dos_char_despues:
        print("Email valido")
    else:
        print("Email invalido")







validar_email()
