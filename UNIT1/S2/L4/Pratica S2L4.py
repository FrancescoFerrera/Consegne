import math

print("Scegli la figura di cui vuoi calcolare il perimetro:")
print("1. Quadrato")
print("2. Rettangolo")
print("3. Cerchio")

scelta = input("Inserisci la tua scelta (1-3): ")

if scelta == '1':
    print("Quadrato")
    lato = float(input("Inserisci il lato del quadrato in cm: "))
    perimetro_q = lato * 4
    print("Il perimetro del quadrato vale ", perimetro_q, "cm")
elif scelta == '2':
    print("Rettangolo")
    base = float(input("Inserisci la base del rettangolo in cm: "))
    altezza = float(input("Inserisci l'altezza del rettangolo in cm: "))
    perimetro_r = base * 2 + altezza * 2
    print("Il perimetro del rettangolo vale ", perimetro_r, "cm")
elif scelta == '3':
    print("Cerchio")
    raggio = float(input("Inserisci il raggio del cerchio in cm: "))
    circonferenza = 2 * math.pi * raggio
    print("La circonferenza del cerchio vale ", circonferenza, "cm")
else:
    print("Errore")