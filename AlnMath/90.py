def checkData(num: int, target: int) -> bool:
    result = 1
    while num:
        result *= num % 10
        num //= 10
    return result == target


def calc(N, B):
    if N < B:
        return 0
    result = 0    
    if checkData(B, 0):
        result += 1
    a = 1
    while a <= N:
        b = a
        while b <= N:
            c = b
            while c <= N:
                d = c
                while d <= N:
                    p = d
                    if B + p <= N and checkData(B + p, p):
                        result += 1
                    d *= 7
                c *= 5
            b *= 3
        a *= 2
    return result


N, B = [int(l) for l in input().split()]
print(calc(N, B))
