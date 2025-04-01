from math import isqrt


def calc(N):
    i = 1
    while i * i <= N // i:
        if N % i == 0:
            d = i
            m = N // d
            if d * d > m:
                break
            tmp = 9 * d * d - 12 * (d * d - m)
            if tmp < 0:
                continue
            sq = isqrt(tmp)
            if sq * sq == tmp:
                if (-3 * d + sq) % 6 == 0:
                    y = (-3 * d + sq) // 6
                    if y > 0 and y + d > 0:
                        return f"{y + d} {y}"
        i += 1
    return "-1"

N = int(input())
print(calc(N))
