#Kalkulator.
#Dane wejśćiowe od użytkownika.
num1 = float(input("Podaj liczbę: "))
operacja = (input("Wybierz operacja (+, -, *, /, **): "))
num2 = float(input("Podaj liczbę: "))
#Operacja dodawania.
if operacja == ("+"):
    wynik = num1 + num2
    print(wynik)
#Operacja odejmowania.    
if operacja == ("-"):
    wynik = num1 - num2
    print(wynik)
#Operacja mnożenia.
if operacja == ("*"):
    wynik = num1 * num2
    print(wynik)
#Operacja dzielenia i wyjątek.
if operacja == ("/"):
    if num2 != 0:
        wynik = num1 / num2
        print(f"{wynik:.2f}")
    else:
        print("Nie można dzielić zero!")
#operacja pierwiastkowania.
def exponentiation(num1, num2):
    result = num1 ** num2
    return result
if operacja == "**":
    print(exponentiation(num1, num2))