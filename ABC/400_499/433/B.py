N = int(input())
A = list(map(int, input().split()))
result = []
for i in range(N):
    f = False
    for j in range(i):
        k = i - j - 1
        if A[i] < A[k]:
            result.append(k+1)
            f = True
            break
    if not f:
        result.append(-1)
for r in result:
    print(r)
