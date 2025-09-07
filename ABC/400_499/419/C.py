def ceil_harf(num):
    return num // 2 + num % 2

N = int(input())
rMax = 0
rMin = 10 ** 10
cMax = 0
cMin = 10 ** 10
for n in range(N):
    r, c = [int(l) for l in input().split()]
    rMax = max(rMax, r)
    rMin = min(rMin, r)
    cMax = max(cMax, c)
    cMin = min(cMin, c)
print(max(ceil_harf(rMax - rMin), ceil_harf(cMax - cMin)))
