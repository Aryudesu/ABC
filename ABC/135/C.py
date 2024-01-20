N = int(input())
A = [int(l) for l in input().split()]
B = [int(l) for l in input().split()]
result = 0
for i in range(N):
    if A[i] < B[i]:
        result += A[i]
        tmp = B[i] - A[i]
        if A[i + 1] > tmp:
            result += tmp
            A[i + 1] -= tmp
        elif A[i + 1] == tmp:
            result += tmp
            A[i + 1] = 0
        else:
            result += A[i + 1]
            A[i + 1] = 0
    elif A[i] == B[i]:
        result += A[i]
    else:
        result += B[i]
print(result)
