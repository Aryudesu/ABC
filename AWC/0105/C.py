N = int(input())
S = input()
XR = 0
for s in S:
    XR ^= ord(s)
XL = 0
result = 0
for idx in range(N-1):
    s = S[idx]
    XL^=ord(s)
    XR^=ord(s)
    nums = []
    for idx2 in range(idx+1):
        nums.append(ord(s)^XR)
    for idx2 in range(idx+1, N):
        nums.append(ord(s)^XL)
    isOk = True
    hosei = 0
    for idx2 in range(N-1, -1, -1):
        if nums[idx2] + hosei > 122:
            isOk = False
            break
        elif nums[idx2] < 97:
            if 97 - nums[idx2] > hosei + 23:
                isOk = False
                break
            hosei = max(97 - nums[idx2], hosei)
            if nums[idx2] + hosei > 122:
                isOk = False
                break
        elif nums[idx2] > 122:
            isOk = False
            break
    if isOk:
        print(nums)
    result += isOk
print(result)
