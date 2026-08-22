def calc(N: int, P: list[int])->int:
    S = sum(P)
    T = 0
    for n in range(N):
        if P[n] < 0:
            T += P[n]
        else:
            break
    for n in range(N-1):
        if P[n] < 0:
            T += P[n]
        else:
            break
    

N = int(input())
P = list(map(int, input().split()))
