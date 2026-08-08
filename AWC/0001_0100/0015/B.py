def calc(N: int, K: int, P: list[int])->int:
    for i in range(N):
        if P[i] >= K:
            return i + 1
    return -1

N, K = map(int, input().split())
P = list(map(int, input().split()))
print(calc(N, K, P))
