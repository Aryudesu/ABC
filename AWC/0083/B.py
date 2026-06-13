from fractions import Fraction

N, Q = map(int, input().split())
H = list(map(int, input().split()))
result = []
for _ in range(Q):
    query = list(map(int, input().split()))
    match query[0]:
        case 1:
            _, x, h = query
            H[x-1] = h
        case 2:
            _, a, b = query
            res = a-1
            maxVp = Fraction()
            for p in range(a-1, b):
                Lp = Fraction()
                for idx in range(p):
                    Lp = max(Lp, Fraction(H[idx], p - idx))
                Rp = Fraction()
                for idx in range(p+1, N):
                    Rp = max(Rp, Fraction(H[idx], idx - p))
                Vp = Fraction(1, 1 + Lp + Rp)
                if maxVp < Vp:
                    res = p
                    maxVp = Vp
            print(res + 1)
