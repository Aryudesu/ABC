N, Q = [int(l) for l in input().split()]
X = [int(l) for l in input().split()]
nums = [0] * N
countNums = []
r = 0
setData = set()
# timing[num] = count
timing = dict()
c = 0
count = 0
for idx in range(Q):
    x = X[idx]
    if not x in setData:
        setData.add(x)
        timing[x] = idx
    else:
        setData.remove(x)
        t = timing[x]
        nums[x - 1] += r - countNums[t]
    r += len(setData)
    countNums.append(r)
    print(x, r, setData, nums, countNums, timing)
for sd in setData:
    x = sd
    t = timing[x]
    nums[x - 1] += r - countNums[t]
    print(x, r, setData, nums, countNums, timing)
print(*nums)
