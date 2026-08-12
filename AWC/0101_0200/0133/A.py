N, M, K = map(int, input().split())
T = list(map(int, input().split()))
D = set()
if M > 0:
    D = set(map(int, input().split()))
for d in D:
    T[d-1] = 0
print(sum(t//K for t in T))
