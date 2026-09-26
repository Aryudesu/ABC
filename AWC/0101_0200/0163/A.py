N, M, K = map(int, input().split())
A = list(map(int, input().split()))
S = sum((a+K-1)//K for a in A)
print(max(0, S-M))
