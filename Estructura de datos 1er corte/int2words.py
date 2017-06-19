# Program: int2words.py
# Description: Convertir un  número entero en palabras en español
# Author: Juan Pablo Trejos Rodriguez

def int2words(numero):
    """ (number) -> string
    return the number converted into a string of spanish words
    """
    # TODO: return the correct string
    #def numero_to_letras(numero):

    indicador = [("",""),("mil","mil"),("millon","millones"),("billon","billones")]

    entero = int(numero)

    contador = 0

    numero_letras = ("")

    while entero >0:

        a = entero % 1000

        if contador == 0:

            en_letras = convierte_cifra(a,1).strip()

        else :

            en_letras = convierte_cifra(a,0).strip()

        if a==0:

            numero_letras = en_letras+" "+numero_letras

        elif a==1:

            if contador in (1,3):

                numero_letras = indicador[contador][0]+" "+numero_letras

            else:

                numero_letras = en_letras+" "+indicador[contador][0]+" "+numero_letras

        else:

            numero_letras = en_letras+" "+indicador[contador][1]+" "+numero_letras

        numero_letras = numero_letras.strip()

        contador = contador + 1

        entero = int(entero / 1000)

    numero = numero_letras

    return numero

def convierte_cifra(numero,numero_letras):

    lista_centana = ["",("cien","ciento"),"doscientos","trescientos","cuatrocientos","quinientos","seiscientos","setecientos","ochocientos","novecientos"]

    lista_decena = ["",("diez","once","doce","trece","catorce","quince","dieciseis","diecisiete","dieciocho","diecinueve"),

                    ("veinte","veinti"),("treinta","treinta y"),("cuarenta" , "cuarenta y"),

                    ("cincuenta" , "cincuenta y"),("sesenta" , "sesenta y"),

                    ("setenta" , "setenta y"),("ochenta" , "ochenta y"),

                    ("noventa" , "noventa y")

                ]

    lista_unidad = ["",("un" ,"uno"),"dos","tres","cuatro","cinco","seis","siete","ocho","nueve"]

    centena = int (numero / 100)

    decena = int((numero -(centena * 100))/10)

    unidad = int(numero - (centena * 100 + decena * 10))

    #print "centena: ",centena, "decena: ",decena,'unidad: ',unidad

    texto_centena = ""

    texto_decena = ""

    texto_unidad = ""

    #Validad las centenas

    texto_centena = lista_centana[centena]

    if centena == 1:

        if (decena + unidad)!=0:

            texto_centena = texto_centena[1]

        else :

            texto_centena = texto_centena[0]

     #Valida las decenas

    texto_decena = lista_decena[decena]

    if decena == 1 :

         texto_decena = texto_decena[unidad]

    elif decena > 1 :

        if unidad != 0 :

            texto_decena = texto_decena[1]

        else:

            texto_decena = texto_decena[0]

    #Validar las unidades

    #print "texto_unidad: ",texto_unidad

    if decena != 1:

        texto_unidad = lista_unidad[unidad]

        if unidad == 1:

            texto_unidad = texto_unidad[numero_letras]
    
    numero_letras = "%s %s %s" %(texto_centena,texto_decena,texto_unidad) 
    return numero_letras
    

def main():
    """ Main Program """
    numero = int(input("enter an integer  number: "))
    numero_letras = int2words(numero)
    print("{} = {}".format(numero, numero_letras))

if __name__ == "__main__":
    main()

