# Zadanie 1.
## Cięcie pręta na kawałki
Firma kupuje długie stalowe pręty i tnie je na kawałki, które sprzedaje. 
Kawałki mają długość w metrach wyrażoną zawsze liczbą naturalną. 
Dla kawałka długości n metrow znane są ceny kawałków długości 1, 2, 3, ... n metrów. 
Firma chce znać maksymalny zysk, który może uzyskać z pocięcia i sprzedania pręta długości n.

Złożoność obliczeniowa: O($n^2$)


# Zadanie 2.
## Modyfikacja zadania 1
Zmodyfikuj rozwiązanie problemu cięcia stalowych prętów tak, aby konstruowało i zwracało także rozwiązanie, tj. listę długości prętów o największej cenie.
Podpowiedź bottom-up będzie łatwiej.

Złożoność obliczeniowa: O($n^2$)

# Zadanie 3.
## Rekurenyjne schody Amazona
Dana jest tablica A zawierająca liczby naturalne nie mniejsze od 1. Początkowo stoimy na pozycji 0, wartość A[i] informuje nas jaka jest maksymalna długość skoku na następną pozycję.

Przykład A = [1, 3, 2, 1, 0].

Z pozycji 0 mogę przejść na pozycję 1, z pozycji 1 mogę przejść na 2, 3, 4. Należy policzyć na ile sposobów mogę przejść z pozycji 0 na pozycję n-1 przestrzegając reguł tablicy.

Złożoność obliczeniowa: O($n^2$)

# Zadanie 4.
## Minimalny koszt przejścia po 2-wymiarowej tablicy
Dostajemy tablicę [MxN] wypełnioną wartościami (kosztem wejścia na dane pole). Mamy znaleźć minimalny koszt potrzebny do dostania się z pozycji [0][0] do [M-1][N-1]. 

Dla uproszczenia przyjmijmy:
1. Możemy poruszać się tylko w bok i w dół.
2. Wszystkie koszty są dodatnie.

Złożoność obliczeniowa: O($n^2$)

# Zadanie 5.
## Najdłuższy rosnący ciąg w 2-wymiarowej tablicy
Dostajemy tablicę [MxN] wypełnioną wartościami. Mamy za zadanie znaleźć najdłuższą ścieżkę w tej tablicy (możemy przechodzić na pola sąsiadujące krawędziami), o rosnących wartościach (to znaczy że z pola o wartości 3, mogę przejść na pola o wartości większej bądź równej 4).

Dla uproszczenia przyjmijmy że mamy dany punkt początkowy najdłuższej ścieżki.

Złożoność obliczeniowa: O($n^2$)

# Zadanie 6.
## Binarne stringi bez jedynek obok siebie
Dostajemy liczbę naturalną n. Naszym zadaniem jest policzenie wszystkich binarnych (0/1) stringów o długości n bez jedynek obok siebie.

Złożoność obliczeniowa: O($n$)

# Zadanie 7.
## Uogólniony problem paczki mentosów
Dostajemy listę wartości. Gramy z drugim graczem. Wybieramy zawsze jedną wartość z jednego z końców tablicy i dodajemy do swojej sumy, a następnie to samo robi nasz przeciwnik. Zakładając, że przeciwnik gra optymalnie, jaką maksymalną sumę możemy uzbierać?

# Zadanie 8.
## Palindrom
Dostając na wejściu string złożony z liter a-z, zwróć najdłuższy jego fragment, który jest palindromem.