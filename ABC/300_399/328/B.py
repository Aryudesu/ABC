def isZorome(m, d):
    s = str(m) + str(d)
    c = str(m)[0]
    t = s.replace(c, "")
    return len(t) == 0


def calc(N, D):
    result = 0
    m, d = 1, 1
    while m <= N:
        if isZorome(m, d):
            result += 1
        d += 1
        if D[m-1] < d:
            d = 1
            m += 1
    return result


N = int(input())
D = [int(l) for l in input().split()]
print(calc(N, D))
