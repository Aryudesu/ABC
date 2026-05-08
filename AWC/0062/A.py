N, M, K = map(int, input().split())
A = list(map(int, input().split()))
c = sum(a//K for a in A)
print("Yes" if c >= M else "No")
