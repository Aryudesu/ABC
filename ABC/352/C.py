N = int(input())
AB = []
sumA = 0
for n in range(N):
    a, b = [int(l) for l in input().split()]
    sumA += a
    AB.append([a, b])
result = sumA
for a, b in AB:
    tmp = sumA - a + b
    if result < tmp:
        result = tmp
print(result)
