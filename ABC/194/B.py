N = int(input())
AB = []
for n in range(N):
    a, b = [int(l) for l in input().split()]
    AB.append([a, b])
result = 10**8
for n in range(N):
    for m in range(N):
        tmp = 0
        if n != m:
            tmp = max([AB[n][0], AB[m][1]])
        else:
            tmp = AB[n][0] + AB[m][1]
        if result > tmp:
            result = tmp
print(result)
