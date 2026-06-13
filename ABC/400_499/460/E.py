MOD = 998244353

def calc(N: int, M: int)->int:
    c = N // M
    return ((c * N) % MOD)

T = int(input())
result = []
for _ in range(T):
    N, M = map(int, input().split())
    res = calc(N, M)
    result.append(res)
for r in result:
    print(r)
