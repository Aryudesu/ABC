RESULT = 0


def calc(x, y, w, h, A, nums):
    if x == w - 1 and y == h - 1:
        global RESULT
        RESULT = RESULT + 1
        return
    if x + 1 < w:
        n = A[y][x + 1]
        if not n in nums:
            nums.add(n)
            calc(x+1, y, w, h, A, nums)
            nums.remove(n)
    if y + 1 < h:
        n = A[y + 1][x]
        if not n in nums:
            nums.add(n)
            calc(x, y+1, w, h, A, nums)
            nums.remove(n)


H, W = [int(l) for l in input().split()]
A = []
for h in range(H):
    A.append([int(l) for l in input().split()])
nums = {A[0][0], }
calc(0, 0, W, H, A, nums)
print(RESULT)
