from bisect import bisect_right

N, M, K = map(int, input().split())
X, Y = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()
B.sort()
aData = [0]
s = 0
for a in A:
    s += a
    aData.append(s)
bData = [0]
bShihei = [0]
s = 0
for b in B:
    s += b
    bData.append(s)
s = 0
for b in B:
    s += (b + K - 1)//K
    if s > Y:
        break
    bShihei.append(s)
allNum = X + Y * K

result = 0
for bIdx in range(len(bShihei)):
    aNum = allNum - bData[bIdx]
    aIdx = bisect_right(aData, aNum)
    result = max(aIdx + bIdx - 1, result)
print(result)
