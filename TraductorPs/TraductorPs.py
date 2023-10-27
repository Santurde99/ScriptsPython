import pyphen

#Parte del codigo que encripta
def separar_silabas_encriptar(palabra):
    vocales="aeiouáéíóúü"
    diccionario = pyphen.Pyphen(lang='es_ES')
    palabraSeparada = diccionario.inserted(palabra)
    vocalActual="a"
    palabraresultado = ""
    for i in palabraSeparada:
        if (i in vocales):
            vocalActual = i
            palabraresultado += i
        elif (i == "-"):
            palabraresultado += "p"+vocalActual
        else:
            palabraresultado += i
    palabraresultado += "p" + vocalActual
    return palabraresultado 

def separar_palabras_encriptar(frase):
    palabraActual = ""
    fraseResultado = ""
    for o in frase:
        if (o == " "):
            fraseResultado += separar_silabas_encriptar(palabraActual)
            fraseResultado += " "
            palabraActual = ""
        else:
            palabraActual += o
    fraseResultado += separar_silabas_encriptar(palabraActual)
    return fraseResultado

#parte del codigo que desencripta
def separar_palabras_desencriptar(frase):
    palabraActual = ""
    fraseResultado = ""
    for o in frase:
        if (o == " "):
            fraseResultado += separar_silabas_desencriptar(palabraActual)
            fraseResultado += " "
            palabraActual = ""
        else:
            palabraActual += o
    fraseResultado += separar_silabas_desencriptar(palabraActual)
    return fraseResultado

def separar_silabas_desencriptar(palabra):
    vocales="aeiouáéíóúü"
    diccionario = pyphen.Pyphen(lang='es_ES')
    palabraSeparada = diccionario.inserted(palabra)
    palabraresultado = ""
    silabaPar = False
    for i in palabraSeparada:
        if (i == "-"):
            if (silabaPar == True):
                silabaPar = False
            else:
                silabaPar = True
        if (silabaPar == False) and (i != "-"):
            palabraresultado += i
    return palabraresultado

#Seguro que hay formas de resumir el codigo y no tenerlo "duplicado" pero soy vago1
if __name__ == "__main__":
    print("========[Menu]========")
    print("(1) Encriptar")
    print("(2) Desencriptar")
    print("======================")
    respuesta=""
    while ((respuesta != "1") or (respuesta != "2")):
        respuesta = input("Elije una opcion: ")
        if (respuesta == "1"):
            frase = input("Introduce la frase que quieres encriptar: ")
            print(separar_palabras_encriptar(frase))
            break
        if (respuesta == "2"):
            frase = input("Introduce la frase que quieres desencriptar: ")
            print(separar_palabras_desencriptar(frase))
            break
    input("Pulsa intro para finalizar")