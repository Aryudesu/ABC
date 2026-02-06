def calc(N: int, M: int, S: str, T: str)-> int:
    result = 10000000
    for n in range(N-M+1):
        tmp = 0
        for m in range(M):
            s = int(S[n+m])
            t = int(T[m])
            if s >= t:
                tmp += s - t
            else:
                tmp += (10 + s) - t
        result = min(result, tmp)
    return result

N, M = map(int, input().split())
S = input()
T = input()
print(calc(N, M, S, T))
