from sortedcontainers import SortedList

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
lastB = B[-1]
A.sort(reverse=True)
B.sort(reverse=True)
maxA = A[0]

data = [None] * N
Aset = SortedList(A)
idx = 0
result = 0
for m in range(N):
    if N <= idx:
        break
    if B[m] < A[idx]:
        data[m] = A[idx]
        Aset.discard(A[idx])
        idx += 1
        result += 1
A.reverse()
B.reverse()
data.reverse()
nowA = None
tmpRes = -1
chikan = False
chikanB = 10 ** 18
lastIdx = -1
for idx in range(N):
    if B[idx] == lastB and data[idx] is not None:
            if nowA is None:
                nowA = data[idx]
            else:
                nowA = max(nowA, data[idx])
            tmpRes = max(data[idx] - lastB, tmpRes)
            lastIdx = max(idx, lastIdx)
    elif B[idx] <= lastB and data[idx] is None:
        # 下位に今のAを持っていって上位のAを引っ張ってきたい
        chikan = True
        chikanB = min(chikanB, B[idx])
# print(A)
# print(B)
# print(data)

if nowA is None:
    if maxA > lastB:
        print(result, maxA - lastB)
    else:
        res = 0
        for idx in range(lastIdx):
            tmp = data[idx]
            if tmp is None:
                continue
            res = max(res, tmp)
        if res - lastB > Aset[-1] - lastB:
            print(result, res - lastB)
        else:
            print(result, Aset[-1] - lastB)
else:
    if chikan:
        print(result, maxA - lastB)
    else:
        if lastIdx == N-1:
            pass
        else:
            print(tmpRes)
