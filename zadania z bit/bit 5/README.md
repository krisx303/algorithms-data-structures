# Zadanie 1
## Problem tankowania paliwa
W problemie tankowania paliwa nasz pojazd musi przemieścić się z punktu 0 do punktu F, a po drodze ma stacje do tankowania paliwa $s_i$. Każda stacja jest identyfikowana przez jej odległość od punktu 0, tzn $s_i$ to odległość pomiędzy i-tą stacją a punktem 0. Pojazd potrafi przejechać odległość d bez potrzeby tankowania. Podaj algorytm, który obliczy, na ilu minimalnie stacjach musi zatrzymać się pojazd na drodze od punktu 0 do punktu F.

Uwaga: jeżeli zdarzy się, że odległość d jest zbyt mała, żeby dojechać do kolejnej stacji, to należy zwrócić None.

# Zadanie 2
## Wydawanie monet
W problemie coin change mamy daną kwotę X i chcemy ją rozmienić na monety o wartościach 1, 5, 10, 25 i 100.

Podaj algorytm, który obliczy, ile minimalnie monet trzeba użyć do wydania reszty oraz ile sztuk każdej monety będzie trzeba użyć.
Można założyć, że każdej monety mamy nieskończenie wiele sztuk.

Czy algorytm zachłanny działa dla zestawu monet 1, 2, 7, 10? Jeśli tak, uzasadnij dlaczego. Jeśli nie, podaj kontrprzykład.

# Zadanie 3
## Rozkład pociągów na stacji
Mamy dany pewien rozkład pociągów, dany jako tablica n krotek (arrival_time, departure_time), przy czym są one posortowane niemalejąco według arrival_time. Chcemy wiedzieć, czy nasza stacja mająca m peronów jest w stanie bezkonfliktowo obsłużyć te pociągi, tzn w żadnym momencie nie będzie "rywalizacji" pociągów o dostępne perony.

Przedstaw algorytm, który poda odpowiedź True lub False na powyższe pytanie.

# Zadanie 4
## Ochrona miast przed koronawirusem
W jednej z chińskich prowincji postanowiono wybudować serię maszyn chronioących ludność przed koronawirusem. Prowincję można zobrazować jako tablicę wartości 1 i 0 gdzie arr[i] = 1 oznacza, że w mieście i można zbudować maszynę, a wartość 0, że nie ma takiej możliwości. Dana jest również liczba k, która oznacza, że jeśli postawimy maszynę w mieście i, to miasta o indexach j takich że abs(i-j) < k są przez nią chronione. 

Należy zaproponować algorytm, który stwierdzi ile minimalnie maszyn potrzeba aby zapewnić ochronę w każdym mieście, lub -1 jeśli nie jest to możliwe.

# Zadanie 5
## Podzbiór przedziałów
Dany jest zbiór przedziałów otwartych. Zaproponuj algorytm, który znajdzie podzbiór tego zbioru, taki że:

1) jego rozmiar wynosi dokładnie k
2) przedziały są rozłączne
3) różnica między najwcześniejszym początkiem, a najdalszym końcem jest minimalna.
Jeśli rozwiązania nie istnieje, to algorytm powinien to stwirdzić.

# Zadanie 6
## Usuwanie duplikatów liter ze stringa
Dany jest string, w którym niektóre litery się powtarzają. Należy zaproponować algorytm, który usunie ze stringa duplikaty tak, że otrzymany string będzie leksykograficznie najmniejszy.

Przykład cbacdcbc, odpowiedzią jest acdb.

# Zadanie 7
## Zlecenia
Dana jest lista zleceń. Każde zlecenie wymaga pewnego kapitału początkowego C, który należy mieć, żeby zacząć zlecenie oraz zysk P, który doda się do naszego całkowitego kapitału, gdy wykonamy zlecenie. Mając kapitał początkowy W i liczbę k wybierz co najwyżej k zleceń tak, że skończysz z maksymalnym możliwym kapitałem.

Przykład k = 2, W = 0, P = [1, 2, 3], C = [0, 1, 1]. Rozwiązanie: na początku, mamy kapitał 0, więc możemy wybrać tylko zlecenie pierwsze. Po jego ukończeniu mamy kapitał równy 1, więc możemy wybrać albo zlecenie 2 albo 3. Zlecenie 3 ma większy profit więc wybieramy zlecenie 3, ponieważ możemy wybrać jużtylko 1 zlecenie (k=2). Kończymy z kapitałem równym 4.

# Zadanie 8
## Zapraszanie znajomych na przyjęcie
Alicja chce zorganizować przyjęcie i zastanawia się, kogo zaprosić spośród n znajomych. Stworzyła już listę par osób które się znają. Chce wybrać możliwie jak najwięcej osób, tak aby spełnione były dwa warunki: na przyjęciu każda osoba powinna znać co najmniej 5 osób oraz co najmniej 5 osób nie znać.

Zaproponuj algorytm który przyjmuje na wejściu listę n osób oraz listę par osób które się znają, a na wyjściu daje możliwie najdłuższą listę gości.