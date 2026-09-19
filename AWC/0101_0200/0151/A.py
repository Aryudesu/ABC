N, M, K = map(int, input().split())
SA = sum(int(input()) for _ in range(M))
print("Yes" if SA <= N * K else "No")
