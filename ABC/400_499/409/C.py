from collections import defaultdict


def calc(N, L, d):
    if L % 3 != 0:
        return 0
    data = defaultdict(list)
    data[0].append(0)
    pos = 0
    count = 0
    for n in range(N-1):
        pos = (pos + d[n]) % L
        count += 1
        data[pos] .append(count)
    result = 0
    for l in range(L//3):
        a = len(data[l])
        b = len(data[l + L // 3])
        c = len(data[l + 2 * L // 3])
        result += a * b * c
    return result


N, L = [int(l) for l in input().split()]
d = [int(l) for l in input().split()]
print(calc(N, L, d))
