N, K = [int(l) for l in input().split()]
A = [int(l) for l in input().split()]
B = [int(l) for l in input().split()]
memo = 0
for i in range(N):
    memo += abs(A[i] - B[i])
print("Yes" if memo <= K and (K - memo)%2 == 0 else "No")
