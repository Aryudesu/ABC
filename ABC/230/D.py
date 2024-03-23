N, D = [int(l) for l in input().split()]
data = []
for n in range(N):
    l, r = [int(l) for l in input().split()]
    data.append((l, 1))
    data.append((r, -1))
data.sort()
# result = 0
# count = 0
# for d in data:
#     if count == 0 and d > 0:
#         result += 1
#     count += d
# print(result)
print(data)
