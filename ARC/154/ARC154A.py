MOD = 998244353
N = int(input())
A = list(input())
B = list(input())
for n in range(N):
    a = int(A[N - n - 1])
    b = int(B[N - n - 1])
    if a > b:
        A[N - n - 1], B[N - n - 1] = B[N - n - 1], A[N - n - 1]
result = int("".join(A)) * int("".join(B))
print(result % MOD)
