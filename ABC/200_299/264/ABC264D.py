S = input()
d = {'a': 0, 't': 1, 'c': 2, 'o':3, 'd': 4, 'e':5, 'r':6}
nums = []
for s in S:
    nums.append(d[s])
c = 0
while True:
    n = 0
    while n < 6:
        if nums[n] > nums[n+1]:
            nums[n], nums[n+1] = nums[n+1], nums[n]
            c += 1
        n += 1
    f = True
    for m in range(6):
        if nums[m] > nums[m+1]:
            f = False
    if f:
        break
print(c)
