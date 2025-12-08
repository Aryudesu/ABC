N = int(input())
A = list(map(int, input().split()))
count = 0
for l in range(N-1):
    for r in range(l+1, N):
        tmp = 0
        for h in range(l,r+1):
            tmp += A[h]
        f = True
        for i in range(l, r + 1):
            if tmp % A[i] == 0:
                f = False
                break
        if f:
            count += 1
print(count)
