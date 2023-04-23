def calc1(N, T, C, R):
    result = None
    for i in range(N):
        if C[i] == T:
            if result is None:
                result = i
                continue
            if R[result] < R[i]:
                result = i
    return result


def calc2(N, T, C, R):
    p1c = C[0]
    result = 0
    for i in range(N):
        if C[i] == p1c:
            if R[result] < R[i]:
                result = i
    return result


def calc(N, T, C, R):
    result = calc1(N, T, C, R)
    if not result is None:
        return result + 1
    return calc2(N, T, C, R) + 1


N, T = [int(l) for l in input().split()]
C = [int(l) for l in input().split()]
R = [int(l) for l in input().split()]
print(calc(N, T, C, R))
