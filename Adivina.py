import random

def leer_numero():
    es_numero = False
    while es_numero==False:
        try:
            usuario = int(input("Adivina el número: "))
            es_numero=True
        except ValueError:
            print("No has introducido ningun número. Vuelva a intentarlo")
    return usuario

vidas = 5
print("¡Bienvenido a adivina el número!")
continuar = True
while continuar:
    print("...............Te quedan {} vidas...............".format(vidas))
    print("Estoy pensando un número entre el 1 y el 10")
    numero = random.randint(1,10)
    usuario = leer_numero()
    if numero==usuario:
        print("¡Has acertado!")
        vidas = vidas + 1
    else:
        print("Te has confundido el número era: {}".format(numero))
        vidas = vidas - 1
        if vidas == 0:
            continuar = False
            print("Se te han acabado las vidas.")
            break

    input()
    print()
    print("------------------------------------------------")
    print()