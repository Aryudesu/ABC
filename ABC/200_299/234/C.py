def calc2(N):
    tmpN = N
    result = []
    while tmpN:
        result.append(str((tmpN % 2) * 2))
        tmpN //= 2
    result.reverse()
    return result


K = int(input())
res = calc2(K)
print("".join(res))
