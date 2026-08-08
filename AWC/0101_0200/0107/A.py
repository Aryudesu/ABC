N, D, V = map(int, input().split())
S = list(map(int, input().split()))
print(sum(s > V for s in S))
