Y, M, D = [int(l) for l in input().split("/")]
while True:
    if Y % (M * D) == 0:
        break
    D += 1
    if M == 4 or M == 6 or M == 9 or M == 11:
        if D == 31:
            M += 1
            if M == 13:
                Y += 1
                M = 1
            D = 1
    elif M == 2:
        # 400で割り切れたら絶対閏年
        if Y % 400:
            # 100で割り切れる場合平年
            if Y % 100:
                # 4で割り切れた場合閏年
                if Y % 4:
                    if D == 29:
                        M += 1
                        if M == 13:
                            Y += 1
                            M = 1
                        D = 1
                else:
                    if D == 30:
                        M += 1
                        if M == 13:
                            Y += 1
                            M = 1
                        D = 1
            else:
                if D == 29:
                    M += 1
                    if M == 13:
                        Y += 1
                        M = 1
                    D = 1
        else:
            if D == 30:
                M += 1
                if M == 13:
                    Y += 1
                    M = 1
                D = 1
    else:
        if D == 32:
            M += 1
            if M == 13:
                Y += 1
                M = 1
            D = 1
res = str(Y) + "/"
if M < 10:
    res += "0"
res += str(M)
res += "/"
if D < 10:
    res += "0"
res += str(D)
print(res)
