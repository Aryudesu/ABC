def calc(N, AB):
    s = 0
    for a, b in AB:
        s += b
    if s % 3:
        return -1
    target = s // 3
    return 0

N = int(input())
AB = []
for n in range(N):
    AB.append([int(l) for l in input().split()])
print(calc(N, AB))
