N = int(input())
data = []
signal = []
pos = set()
for n in range(N):
    x, l, r, c = map(int, input().split())
    signal.append((x-l, c))
    signal.append((x+r+1, -c))
    pos.add(x-l)
    pos.add(x+r)
    pos.add(x+r+1)
signal.sort()
pos = sorted(pos)
posIdx = dict()
for i in range(len(pos)):
    posIdx[pos[i]] = i
imos = [0] * (len(pos) + 1)
for p, c in signal:
    idx = posIdx[p]
    imos[idx] += c
s = 0
for idx in range(len(pos)):
    s += imos[idx]
    imos[idx] = s
print(max(imos))
