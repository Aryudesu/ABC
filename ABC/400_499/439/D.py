from bisect import bisect_left, bisect_right

def calc(sevs, fivs, thrs):
    result = 0
    for k in fivs:
        fiv = fivs[k]
        tmp1 = sevs.get(k)
        tmp2 = thrs.get(k)
        if tmp1 is None or tmp2 is None:
            continue
        for f in fiv:
            idx1 = bisect_left(tmp1, f)
            idx2 = bisect_left(tmp2, f)
            result += idx1 * idx2
            idx1 = bisect_right(tmp1, f)
            idx2 = bisect_right(tmp2, f)
            result += (len(tmp1) - idx1) * (len(tmp2) - idx2)
    return result

N = int(input())
A = list(map(int, input().split()))
sevs = dict()
fivs = dict()
thrs = dict()
for i in range(N):
    a = A[i]
    if a % 7 == 0:
        tmp = sevs.get(a//7, [])
        tmp.append(i)
        sevs[a//7] = tmp
    if a % 5 == 0:
        tmp = fivs.get(a//5, [])
        tmp.append(i)
        fivs[a//5] = tmp
    if a % 3 == 0:
        tmp = thrs.get(a//3, [])
        tmp.append(i)
        thrs[a//3] = tmp

print(calc(sevs, fivs, thrs))
