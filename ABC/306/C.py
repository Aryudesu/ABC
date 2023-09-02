N = int(input())
A = [int(l) for l in input().split()]
data = [0] * (N + 1)
nums = dict()
count = 0
for a in A:
    data[a] += 1
    if data[a] == 2:
        nums[count] = a
        count += 1
# print(nums)
result = []
for i in range(N):
    result.append(nums[i])
print(*result)
