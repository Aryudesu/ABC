N = int(input())
rNum = 0
wNum = 0
qNum = 0
for n in range(N):
    S = input()
    if S == "R":
        rNum += 1
    elif S == "W":
        wNum += 1
    elif S == "?":
        qNum += 1
    else:
        raise ValueError()
if abs(rNum - wNum) < qNum:
    d = abs(rNum - wNum)
    print((qNum - d) % 2)
else:
    m, M = min(rNum, wNum) + qNum, max(rNum, wNum)
    print(M - m)
