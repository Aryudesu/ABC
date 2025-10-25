from bisect import bisect_right

def calc(N, K, data):
    result = 0
    for i in range(N):
        d = data[i]
        idx = bisect_right(data, d + K)
        # print(d, idx)
        result += idx - i - 1
    return result

N, K = [int(l) for l in input().split()]
A = [int(l) for l in input().split()]
data = [0]
s = 0
for a in A:
    s += a
    data.append(s)
# print(data)
print(calc(N, K, data))
