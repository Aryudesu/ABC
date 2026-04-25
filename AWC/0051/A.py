N, M, K = map(int, input().split())
P = list(map(int, input().split()))
L = list(map(int, input().split()))
T = list(map(int, input().split()))
A = 0
for t in T:
    A = max(L[t-1], A)
result = 0
for p in P:
    if p <= A:
        result += p
print(result)
