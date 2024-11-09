N, M = [int(l) for l in input().split()]
A = [int(l) for l in input().split()]
S = []
c = 0
for n in range(N):
    c = (c + A[n]) % M
    S.append(c)
result = 0
for i in range(N):
    result += S[i]
    for j in range(i + 1):
        result += (S[i] - S[j]) % M
print(result)
