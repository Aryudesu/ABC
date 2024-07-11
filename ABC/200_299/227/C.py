def cube_root(num):
    l = -1
    r = num + 1
    while r - l > 1:
        mid = (r + l)//2
        if mid ** 3 > num:
            r = mid
        else:
            l = mid
    return l

N = int(input())
cr = cube_root(N)
result = 0
for c in range(cr, N + 1):
    tmp_c = N // c
    cr_ab = cube_root(tmp_c)
    for b in range(cr_ab, cr):
        tmp_bc = b * c
        tmp = N // tmp_bc
        result += tmp
print(result)
