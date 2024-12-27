N = int(input())
A = [int(l) for l in input().split()]
layer = []
lsum = [0]
max_depth = 0
for a in A:
    tmp = [a]
    num = a
    lsum[0] += a
    depth = 1
    while num:
        if num % 2 == 0:
            num //= 2
            depth += 1
            if depth > max_depth:
                lsum.append(0)
            lsum[depth-1] += num
        else:
            break
        tmp.append(num)
    max_depth = max([max_depth, depth])
    if len(lsum) < max_depth:
        while len(lsum) >= max_depth:
            lsum.append(0)
    layer.append(tmp)
print(layer)
print(lsum)
