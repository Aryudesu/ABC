N, K = map(int, input().split())
D = list(map(int, input().split()))
D.sort(reverse=True)
for k in range(K):
    D[k] = 0
print(sum(D))
