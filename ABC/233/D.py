N, K = [int(l) for l in input().split()]
A = [int(l) for l in input().split()]
data = [0]
point = dict()
s = 0
for n in range(N):
    s += A[n]
    data.append(s)
    point[s] = point.get(s, 0) + 1
# print(data)
result = 0
for i in range(N):
    num = K + data[i]
    tmp = point.get(num)
    if not (tmp is None):
        # print(i, num, tmp)
        result += tmp
    point[data[i]] = point.get(data[i], 0) - 1
print(result)
