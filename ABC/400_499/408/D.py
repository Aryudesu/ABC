def calc()-> int:
    N = int(input())
    S = input()
    C = [0] * (N + 1)

    for i in range(N):
        C[i + 1] = C[i] + (1 if S[i] == "0" else -1)
    sm = S.count("1")
    ma = 0
    res = 0
    for i in range(N+1):
        res = min(res, C[i] - ma)
        ma = max(ma, C[i])
    return sm + res


T = int(input())
for _ in range(T):
    print(calc())
