N, M, K = map(int, input().split())
S = list(map(int, input().split()))
R = list(map(int, input().split()))
S.sort()
R.sort(reverse=True)
for _ in range(K):
    S.pop()
S.reverse()
idx = 0
result = 0
for m in range(M):
    if len(S) <= idx:
        break
    if R[m] <= S[idx]:
        idx += 1
        result += 1
print(result)
