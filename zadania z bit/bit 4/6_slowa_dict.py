"""
f(i) - czy ciąg znaków od i-tego do końca da się rozdzielić dobrze spacjami

Złożoność obliczeniowa: O(n^2)
Złożoność pamięciowa: O(n)
"""

d = ["ala", "kota", "ma", "al", "ta", "i", "nie", "psa", "ma", "aa", "a", "sa"]


def indict(s: str) -> bool:
    return s in d


def slowa(t: str) -> bool:
    n = len(t)

    F = [False for _ in range(n+1)]
    F[0] = True

    for i in range(n):
        if F[i] is True:
            for j in range(i, n+1):
                if indict(t[i:j]):
                    F[j] = True
    return F[n]


if __name__ == "__main__":
    t = "alamakotainiemapsa"
    print(slowa(t))
