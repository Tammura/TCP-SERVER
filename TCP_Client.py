import socket
import sys

def invia_comandi(s):
    messaggio = input("---> ")
    if messaggio == "ESC": #Nel caso l'utente non voglai inviare niente
        print("Sto chiudendo la connessione col Server.")
        s.close() #Viene chiuso il socket
        sys.exit()
    else:
        s.send(messaggio.encode()) #Viene codificato il messaggio e viene mandato al server 

def ricevi_comandi(s):
    risposta = ""
    while risposta == "":
        risposta = s.recv(4096) #lunghezza del buffer
        print(risposta.decode())

def conn_sub_server(indirizzo_server):
    try:
        s = socket.socket()             #Viene creato il socket
        s.connect(indirizzo_server)     #Viene effettuata la connessione al server
        print(f"Connessessione al Server: { indirizzo_server } effettuata.")
    except socket.error as errore: #in caso di errore viene avvisato l'utente e si esce dal programma.
        print(f"Qualcosa è andato storto, sto uscendo... \n{errore}")
        sys.exit()
    invia_comandi(s) #Viene chiamata la funzione che avrà il compito di inva un messaggio
    ricevi_comandi(s) #Viene chiamata la funzione che avrà il compito di inviare un messaggio 

if __name__ == '__main__':
    conn_sub_server(("192.168.178.81", 1001)) #Viene chiamata la funzione che avrà il compito di creare il socket e gestire varie operazioni, viene passato il numero della porta e l'indirizzo del server

