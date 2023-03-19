"""
Tworzymy kolejkę priorytetową wielkości p (maksymalna pojemność stacji).
Dodajemy do niej początkowe p odjazdów. Następnie dla każdego kolejnego przyjazdu wyjmujemy z niej jeden odjazd
i sprawdzamy czy czasy się nie pokrywają. Jeśli nie to oznacza że nowy pociąg może spokojnie wjechać na stację,
w przeciwnym wypadku nie ma takiej możliwości.
"""


from queue import PriorityQueue


def rozklad(P: list[tuple[int, int]], p: int) -> bool:
    q = PriorityQueue()
    for i in range(p):
        q.put(P[i][1])

    j = p
    o = 3
    while j < len(P):
        odjazd = q.get()
        przyjazd = P[j][0]
        print(odjazd, przyjazd)
        if odjazd < przyjazd:
            q.put(P[j][1])
        else:
            return False
        j += 1
    return True


if __name__ == "__main__":
    P = [(900, 1100),
         (940, 1020),
         (1020, 1300),
         (1140, 1420),
         (1210, 1300),
         (1240, 1250),
         (1300, 1500)]
    p = 3
    print(rozklad(P, p))