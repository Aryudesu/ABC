N, P = map(int, input().split())
data = []
for n in range(N):
    h, g = map(int, input().split())
    data.append((P-h)//g)
data.sort()
isOk = True
for idx in range(N):
    if idx > data[idx]:
        isOk = False
        break
print("Yes" if isOk else "No")
