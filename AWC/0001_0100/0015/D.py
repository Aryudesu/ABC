N, M, C = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort(reverse=True)
B.sort(reverse=True)
result = 0
bidx = 0
for aidx in range(N):
    a = A[aidx]
    while bidx < M and B[bidx] > a:
        bidx += 1
    if bidx >= M:
        break
    if a >= B[bidx]:
        result += 1
        bidx += 1
print(result*C)
