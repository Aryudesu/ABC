data_max = 2 * (10**5)
data = [0] * (data_max + 2)
N = int(input())
for _ in range(N):
    l, r = [int(l) for l in input().split()]
    data[l] += 1
    data[r] -= 1

result = []
prev = 0
s = 0
for idx in range(data_max + 2):
    s += data[idx]
    if s >= 1 and prev == 0:
        result.append([idx])
    elif s == 0 and prev > 0:
        result[-1].append(idx)
    prev = s
for r in result:
    print(*r)
