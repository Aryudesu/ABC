def calc(N):
    num = N
    one_1 = -1
    one_2 = -1
    one_3 = -1
    d = 1
    if N < 7:
        return -1
    while num:
        t = num % 2
        num //= 2
        if t:
            one_3 = one_2
            one_2 = one_1
            one_1 = d
        d *= 2
    if one_1 != -1 and one_2 != -1 and one_3 != -1:
        pass
    elif one_1 != -1 and one_2 != -1 and one_3 == -1:
        one_2 //= 2
        one_3 = one_2//2
        if one_3 == 0:
            one_1 //= 2
            one_2 = one_1 // 2
            one_3 = one_2 // 2
    elif one_1 != -1 and one_2 == -1 and one_3 == -1:
        one_1 //= 2
        one_2 = one_1 // 2
        one_3 = one_2 // 2
    return one_1 + one_2 + one_3


T = int(input())
for t in range(T):
    num = int(input())
    print(calc(num))
