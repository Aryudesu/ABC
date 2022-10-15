N = int(input())
A = [int(l) for l in input().split()]
A.sort(reverse=True)
c = 0
m = A[0]
tmplist = []
for n in range(N):
    if m > A[n]:
        c += 1
        m = A[n]
    tmplist.append(c)
res = [0] * N
for n in range(N):
    res[tmplist[n]] += 1
for r in res:
    print(r)
