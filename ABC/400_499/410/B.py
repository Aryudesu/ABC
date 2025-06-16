from sortedcontainers import SortedList

N, Q = [int(l) for l in input().split()]
X = [int(l) for l in input().split()]
result = []
data = [0] * N
for x in X:
    if x != 0:
        result.append(x)
        data[x-1] += 1
    else:
        idx = 0
        for i in range(N):
            if data[i] < data[idx]:
                idx = i
        data[idx] += 1
        result.append(idx+1)
print(*result)
