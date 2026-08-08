N = int(input())
result = []
for n in range(N):
    l, t = map(int, input().split())
    res = l // t
    if l % t > 0 and l % t >= t//2:
        res += 1
    result.append(res)
for r in result:
    print(r)
