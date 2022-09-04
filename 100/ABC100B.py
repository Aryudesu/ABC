D, N = [int(l) for l in input().split()]
n = 100 ** D
res = 1
c = 0
while True:
    if res % n == 0:
        if res % (n * 100) != 0:
            c += 1
            if c == N:
                break
    res += 1
print(res)
