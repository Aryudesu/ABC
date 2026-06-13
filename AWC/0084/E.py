from itertools import permutations

def calcMax(N: int, K: int, L: int, ar: list[int], B: list[int], T: list[int], A: list[int])->int:
    result = 0
    Sn = list(range(K))
    data = dict()
    for n in range(N):
        t = T[ar[n]]
        d = []
        isOk = True
        for l in range(L):
            if B[l] == 1:
                d.append(t[l])
            elif B[l] == t[l]:
                d.append(t[l])
            else:
                isOk = False
                break
        result += 1
        nextB = []
        for k in range(K):
            s = Sn[k]
        if not isOk:
            tmp = tuple(d)
            data[tmp] = data.get(tmp, 0) + 1



N, K, L = map(int, input().split())
B = list(map(int, input().split()))
T = []
A = []
for n in range(N):
    t = list(map(int, input().split()))
    a = list(map(int, input().split()))
    T.append(t)
    A.append(a)

for dat in permutations(range(N)):
    print(dat)
