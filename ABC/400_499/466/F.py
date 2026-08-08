def calc()->int:
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    nums = [X]
    for a in A:
        if not nums:
            nums.append(a)
        else:
            if nums[-1] > a:
                nums.append(a)
    result = 0
    c = 1
    for i in range(1, len(nums)):
        result += (nums[i-1] - 1) // nums[i]
        if i - 2 >= 0:
            result += (nums[i-2] - nums[i-1] - 1) // nums[i]
    return result


T = int(input())
result = []
for _ in range(T):
    result.append(calc())
for r in result:
    print(r)
