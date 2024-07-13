data = dict()
N = int(input())
for n in range(N):
    a, b = [int(l) for l in input().split()]
    data[a] = data.get(a, 0) + 1
    data[a + b] = data.get(a + b, 0) - 1
keys = list(data.keys())
keys.sort()
[0] * N
s = 0
s_data = []
for k in keys:
    tmp = data.get(k, 0)
    s += tmp
    s_data.append(s)
prev = keys[0]
p_sum = s_data[0]
# print("==========")
result = dict()
# print(keys)
# print(s_data)
for idx in range(1, len(s_data)):
    key = keys[idx]
    # print(p_sum, result.get(p_sum, 0), key, prev)
    result[p_sum] = result.get(p_sum, 0) + (key - prev)
    p_sum = s_data[idx]
    prev = key
# print("==========")
# print(result)
res_list = list()
for n in range(1, N+1):
    res_list.append(result.get(n, 0))
print(*res_list)
