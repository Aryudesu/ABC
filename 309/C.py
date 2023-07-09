N, K = [int(l) for l in input().split()]
b_sum = 0
ab = []
for n in range(N):
    a, b = [int(l) for l in input().split()]
    ab.append([a, b])
    b_sum += b
ab.sort()
num = b_sum
if num <= K:
    print(1)
else:
    for dat in ab:
        num -= dat[1]
        if num <= K:
            print(dat[0] + 1)
            break
