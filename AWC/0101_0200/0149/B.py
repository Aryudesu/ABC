N, M = map(int, input().split())
P = list(map(int, input().split()))
score = [0] * N
for n in range(N):
    S = input()
    for idx in range(M):
        score[n] += P[idx] * (S[idx] == "o")
data = sorted(score, reverse=True)
scoreData = dict()
for idx in range(N):
    if data[idx] not in scoreData:
        scoreData[data[idx]] = idx + 1
result = []
for idx in range(N):
    result.append(scoreData[score[idx]])
print(*result, sep="\n")
