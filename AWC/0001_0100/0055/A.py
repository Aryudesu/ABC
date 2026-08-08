N, K = map(int, input().split())
D = list(map(int, input().split()))
print(sum(D[i] for i in range(N) if (i + 1) % (K+1)))
