N = int(input())
S = [int(l) for l in input()]
W = [int(l) for l in input().split()]
otona = 0
kodomo = 0
for w in W:
    if w == 0:
        kodomo += 1
    else:
        otona += 1

data = []
for n in range(N):
    data.append((W[n], S[n]))
data.sort()
sotona = otona
skodomo = 0
result = otona
for dat in data:
    w, s = dat
    if s == 0:
        skodomo += 1
        sotona -= 1
        tmp = skodomo + sotona
