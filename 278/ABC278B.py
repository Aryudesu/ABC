def is_miss_num(H, M):
    return H >= 0 and H < 24 and M >= 0 and M < 60


def calc(H, M):
    while True:
        H_ = (H // 10) * 10 + M // 10
        M_ = (H % 10) * 10 + M % 10
        if is_miss_num(H_, M_):
            print(H, M)
            return
        M += 1
        if M == 60:
            H += 1
            M = 0
            if H == 24:
                H = 0


H, M = [int(l) for l in input().split()]
calc(H, M)
