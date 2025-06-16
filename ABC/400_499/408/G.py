def calc(A, B, C):
    left = 0
    right = 10 ** 36 + 1
    while right - left > 1:
        mid = left + (right - left)//2
        y = ((A * mid) // B + 1) * B
        if y < C * mid:
            right = mid
        else:
            left = mid
    return left

T = int(input())
result = []
for t in range(T):
    A, B, C, D = [int(l) for l in input().split()]
    res = calc(A * D, B * D, C * B)
    result.append(res)
for r in result:
    print(r)
