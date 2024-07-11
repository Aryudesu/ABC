import bisect

N, M = [int(l) for l in input().split()]
A = [int(l) for l in input().split()]
B = [int(l) for l in input().split()]
A.sort()
B.sort()
ma = A[0]
mi = A[0]

for a in A:
    if ma < a:
        ma = a
    if mi > a:
        mi = a
for b in B:
    if ma < b:
        ma = b
    if mi > b:
        mi = b
while ma > mi + 1:
    # print(ma, mi)
    tmp = (ma + mi) // 2
    Atmp = bisect.bisect_right(A, tmp)
    Btmp = bisect.bisect_left(B, tmp)
    if Atmp >= M - Btmp:
        ma = tmp
    else:
        mi = tmp
# result = ma
# Atmp = bisect.bisect_right(A, ma)
# Btmp = bisect.bisect_left(B, ma)
# print(Atmp, Btmp)
# Atmp = bisect.bisect_right(A, mi)
# Btmp = bisect.bisect_left(B, mi)
# print(Atmp, Btmp)
print(ma)
