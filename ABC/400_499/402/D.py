from collections import defaultdict

N, M = [int(l) for l in input().split()]
data = defaultdict(set)
for m in range(M):
    a, b = [int(l) - 1 for l in input().split()]
    data[(a + b) % N].add((a, b))
dat = []
nums = []
c = 0
for k in data:
    c += len(data[k])
    dat.append(len(data[k]))
    nums.append(c)
nums.reverse()
dat.reverse()
# print(dat)
# print(nums)
result = 0
for i in range(len(nums)):
    result += (nums[i] - dat[i]) * dat[i]
print(result)
