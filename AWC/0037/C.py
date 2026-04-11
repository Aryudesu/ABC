def calc_rev(num: int, MOD:int = 1000000007)->int:
    return pow(num, MOD-2, MOD)

MOD = 1000000007
N, K = map(int, input().split())
A = list(map(int, input().split()))
result = 0
tmp = 1
for k in range(K):
    a = A[k]
    tmp = (tmp * a) % MOD
result = tmp % MOD
for i in range(1, N-K+1):
    a = A[i+K-1]
    b = A[i-1]
    tmp = (tmp * a) % MOD
    tmp = (tmp * calc_rev(b, MOD)) % MOD
    result = (result + tmp) % MOD
    # print(i, i+K-1)
print(result)
