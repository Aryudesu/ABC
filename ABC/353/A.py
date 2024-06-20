def calc(N, H):
    for n in range(N):
        if H[0] < H[n]:
            return n + 1
    return -1

N = int(input())
H = [int(l) for l in input().split()]
print(calc(N, H))
