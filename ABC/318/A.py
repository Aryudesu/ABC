N, M, P = [int(l) for l in input().split()]
count = 0
day = M
while day <= N:
    day += P
    count += 1
print(count)
