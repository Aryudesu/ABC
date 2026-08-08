INF = 10**10
N, M = map(int, input().split())
D = list(map(int, input().split()))
S = list(map(int, input().split()))
data = []
for d in D:
    data.append((d, 0))
for s in S:
    data.append((s, 1))
data.sort()
prevS = -INF
data1 = []
for x, n in data:
    if n == 1:
        prevS = x
    else:
        data1.append(abs(prevS - x))
# print(data)
data.reverse()
prevS = INF
data2 = []
for x, n in data:
    if n == 1:
        prevS = x
    else:
        data2.append(abs(prevS - x))
# print(data)
data2.reverse()
# print(data1, data2)
result = 0
for a, b in zip(data1, data2):
    result += min(a, b)
print(result)
