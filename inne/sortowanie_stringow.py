"""
Posortować tablicę stringów o różnych długościach.


Można też powrzucać do kubełków względem długości (gdzie największą długość oznaczam jako k),
potem posortować countingiem tylko te o długości k, względem k-tej litery.
Potem dołączyć te wszystkie liczby na koniec k-1 kubełka i znowu posortować countingiem kubełek k-1 względem k-1 litery
i tak powtarzać do momentu gdy k=0
"""