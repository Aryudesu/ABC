# ABC5^3
N, D, S = map(int, input().split())
T = list(map(int, input().split()))
result = (N-1)*D + min(max(N-S, 0), max(S - 1, 0)) * D + sum(T)
print(result)
