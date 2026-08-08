N, M, A = map(int, input().split())
H = list(map(int, input().split()))
battery = M
result = 0
isOk = True
for h in H:
    if battery == 0:
        isOk = False
        break
    if h <= A:
        continue
    if h > battery:
        isOk = False
        break
    battery //= 2
    result += 1
print(result if isOk else -1)
