for t in range(int(input())):
    a, b, c = [int(l) for l in input().split()]
    print(min(a, c, (a + b + c) // 3))
