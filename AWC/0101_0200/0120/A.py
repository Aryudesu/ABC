N, K = map(int, input().split())
result = []
for n in range(N):
    M, *S = list(map(int, input().split()))
    result.append(sum(s >= K for s in S))
print(*result, sep="\n")
