U = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
L = "abcdefghijklmnopqrstuvwxyz"
# 大 -> 小
UL = dict()
# 小 -> 大
LU = dict()
for i in range(len(U)):
    UL[U[i]] = L[i]
    LU[L[i]] = U[i]
N = int(input())
S = list(input())
Q = int(input())
data = set()
LorU = 0
for q in range(Q):
    t, x, c = [l for l in input().split()]
    if t == "1":
        S[int(x)-1] = c
        data.add(int(x)-1)
    elif t == "2":
        LorU = -1
        data = set()
    elif t == "3":
        LorU = 1
        data = set()
# print(S)
result = []
for n in range(N):
    s = S[n]
    if LorU == 0:
        result.append(s)
    elif LorU == 1:
        if n not in data:
            result.append(LU.get(s, s))
        else:
            result.append(s)
    elif LorU == -1:
        if n not in data:
            result.append(UL.get(s, s))
        else:
            result.append(s)
print("".join(result))
