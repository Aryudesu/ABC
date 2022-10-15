X, K = [int(l) for l in input().split()]
base = 1
x = X
for k in range(K):
    tmp = x // base
    t = tmp % 10
    if t >= 5:
        x = (tmp//10 + 1)*10 * base
    else:
        x = (tmp//10) * 10 * base
    base *= 10
print(x)
