def calc(N: int, X: int, A: list[int])->int:
    s = 0
    for idx in range(N):
        a = A[idx]
        s += a
        if s >= X:
            return idx + 1
    return -1

N, X = map(int, input().split())
A = list(map(int, input().split()))
print(calc(N, X, A))
