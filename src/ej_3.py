

def filtro_spoilers():
   
    review = """La película sigue a un grupo de astronautas que viajan a Marte
    en una misión de rescate. El capitán Torres lidera al equipo a través
    de tormentas solares y fallos en el sistema de navegación. Al llegar
    a Marte descubren que la base está abandonada y los suministros
    destruidos. Torres decide sacrificar la nave nodriza para salvar
    al equipo y logran volver a la Tierra en una cápsula de emergencia.
    El final revela que Torres sobrevivió gracias a un pasaje secreto."""

    
    lista_spoilers = []
    lista_spoilers = input('Ingrese las palabras spoilers separadas por coma: ').split(', ')


    lista_review = review.split()
        

    output = []

    for palabra in lista_review:
        palabra = palabra.strip('.')
        if palabra in lista_spoilers:
            c = 0
            for letra in palabra:
                c += 1
            palabra = "*" * c
            output.append(palabra)
        else:
            output.append(palabra)

    print(' '.join(output))


