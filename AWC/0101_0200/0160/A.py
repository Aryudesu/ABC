N, M = map(int, input().split())
score = []
for n in range(N):
    S = list(map(int, input().split()))
    score.append(sum(S) - max(S) - min(S))
print(score.index(max(score)) + 1)
