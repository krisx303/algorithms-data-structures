"""
Wykorzystanie 'unii'. Tworzymy zbiory liter z 'liderami' (literami najmniejszymi leksykograficznie).
Na koniec dla każdej litery tekstu wypisujemy lidera zbioru w którym się znajduje.
"""


def litery(A: str, B: str, C:str):
    P = [i for i in range(26)]
    for x in range(len(A)):
        a = ord(A[x]) - 97
        b = ord(B[x]) - 97
        if a < b:
            P[b] = a
        else:
            P[a] = b
    for x in range(26):
        print(chr(97+x), chr(97+P[x]))
    c = ""
    for i in range(len(C)):
        c += chr(97+P[ord(C[i])-97])
    print(c)

A = "pawelob"
B = "wkapeio"
C = "wpkboi"
litery(A, B, C)