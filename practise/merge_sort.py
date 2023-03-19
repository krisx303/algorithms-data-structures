"""
Algorytm wykonuj dopóki tablice mają więcej niż 1 element.
Znajdź środek sortowanej tablicy, względem niego utwórz tablicę Lewą i Prawą.
Wykonaj rekurencyjnie algorytm dla obu tablic. Następnie wykonaj scalanie.
Ustaw wskaźniki na początkach tablic. I przepisuj do właściwej tablicy wartości mniejsze przesuwając odpowiedni wskaźnik
Jeżeli pozostała jakaś część tablicy do ją dopisz. (Zawsze będzie reszta tylko jednej tablicy).
"""


def merge_sort(A: list[int]):
    n = len(A)
    if n < 2:
        return
    mid = n//2
    L = A[:mid]
    R = A[mid:]

    merge_sort(L)
    merge_sort(R)

    i = 0
    j = 0
    k = 0
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1

    while i < len(L):
        A[k] = L[i]
        i += 1
        k += 1

    while j < len(R):
        A[k] = R[j]
        j += 1
        k += 1


if __name__ == "__main__":
    A = [1, 25, 8, 1, 12, 7, 2]
    merge_sort(A)
    print(A)