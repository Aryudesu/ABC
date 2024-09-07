def calc(h, t):
    # 端数除く回数
    count = h // 5
    count *= 3
    # 端数
    new_h = h % 5
    new_t = t
    while new_h > 0:
        new_t = (new_t + 1) % 3
        if new_t % 3 != 0:
            new_h -= 1
        else:
            new_h -= 3
        count += 1
    return count, new_t


N = int(input())
H = [int(l) for l in input().split()]
t = 0
result = 0
for h in H:
    c, t = calc(h, t)
    result += c
print(result)
