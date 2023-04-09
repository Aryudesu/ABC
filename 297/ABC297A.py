def calc(N, D, T):
    for i in range(N - 1):
        if T[i + 1] - T[i] <= D:
            return T[i+1]
    return -1


N, D = [int(l) for l in input().split()]
T = [int(l) for l in input().split()]
print(calc(N, D, T))
