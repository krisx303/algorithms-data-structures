# Zadanie 1
## Spadające klocki
Dany jest zbiór klocków $K$ = ($K_1$, $K_2$, ..., $K_n$). Każdy klocek $K_i$ opisany jest jako jednostronnie domknięty przedział $(a_i, b_i]$, gdzie $a_i, b_i \in \N$ i ma wysokość 1 (należy założyć, że żadne dwa klocki nie zaczynająsięw tym samym punkcie, czyli wartości $a_i$ są parami różne). Klocki są zrzucane na oś liczbową w pewnej kolejności. Gdy tylko spadający klocek dotyka innego klocka (powierzchnią poziomą), to jest do niego trawale doczepiony i przestaje spadać. Kolejnosć spadania klocków jest poprawna jeśli każdy klocek albo w całości ląduje na osi liczbowej, albo w całości ląduje na innych klockach. 

Rozważmy przykładowy zbiór klocków $K$ = {$K_1$, $K_2$, $K_2$, $K_2$}, gdzie:
$K_1$ = (2, 4] $K_2$ = (5, 7] $K_3$ = (3, 6] $K_4$ = (4, 5].

Kolejność $K_1$ $K_4$ $K_2$ $K_3$ jest poprawna (choć istnieją też inne poprawne kolejności) podczas gdy kolejność $K_1$ $K_2$ $K_3$ $K_4$ poprawna nie jest ($K_3$ nie leży w całości na innych klockach).

# Zadanie 2
## Problem plecakowy, ale liczymy ilość rozwiązań
Złodziej włamuje się do sklepu z przedmiotami o wagach i cenach, będących liczbami naturalnymi dodatnimi. Chowa je do plecaka, w którym może unieść rzeczy o łącznej maksymalnej wadze $W_max$. Tym razem złodziejowi nie zależy na tym, by ukraść artykuły o najwyższej możliwej łącznej cenie. Interesuje go za to, na ile sposobów może wybrać przedmioty, aby ich łączna cena była równa co najmniej $C_min$ oraz aby ich łączna waga nie przekraczała $W_max$.

# Zadanie 3
## Żeglarz Henryk
Żeglarz Henryk mieszka na wysepce pewnego archipelagu. Wszystkie wyspy w tym archipelagu są tak małe, że można je reprezentować jako punkty w przestrzeni $R^2$. Pozycji wszystkich wysp dane są jako ciąg $W = ((x_1, y_1), (x_2, y_2), ..., (x_n, y_n)).$

Henryk mieszka na wyspie $(x_1, y_1)$, ale chce się przeprowadzić na wyspę $(x_n, y_n)$. Normalnie, każdego dnia może przepłynąć na wyspę znajdującą się w odległości najwyżej Z (w sensie standardowej odległości euklidesowej), ale może także każdego dnia przepłynąć odległość do 2Z, pod warunkiem, że cały następny dzień będzie odpoczywał. Henryk musi zawsze nocować na jakiejś wyspie. Ile minimalnie dni potrzebuje Henryk, żeby dostać się na swoją docelową wyspę (lub czy jest to nie możliwe)?

# Zadanie 4
## Sasza i matrioszki
Sasza kolekcjonuje rosyjskie lalki - matrioszki. Każda z nich ma określoną wysokość Y i szerokość X,dane liczbami naturalnymi dodatnimi. Jedną matrioszkę można włożyć do drugiej, jeżeli ma od niej mniejszą zarówno wysokość, jak i szerokość.

Sasza zastanawia się, jaki jest najdłuższy ciąg matrioszek, które może powkładać w siebie po kolei.

# Zadanie 5
## Opieka nad dzieckiem
Cersel i Jalme mają 3 letniego syna. Przygotowali listę N aktywności podanych jako pary reprezentujące czas rozpoczęcia i zakończenia danej aktywności. Zaimplementuj algorytm, który przyporządkuje każdej aktywności literę C lub J, oznaczającą, że daną aktywność z synem wykona odpowiednio Cersei lub Jalme, w taki sposób, że żaden rodzic nie wykonuje pokrywających się czasowo aktywności. Jeżeli takie przyporządkowanie nie istnieje, to algorytm zwraca "IMPOSSIBLE", a jeśli istnieje, to zwraca odpowiedniego stringa.

Przykładowo: (99, 150), (1, 100), (100, 301), (2, 5), (150, 250) - odpowiedź to JCCJJ lub CJJCC.

# Zadanie 6
## Pakowanie bagaży
Wyheżdżacie ze znajomymi na wakacje. Macie dwa samochody i N bagaży o łącznej wadze W. Waga każdego z bagaży jest liczbą naturalną dodatnią. Czy jesteście w stanie tak je zapakować, aby w obu samochodach były bagaże o tej samej łącznej wadze?