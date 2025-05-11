def calc(N, M):
    result = 0
    inf = 10 ** 9
    for i in range(M + 1):
        result += pow(N, i)
        if result > inf:
            return "inf"
    return str(result)

N, M = [int(l) for l in input().split()]
print(calc(N, M))
