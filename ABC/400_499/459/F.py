N = int(input())
A = list(map(int, input().split()))
renbanIdx = [0]
result = 0
for i in range(1, N):
    if A[i-1] >= A[i]:
        pass
