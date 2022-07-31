N = int(input())
A = [int(l) for l in input().split()]
same = 0
res = 0
for i in range(N):
    if i + 1 == A[i]:
        res += same
        same += 1
    else:
        if i + 1 <= A[i]:
            j = A[i]
            if i + 1 == A[j - 1]:
                res += 1
print(res)
