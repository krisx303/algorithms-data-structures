# Zadanie 1 
## Minimalizacja błędów zaokrągleń
Asystent znanego profesora otrzymał polecenie wyliczenia sumy pewnego ciągu liczb (liczby mogą być zarówno dodatnie jak i ujemne). Aby zminimalizować błędy zaokrągleń asystent postanowił wykonać powyższe dodawania w takiej kolejności, by największy co do wartości bezwzględnej wynik tymczasowy (wynik każdej operacji dodawania; wartość końcowej sumy również traktujemy jak wynik tymczasowy) był możliwie jak najmniejszy.

Aby ułatwić sobie zadanie, asysteny nie zmienia kolejności liczb w sumie a jedynie wybiera kolejność dodawań. Napisz funkcję która przyjmuje tablicę liczb n1, n2, ... nk (w kolejności w jakiej występują w sumie; zakładamy, że tablica zawiera co najmniej dwie liczby) i zwraca największą wartość bezwzględną wyniku tymczasowego w optymalnej kolejności dodawań.

Na przykład dla tablicy wejściowej: [1, -5, 2] funkcja powinna zwrócić wartość 3, co odpowiada dodaniu -5 i 2 a następnie dodaniu 1 do wyniku.

# Zadanie 2
## Łączenie napisów w jeden
Mamy dany ciąg napisów (słów) S = [s1,s2,...,sn] oraz pewien napis t. Wiadomo że t można zapisać jako złączenie pewnej ilości napisów z S (z powtórzeniami). Na przykład dla S = [ab, abab, ba, bab, b], napis t = ababbab można zapisać, między innymi jako abab + bab lub jako ab + ab + ba + b.

Taki wybór konkretnych $s_i$ nazywamy reprezentacją. przez szerokość reprezentacji rozumiemy długość najkrótszego $s_i$ należącego do reprezentacji - dla abab + bab szerekość to 3.

Zaimplementuj algorytm, który mając na wejściu S oraz t znajdzie maksymalną szerokość reprezentacji t (tzn najkrótszy napis w jej reprezentacji jest możliwie jak najdłuższy).

# Zadanie 3
## Ropucha Zbigniew
Żaba Zbigniew skacze po osi liczbowej. Ma się dostać z zera do n-1, skacząc wyłącznie w kierunku większych liczb. Skok z liczby j (j>i) kosztuje Zbigniewa j - i jednostek energii, a jego energia nigdy nie może spaść poniżej zera. Na początku Zbigniew ma 0 jednostek energii, ale na szczęście na niektórych liczbach - także na zerze- leżą przekąski o określonej wartości energetycznej (wartość przekąski dodaje się do aktualnej energii Zbigniewa).

Proszę zaimplementować funkcję, która otrzymuje tablicę A długości N gdzie każde pole zawiera wartość energetyczną przekąski leżącej na odpowiedniej liczbie. Funkcja powinna zwrócić minimalną liczbę skoków potrzebną, żeby Zbigniew dotarł z zera do n-1 lub -1 gdy nie jest to możliwe.

Podpowiedź: Warto rozważyć funkcję f(i, y) zwracającą minimalną liczbę skoków potrzebną by dotrzeć do liczby i mając w zapasie dokładnie y jednostek energii.

Przykład: Dla tablicy A = [2, 2, 1, 0, 0, 0] wynikiem jest 3 (Zbigniew skacze z 0 na 1, z 1 na 2 i z 2 na 5, kończąc z zerową energią). Dla tablicy A = [4, 5, 2, 4, 1, 2, 1, 0] wynikiem jest 2 (Zbigniew skacze z 0 na 3 i z 3 na 7 kończąc z jedną jednostką energii).

# Zadanie 4
## Czarodziej Pascal
Czarodziej Pascal ma N stosów porcelanowych talerzy, przy czym każdy stos zawiera dokładnie k talerzy. Pascal wystawia dziś wieczorem kolację dla P gości i jedzenie będzie serwowane na tych właśnie talerzach. Każdy talerz ma pewne piękno określone liczbą całkowitą. Pomóż czarodziejowi wybrać dokładnie P talerzy tak, aby miały one maksymalnie możliwe piękno. 

Ale uwaga! Stos to stos (xD) więc jeśli chcesz zabrać jakiś talerz to musisz też zabrać wszystkie nad nim.

# Zadanie 6
## Ciąg słów ze słownika
Dana jest zawsze działająca w czasie O(1) funkcja dict(word), która mówi, czy słowo jest poprawnym słowem danego języka. Dostajemy na wejściu stringa bez spacji. Podaj algorytm, który stwierdzi, czy da się tak powstawiać spacje do wejściowego stringa, że ciąg słów który otrzymamy tworzą słowa z danego języka. Np "alamakotainiemapsa" możemy zapisać jako "ala ma kota i nie ma psa". Podaj również, jak wykorzystać algorytm, aby uzyskać przykładowe poprawne rozdzielenie stringa spacjami, jeśli oczywiście ono istnieje.

# Zadanie 7
## Cięcie tkaniny
Dany jest prostokątny kawałek tkaniny o wymiarach X x Y, oraz lista n produktów, które mogą zostać wykonane z tej tkaniny. Do wytworzenia każdego produktu i (i zmienia się od 1 do n) potrzebny jest prostokątny kawałek tkaniny o wymiarach $a_i$ na $b_i$, a zysk ze sprzedaży tego produktu wynosi $c_i$. Zakładamy, że $a_i$, $b_i$, $c_i$ są dodatnie całkowite. Mając maszynę, która może przeciąć dowolny prostokątny kawałek tkaniny na dwa kawałki wzdłuż linii poziomej lub pionowej, zaprojektuj algorytm, który wyznaczy taką strategię cięcia materiału o wymiarach X na Y, aby sprzedaż wytworzonych produktów dała łącznie jak największy zysk.