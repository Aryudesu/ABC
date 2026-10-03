N, M = map(int, input().split())
D = list(map(int, input().split()))
print((sum(D) + M - 1) // M)
