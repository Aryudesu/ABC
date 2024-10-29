N = int(input())
A = [int(l) for l in input().split()]
B = [int(l) for l in input().split()]
A.sort(reverse=True)
B.sort(reverse=True)
j = 0
result = []
for i in range(N):
    if j >= N - 1:
        result.append(A[i])
        break
    if A[i] <= B[j]:
        j += 1
    else:
        result.append(A[i])
if len(result) > 1:
    print(-1)
else:
    print(result[0])
