from collections import defaultdict

N, M = map(int, input().split())
acData = set()
waData = defaultdict(int)
for m in range(M):
    p, s = input().split()
    p = int(p)
    if s == "AC":
        acData.add(p)
    else:
        if not p in acData:
            waData[p] += 1
ac = 0
wa = 0
for key in acData:
    ac += 1
    wa += waData[key]
print(ac, wa)
