def int_root(num):
    lr = -1
    rr = num
    while rr - lr > 1:
        tmp = lr + (rr - lr) // 2
        if tmp * tmp > num:
            rr = tmp
        else:
            lr = tmp
    return rr if rr * rr == num else lr


N = int(input())
print(int_root(N))
