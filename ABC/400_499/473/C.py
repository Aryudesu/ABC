N, K = map(int, input().split())
A = list(map(int, input().split()))
C = [0] * K
for a in A:
    C[a-1] += 1
M = max(C)
print(C.count(M) + C.count(M-1))
