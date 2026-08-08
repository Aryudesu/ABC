from collections import deque

N = int(input())
A = list(map(int, input().split()))
A.sort()
result = deque()
l = 0
r = N-1
result.append(A[l])
l += 1
maxF = 1
while r - l >= 0:
    if maxF > 0:
        tmp = A[r]
        p1 = result.pop()
        result.append(p1)
        p2 = result.popleft()
        result.appendleft(p2)
        if abs(p1 - tmp) > abs(p2 - tmp):
            result.append(tmp)
        else:
            result.appendleft(tmp)
        r -= 1
        maxF += 1
        if maxF == 3:
            maxF = -1
    else:
        tmp = A[l]
        p1 = result.pop()
        result.append(p1)
        p2 = result.popleft()
        result.appendleft(p2)
        if abs(p1 - tmp) > abs(p2 - tmp):
            result.append(tmp)
        else:
            result.appendleft(tmp)
        l += 1
        maxF -= 1
        if maxF == -3:
            maxF = 1
# print(result)
prev = result.popleft()
res = 0
while result:
    tmp = result.popleft()
    res += abs(tmp - prev)
    prev = tmp

result = deque()
l = 0
r = N-1
result.append(A[r])
r -= 1
maxF = -1
while r - l >= 0:
    if maxF > 0:
        tmp = A[r]
        p1 = result.pop()
        result.append(p1)
        p2 = result.popleft()
        result.appendleft(p2)
        if abs(p1 - tmp) > abs(p2 - tmp):
            result.append(tmp)
        else:
            result.appendleft(tmp)
        r -= 1
        maxF += 1
        if maxF == 3:
            maxF = -1
    else:
        tmp = A[l]
        p1 = result.pop()
        result.append(p1)
        p2 = result.popleft()
        result.appendleft(p2)
        if abs(p1 - tmp) > abs(p2 - tmp):
            result.append(tmp)
        else:
            result.appendleft(tmp)
        l += 1
        maxF -= 1
        if maxF == -3:
            maxF = 1
# print(result)
prev = result.popleft()
res2 = 0
while result:
    tmp = result.popleft()
    res2 += abs(tmp - prev)
    prev = tmp
print(max(res, res2))
