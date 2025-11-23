from collections import defaultdict

N, M = map(int, input().split())

Astr = input().split()
Anum = list(map(int, Astr))
Alen = [len(a) for a in Astr]

data = defaultdict(int)
for idx in range(N):
    a = Anum[idx]
    num = a
    for n in range(12):
        tmp = M - (num % M)
        if tmp == M:
            data[(0, n)] += 1
        else:
            data[(M - (num % M), n)] += 1
        num *= 10
# print(data)
result = 0
for idx in range(N):
    n = Anum[idx] % M
    l = Alen[idx]
    result += data[(n, l)]
print(result)
