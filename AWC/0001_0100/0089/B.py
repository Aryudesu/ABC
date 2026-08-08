N, D, K, C = map(int, input().split())
data = []
for n in range(N):
    a, b = map(int, input().split())
    if b == 1:
        data.append(max(a-C,0))
    else:
        data.append(a)
data.sort()
s = data.pop()
while data:
    d = data.pop()
    if d - K > 0:
        s += d - K
    else:
        break
if s >= D:
    print(s)
else:
    print(-1)
