N, K = map(int, input().split())
tmpTP = list(map(int, input().split()))
TP = []
for k in range(K):
    t, p = tmpTP[2 * k], tmpTP[2 * k + 1]
    TP.append((t, p))
C = list(map(int, input().split()))
sc = sum(C)
maxP = 0
for t, p in TP:
    if t <= sc:
        maxP = p
print(sc - (sc * maxP)//100)
