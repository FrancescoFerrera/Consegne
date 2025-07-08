#include <stdio.h> //Libreria

//Prodotto tra due numeri interi

int main() { //Inizio della funzione principale

    int n1;	//Dichiarazione della variabile intera n1
    int n2;	//Dichiarazione della variabile intera n2
    int p;	//Dichiarazione della variabile intera p

    printf("Inserisci il primo fattore: ");	//Richiede l'input di n1
    scanf("%d" , &n1);	//Input di n1
    printf("Inserisci il secondo fattore: "); //Richiede l'input di n2
    scanf("%d" , &n2);	//Input di n2

    p = n1 * n2;	//Calcolo del prodotto

    printf("Il prodotto vale: %d\n" , p); //Presentazione del risultato

    return 0; //Conclusione del programma
}
