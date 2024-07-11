N = int(input())
A = [int(l) for l in input().split()]
data = []
for a in A:
    c = 0
    tmp = a
    while True:
        if tmp % 2:
            data.append(c)
            break
        else:
            c += 1
            tmp //= 2
print(sum(data))
