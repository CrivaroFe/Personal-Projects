# Questo è un semplice programma calcolatrice scritto in Python.
# Il programma permette all'utente di eseguire operazioni aritmetiche di base:
# addizione, sottrazione, moltiplicazione e divisione.
# Il programma chiede all'utente di scegliere un'operazione e inserire due numeri.
# In base all'operazione scelta, mostra il risultato.

print('=-' * 20)
print(f'{"LA CALCOLATRICE":^40}')
print('=-' * 20)

# Il programma:
def somma(a, b):
    return a + b

def sottrai(a, b):
    return a - b

def moltiplica(a, b):
    return a * b

def dividi(a, b):
    if b == 0:
        return "\033[31mErrore! Divisione per zero.\033[m"
    return a / b

def principale():
    while True:
        print("Seleziona l'operazione desiderata:")
        print('-' * 40)
        print("1. Somma")
        print("2. Sottrai")
        print("3. Moltiplica")
        print("4. Dividi")
        print('-' * 40)
        scelta = input("Inserisci il numero dell'operazione (1/2/3/4): ")

        if scelta in ['1', '2', '3', '4']:
            # Aggiunta della validazione dell'input per i numeri
            try:
                num1 = float(input("Inserisci il primo numero: "))
                num2 = float(input("Inserisci il secondo numero: "))
            except ValueError:
                print("\033[31mErrore: Inserisci un numero valido.\033[m")
                continue  # Ritorna al ciclo per una nuova tentativo di input

            print('=-' * 20)
            if scelta == '1':
                print(f"Il risultato della somma è: {somma(num1, num2)}")
            elif scelta == '2':
                print(f"Il risultato della sottrazione è: {sottrai(num1, num2)}")
            elif scelta == '3':
                print(f"Il risultato della moltiplicazione è: {moltiplica(num1, num2)}")
            elif scelta == '4':
                print(f"Il risultato della divisione è: {dividi(num1, num2)}")
            print('=-' * 20)
        else:
            print('\033[31mOpzione non valida!\033[m')

        calcola_di_nuovo = input("Vuoi calcolare un altro risultato? (S/N): ").upper()[0]

        if calcola_di_nuovo == 'N':
            print('=-' * 20)
            print(f'{"Programma Terminato":^40}')
            print('=-' * 20)
            break
        elif calcola_di_nuovo != 'S':
            print('\033[31mOpzione non valida! Il programma si chiuderà.\033[m')
            print('=-' * 20)
            print(f'{"Programma Terminato":^40}')
            print('=-' * 20)
            break


if __name__ == '__main__':
    principale()
# Serve per eseguire il codice solo quando il file è eseguito direttamente, non quando è importato come modulo.



