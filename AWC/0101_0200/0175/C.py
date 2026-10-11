N = int(input())
H = list(map(int, input().split()))
M = H[0]
L = []
result1 = 0
for n in range(N):
    if M > H[n]:
        result1 += abs(H[n] - M)
    L.append(result1)
    M = max(M, H[n])
H.reverse()
R = []
M = H[0]
result2 = 0
for n in range(N):
    if M > H[n]:
        result2 += abs(H[n] - M)
    R.append(result2)
    M = max(M, H[n])
R.reverse()
result = 10 ** 18
result = min(result, R[0])
result = min(result, L[-1])
for n in range(N-1):
    result = min(result, L[n] + R[n+1])
print(L)
print(R)
print(result)
