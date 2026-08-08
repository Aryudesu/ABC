from bisect import bisect_right

N, K = map(int, input().split())
A = list(map(int, input().split()))
data = []
s = 0
for a in A:
    s += a
    data.append(s)
# print(data)
result = bisect_right(data, K)
for i in range(1, N):
    s = data[i-1]
    idx = bisect_right(data, data[i-1] + K)
    result += idx - i
print(result)
