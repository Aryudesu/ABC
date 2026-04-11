def calcModSum(N: int, a: int, MOD: int = 998244353):
    """1～Nのnについてn%aの総和を計算"""
    tmp = (((a-1) * a) //2) % MOD
    num = N // a
    modNum = N % a
    tmp2 = (((modNum+1) * modNum) //2) % MOD
    result = (num * tmp + tmp2) % MOD
    print("debug", N, a, result)
    return result

MOD = 998244353
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
SA = sum(A)
SB = sum(B)

for i in range(N):
    tmp = []
    for j in range(M):
        tmp.append(((j+1)-(i+1)) % (j+1))
    print(tmp)

result = 0
for j in range(M):
    tmp = (SA * calcModSum(N, j+1, MOD)) % MOD
    result = (result + tmp) % MOD
print(result)

