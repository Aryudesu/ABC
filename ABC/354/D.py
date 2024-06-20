A, B, C, D = [int(l) for l in input().split()]
base = 8
if (C - A) % 4 == 0:
    if (D - B) % 2 == 0:
        tmp = (C - A) * (D - B)
        result = tmp
    else:
        tmp1 = (C - A) * (D - B - 1)
        result = tmp1 + (C - A)
elif (C - A) % 4 == 1:
    if (D - B) % 2 == 0:
        tmp1 = (C - A - 1) * (D - B)
        if (A % 4 < 2):
            tmp2 = ((D - B) // 2) * 3
        elif A % 4 == 2 and B % 2 == 1:
            tmp2 = 1
        elif A % 4 == 3 and B % 2 == 0:
            tmp2 = 1
        else:
            tmp2 = 0
        result = tmp1 + tmp2
    else:
        tmp1 = (C - A) * (D - B - 1)
        result = tmp1 + (C - A)
