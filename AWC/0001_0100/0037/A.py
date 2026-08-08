N = int(input())
A = list(map(int, input().split()))
idx = 0
c = 0
for i in range(N):
    a = A[i]
    if A[idx] < a:
        idx = i
        c = 1
    elif A[idx] == a:
        c += 1
print(A[idx] if c == 1 else 0)
