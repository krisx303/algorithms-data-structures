"""
f(i) - szerokość napisu od i-tego znaku do końca słowa t


f(0) = max(s in S and t[0:] starts with s){f(0+len(s))}
S = [ab, abab, ba, bab, b], napis t = ababbab 


"""

def lacz(S: list[str], t: str) -> int:
    d = len(t)
    F = [-1 for _ in range(d)]

    def f(i: int) -> int:
        if i == d:
            return 0
        if i > d:
            return -1
        if F[i] != -1:
            return F[i]
        m = -1
        for s in S:
            if t[i:].startswith(s):
                o = f(i+len(s))
                if o == 0:
                    m = max(m, len(s))
                if o != -1:
                    m = max(m, min(o, len(s)))
        F[i] = m
        return m

    return f(0)


if __name__ == "__main__":
    t = "ababbab"
    S = ["ab", "abab", "ba", "bab", "b"]
    # t = "oooobbb"
    # S = ["bbb", "oooo"]
    print(lacz(S, t))
