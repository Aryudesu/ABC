N, K = map(int, input().split())
D = list(map(int, input().split()))
D.sort()
print(sum(D[K:]))
