N, L, P, Q = map(int, input().split())
result = []
for n in range(N):
    S = int(input())
    T = None
    if S <= L:
        T = (S * P)//100
    else:
        T = (L * P + (S - L) * Q)//100
    result.append(T)
for r in result:
    print(r)
