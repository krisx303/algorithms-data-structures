"""
NIE DZIAŁA
Zliczamy występowanie liter w tablicy pomocniczej. Tworzymy 'upośledzony' stos do którego
"""


def delete(t: str) -> str:
    C = [0 for _ in range(26)]
    for x in t:
        C[ord(x)-97] += 1
    print(C)

    stack = []

    for c in t:
        print(stack)
        x = ord(c)-97
        if len(stack) == 0:
            stack.append(x)
            continue
        last = stack[-1]
        if last > x:
            if C[last] > 1:
                stack.pop(-1)
        stack.append(x)


if __name__ == "__main__":
    t = "cbacdcbcabcdbcbbdacbbdabcb"
    print(delete(t))
