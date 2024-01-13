N = int(input())
pos = []
for n in range(N):
    x, y = [int(l) for l in input().split()]
    pos.append((x, y))
result = 10 ** 15
for n in range(N - 1):
    ax, ay = pos[n]
    for m in range(n + 1, N):
        bx, by = pos[m]
        tmp = (ax - bx) ** 2 + (ay - by) ** 2
        if result > tmp:
            result = tmp
print(result ** 0.5)
