def calc(N, H):
    for i in range(N - 1):
        if H[i] >= H[i + 1]:
            return H[i]
    return H[-1]

N = int(input())
H = [int(l) for l in input().split()]
print(calc(N, H))
