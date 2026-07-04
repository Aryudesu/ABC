N, K = map(int, input().split())
for n in range(N):
    X = int(input())
    if n == K-1:
        print(X-1)
