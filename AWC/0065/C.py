N = int(input())
A = list(map(int, input().split()))
dat1 = A[0]
dat2 = 0
for i in range(1, N):
    dat1, dat2 = max(dat1, dat2 + A[i]), max(dat1, dat2)
print(max(dat1, dat2))
