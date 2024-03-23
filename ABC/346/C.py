N, K = [int(l) for l in input().split()]
A = [int(l) for l in input().split()]
B = []
for a in A:
    if a <= K:
        B.append(a)
C = set(B)
S = (K * (K + 1)) // 2
print(S - sum(C))
