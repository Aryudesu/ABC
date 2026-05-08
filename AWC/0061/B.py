N = int(input())
S = list(map(int, input().split()))
if N > 1:
    C = list(map(int, input().split()))
score = S[0]
result = score
for i in range(N-1):
    score += S[i+1] - C[i]
    result = max(result, score)
print(result)
