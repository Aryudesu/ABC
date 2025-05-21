def calc(A, B, K):
    co = 0
    num = A
    while True:
        if num >= B:
            return co
        num *= K
        co += 1


A, B, K = [int(l) for l in input().split()]
print(calc(A, B, K))
