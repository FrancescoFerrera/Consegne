import math

while True:
    print("Scegli la figura di cui vuoi calcolare il perimetro:")
    print("1. Quadrato")
    print("2. Rettangolo")
    print("3. Cerchio")
    print("4. Esci dal menù")

    scelta = input("Inserisci la tua scelta (1-4): ")

    if scelta == '1':
        print("Quadrato.")
        lato = 0.0
        while lato <= 0:
            lato = float(input("Inserisci il lato del quadrato in cm: "))
            if lato <= 0:
                print("Il lato deve essere un numero maggiore di 0!")      
        perimetro_Q = lato * 4
        print("Il perimetro del quadrato vale ", perimetro_Q, " cm")
    elif scelta == '2':
        print("Rettangolo.")
        base = 0.0
        while base <= 0:
            base = float(input("Inserisci la base del rettangolo in cm: "))
            if base <= 0:
                print("La base deve essere un numero maggiore di 0!")
        altezza = 0.0
        while altezza <= 0:
            altezza = float(input("Inserisci l'altezza del rettangolo in cm: "))
            if altezza <= 0:
                print("L'altezza deve essere un numero maggiore di 0!")
        if base == altezza:
            print("Avresti potuto scegliere quadrato nel menù.")     
        perimetro_R = base * 2 + altezza * 2
        print("Il perimetro del rettangolo vale ", perimetro_R, " cm")
    elif scelta == '3':
        print("Cerchio.")
        raggio = 0.0 
        while raggio <= 0:
            raggio = float(input("Inserisci il raggio del cerchio in cm: "))
            if raggio <= 0:
                print("Il raggio deve essere un numero maggiore di 0!")        
        circonferenza = 2 * math.pi * raggio
        print("La circonferenza del cerchio vale ", circonferenza, " cm") 
    elif scelta == '4':
        print("Uscita dal menù.")
        break
    else:
        print("Scelta non valida, seleziona un numero da 1 a 4.")