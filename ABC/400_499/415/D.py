N, M = [int(l) for l in input().split()]
AB = []
for m in range(M):
    a, b = [int(l) for l in input().split()]
    AB.append([a-b, a, b])
AB.sort()
result = 0
num = N
for n, a, b in AB:
    x = max(0, (num-a)//n + 1)
    result += x
    num -= n * x
print(result)
