def calc(N):
    result = 1
    for i in range(1, N + 1):
        result *= i
    return result

S = "アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマメミムメモヤユヨラリルレロワヲン"
for i in range(1, int(input())):
    N = calc(i)
    sn = str(N)
    if len(sn) == len(S):
        print(f"{i}! = {N}")
        for k in range(len(sn)):
            print(S[k], end="")
        print()
    elif len(sn) > len(S):
        break
