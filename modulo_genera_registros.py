#modulo para generar los registros a travez de la entrada del usuario

acumulados = []

def suma_registro(): #calcula los montos  del registro y lo añade a la lista

    print ("ingrese los datos de la siguiente carta")
    print ()
    try:
        nombre, dolares, estado = input("nombre: "), float(input("valor en dolares: ")), input("estado: ")
        registro = [nombre.lower(), dolares, dolares*10, dolares*50, dolares*60, estado.lower()] 
        acumulados.append(registro)
    except:
        print ("valores ingresados no admisibles")
    print ()
    print ("hasta ahora han sido ingresadas " + str(len(acumulados)) + " cartas" )
    respuesta = input("desea ingresar otra carta? ")
    print ()

    if respuesta == "si":
        suma_registro()

def envia_registros(): #funcion que sera llamada por otros modulos
    suma_registro()
    registros = acumulados
    return registros

if __name__ == "__main__":
    print(envia_registros())