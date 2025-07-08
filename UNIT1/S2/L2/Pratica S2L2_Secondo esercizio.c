#include <stdio.h> //Libreria

//Media tra due numeri

int main() { //Inizio della funzione principale

    int n1; //Dichiarazione della variabile intera n1
    int n2; //Dichiarazione della variabile intera n2
    float m; //Dichiarazione della variabile reale m

    printf("Inserisci il primo numero: "); //Richiede l'input di n1
    scanf("%d" , &n1); //Input di n1
    printf("Inserisci il secondo numero: "); //Richiede l'input di n2
    scanf("%d" , &n2); //Input di n2

    m = (n1 + n2) / 2.0; 
    //Calcolo della media (divisione per 2.0 altrimenti, dividendo per 2, calcolerebbe m come numero intero e non come numero reale)

    printf("La media tra i due numeri vale: %f\n" , m); //Presentazione del risultato

    return 0; //Conclusione del programma
}
