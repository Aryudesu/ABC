N, M, K = map(int, input().split())
result = 0
for n in range(N):
    S = list(map(int, input().split()))
    S.sort()
    SSum = sum(S)
    score = (SSum-S[0]-S[-1])//(M-2) if M >= 3 else SSum // M
    if score < K:
        result += 1
print(result)
