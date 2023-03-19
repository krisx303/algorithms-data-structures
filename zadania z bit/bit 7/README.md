# Zadanie 1
## Detekcja cyklu
Napisz algorytm sprawdzający, czy graf nieskierowany posiada cykl.

# Zadanie 2
## Wiadomość
Otrzymujemy na wejściu listę par ludzi, które się wzajemnie znają. Osoby są reprezentowane przez liczby od 0 do n-1.

Dnia pierwszego osoba 0 przekazuje pewna wiadomość wszystkim swoim znajomym. Dnia drugiego każdy ze znajomych przekazuje tę wiadomość wszystkim swoim znajomym, którzy jej jeszcze nie znali i tak dalej.

Napisz algorytm, który zwróci dzień, w którym najwięcej osób poznało wiadomość oraz ilość osób, które tego dnia ją otrzymały.

# Zadanie 3
## Jeziora
Dana jest dwuwymiarowa tablica N x N, w której każda komórka ma wartość "W" - reprezentującą wodę lub "L" - ląd. Grupę komórek wody połączonych ze sobą brzegiem nazywamy jeziorem.
1) Policz, ile jezior jest w tablicy
2) Policz, ile komórek zawiera największe jezioro
3) Zakłądając, że pola o indexach [0][0] i [n-1][n-1] są lądem, sprawdź czy da się przejść drogą lądową z pola [0][0] do pola [n-1][n-1]. Można chodzić tylko na boki, nie na ukos.
4) Znajdź najkrótszą ścieżkę miedzy tymi punktami. Wypisz po kolei indexy pól w tej ścieżce.

# Zadanie 4
## Sklejanie przedziałów
Dany jest ciąg przedziałów postaci [a, b]. Dwa przedziały można skleić, jeśli mają dokładnie jeden punkt wspólny. Podaj algorytm, który sprawdza, czy da się uzyskać przedział [a, b] poprzez sklejanie odcinków.

# Zadanie 5
## Sejf
Dostałeś sejf, który odblokowuje się czterocyfrowym PINem (0000 - 9999). Pod wyświetlaczem znajduje się kilka przycisków z liczbami od 1 do 9999 - przykładowo (13, 223, 782, 3902). Sejf ten działa inczej niż normalny: wciśnięcie przycisku z liczbą powodoju dodanie liczby z przycisku do liczby na wyświetlaczu. Jeżeli suma jest większa niż 9999, to pierwsza cyfra zostaje obcięta.

Jest tobie znany PIN oraz cyfry, które są aktualnie wyświetlane. Znajź najkrótszą sekwencję naciśnięć przycisków, która pozwoli ci odblokować sejf. Jeżeli taka sekwencja nie istnieje, zwróć None.

# Zadanie 6
## Rozmiary poddrzew
Dostajemy na wejściu listę krawędzi drzewa (niekoniecznie binarnego!) oraz wyrużniony wierzchołek - korzeń. Każdy wierzchołek tworzy swoje własne poddrzewo. Dla każdego wierzchołka, wyznacz ilość wierzchołków w jego poddrzewie.

# Zadanie 7
## Domy i sklepy
Mamy mapę miasteczka, w którym są domy i sklepy. Na mapie są również drogi (każda długości 1), które łączą dom z domem, albo dom ze sklepem. Naszym zadaniem jest, dla każdego domu, znaleźć odległość do najbliższego sklepu.

# Zadanie 8
## Średnica drzewa
Średnicą drzewa nazywamy odległość między najbardziej oddalonymi od siebie wierzchołkami. Napisz algorytm, który przyjmując na wejściu drzewo (niekoniecznei binarne!) w postaci listy krawędzi zwróci jego średnicę.