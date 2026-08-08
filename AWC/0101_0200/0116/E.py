from collections import defaultdict

MOD = 10**9 + 7
def calc(N: int)->int:
    """N以下の個数を求めたい"""
    S = str(N)
    L = len(S)
    eq = defaultdict(int)
    smaller = defaultdict(int)
    l = int(S[0])
    eq[l] = 1

    for n in range(10):
        if n < l:
            smaller[n] = 1

    for i in range(1, L):
        nextEQ = defaultdict(int)
        nextSmaller = defaultdict(int)
        for n in range(10):
            for m in range(10):
                if n > m:
                    if n == int(S[i]):
                        nextEQ[n] = eq[m]


L = int(input())
R = int(input())