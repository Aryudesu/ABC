N = int(input())
XP = []
for n in range(N):
    x, p = map(int, input().split())
    XP.append((abs(x), p))
XP.sort(reverse=True)
result = 0
s = 0
for r in range(101):
    if not XP:
        break
    while XP:
        if XP[-1][0] == r:
            x, p = XP.pop()
            s += p
        else:
            break
    result = max(result, s - r*r)
print(result)
