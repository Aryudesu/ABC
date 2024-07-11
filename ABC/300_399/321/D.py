# Arr[a] <= Numになる最大のaの検索
def searchIdx(Arr, Num, _r):
    r = _r
    l = 0
    while True:
        tmp = (r + l) // 2
        if Arr[tmp] > Num:
            r = tmp
        else:
            l = tmp
        if l == r or l + 1 == r:
            break
    if Arr[r] <= Num:
        return r
    return l if Arr[l] <= Num else -1


N, M, P = [int(l) for l in input().split()]
A = [int(l) for l in input().split()]
B = [int(l) for l in input().split()]
A.sort()
B.sort()
Bsum = []
s = 0
for b in B:
    s += b
    Bsum.append(s)
nr = M - 1
result = 0
for a in A:
    if nr >= 0:
        nr = searchIdx(B, P - a, nr)
    if nr >= 0:
        if nr != M:
            result += Bsum[nr] + a * (nr + 1) + P * (M - 1 - nr)
        else:
            result += Bsum[nr] + a * (nr + 1)
    else:
        result += P * M
print(result)
