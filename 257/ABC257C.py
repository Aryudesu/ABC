def abs(n):
    return n if n >= 0 else -n

N = int(input())
S = input()
W = [int(l) for l in input().split()]
CNum = 0
ANum = 0
Data = dict()
for n in range(N):
    s = int(S[n])
    DIdx = str(W[n])
    dat = Data.setdefault(DIdx, [0, 0])
    if s:
        ANum += 1
        dat[1] += 1
    else:
        CNum += 1
        dat[0] += 1

W.sort()
C_ = 0
A_ = 0
minR = 2 * (10 ** 5)

r = abs(CNum) + abs(N - ANum)
if r < minR:
    minR = r

for idx in range(N):
    DIdx = str(W[idx])
    if idx < N - 1:
        if W[idx] == W[idx + 1]:
            continue
    A_ += Data[DIdx][1]
    C_ += Data[DIdx][0]
    CN = idx
    AN = N - idx
    r = abs(CN - C_) + abs(AN - A_)
    if r < minR:
        minR = r
r = abs(N - CNum) + abs(ANum)
if r < minR:
    minR = r
print(N - minR)
