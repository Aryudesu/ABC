S = input()
data = dict()
for i in range(len(S)):
    tmp = data.get(S[i], list())
    tmp.append(i)
    data[S[i]] = tmp
result = 0
for k in data:
    nums = data.get(k, [])
    if len(nums) < 2:
        continue
    N = len(nums)
    cs = nums[-1]
    for i in range(N - 2, -1, -1):
        result += cs - (nums[i] + 1) * (N - i - 1)
        cs += nums[i]
    #     print("debug", i, cs, result)
    # print("result:", result)
print(result)
