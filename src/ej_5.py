def calcular_costo_envio():

    peso = float(input("Ingrese el peso del paquete (kg): "))
    zona = input("Ingrese la zona del paquete: ")


    if zona.lower() != "local" and zona.lower() != "regional" and zona.lower() != "nacional":
        print("Zona invalida (local, regonal, nacional)")
    
    if zona.lower() == "local":
        if peso < 1:
            costo = 500
        elif peso >= 1 and peso < 5:
            costo = 1000
        elif peso >= 5:
            costo = 2000
    elif zona.lower() == "regional":
        if peso < 1:
            costo = 1000
        elif peso >= 1 and peso < 5:
            costo = 2500
        elif peso >= 5:
            costo = 5000
    elif zona.lower() == "nacional":
        if peso < 1:
            costo = 2000
        elif peso >= 1 and peso < 5:
            costo = 4500
        elif peso >= 5:
            costo = 8000

    print(f"Costo de envio {costo}")


calcular_costo_envio()
