N = int(input())
A = [int(l) for l in input().split()]
l = [0] * 1000000
r = [0] * 1000000
cnt = 0
for i in range(1, N + 1):
    if i == A[i-1]:
        continue
    l[cnt] = i
    r[cnt] = A[i-1]
    if l[cnt] > r[cnt]:
        l[cnt], r[cnt] = r[cnt], l[cnt]
    tmp = A[i - 1]
    A[i - 1] = A[tmp - 1]
    A[tmp - 1] = tmp
    cnt += 1
if cnt >= N:
    raise Exception()
print(cnt)
for i in range(cnt):
    print(l[i], r[i])
print(A)
