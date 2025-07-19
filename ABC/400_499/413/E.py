def calc(P, l, r):
    if r - l == 2:
        if P[l] < P[r-1]:
            return [P[l], P[r-1]]
        else:
            return [P[r-1], P[l]]
    data1 = calc(P, l, l + (r - l)//2)
    data2 = calc(P, l + (r - l)//2, r)
    if data1[0] < data2[0]:
        return [data1, data2]
    else:
        return [data2, data1]

RESULT = []
def make_data(data):
    if type(data) is int:
        RESULT.append(data)
        return
    for dat in data:
        make_data(dat)

T = int(input())
for t in range(T):
    N = int(input())
    P = [int(l) for l in input().split()]
    data = calc(P, 0, 2 ** N)
    RESULT = []
    make_data(data)
    print(*RESULT)

