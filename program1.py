kotel = "=^_^="
ilosckotelow = input("Cześć, podaj swój numer karty,przegrywie :)")

try:
    ilosckotelow =int(ilosckotelow)
except ValueError as owcaError:
    print("nie wpisałeś liczby całkowitej")
    ilosckotelow = 7

#zadanie Domowe
"""
napisać program który generuje dowolną priramide z kotelow.
Założenia: Jeśli uzytkownik wpisze liczbe ujemną to powino go okrzyczeć i wypisać do konsoli =^!^=
Przykaład:
dla ilosc kotelow = 3
Hint: Pętle for i ify
"""