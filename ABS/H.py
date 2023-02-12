def calc(N, Y):
    for a in range(N + 1):
        for b in range(N + 1 - a):
            if a * 10000 + b * 5000 + (N - a - b) * 1000 == Y:
                print(a, b, N - a - b)
                return
    print(-1, -1, -1)


N, Y = [int(l) for l in input().split()]
calc(N, Y)
