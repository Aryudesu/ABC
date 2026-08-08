N = int(input())
A = list(map(int, input().split()))
idx = 0
for i in range(1, N):
    if A[idx] < A[i]:
        idx = i
if idx == 0:
    print(-1)
else:
    print(idx+1)
