from bisect import bisect_right

N, K, M = map(int, input().split())
A = list(map(int, input().split()))
s = 0
data = [0]
for a in A:
    s += a
    data.append(s)
# print(data)
result = 0
for idx1 in range(K, N+1):
    d = data[idx1]
    if M > d:
        continue
    idx2 = bisect_right(data, d - M)
    # print("test", idx2, idx1 - K)
    result += min(idx2, idx1 - K + 1)
print(result)
