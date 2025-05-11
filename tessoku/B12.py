N = int(input())
r = float(N)
l = 0.0
for i in range(1000):
    tmp = (l + r) / 2
    if tmp ** 3 + tmp > N:
        r = tmp
    else:
        l = tmp
print(l)
