N, M = map(int, input().split())
D = list(map(int, input().split()))
D.sort(reverse=True)
for m in range(min(M, N)):
    D[m] = 0
print(max(D))
