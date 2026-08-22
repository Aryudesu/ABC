N, K = map(int, input().split())
data = []
for _ in range(N):
    S = input()
    n = int(S)
    num = 10 ** (10 - len(S)) * n
    hZero = 0
    for s in S:
        if s == "0":
            hZero += 1
        else:
            break
    data.append((len(S), num, S))
data.sort(reverse=True)
headIndex = 0
for n in range(N):
    l, num, S = data[n]
    if num != 0 and n >= K-1:
        headIndex = n
        break
result = []
result.append(data[headIndex][2])
newData = []
for n in range(N):
    l, num, S = data[n]
    if headIndex == n:
        continue
    newData.append((num, S))
newData.sort(reverse=True)
data = newData
count = 1
for n in range(N):
    if n != headIndex:
        result.append(data[n][1])
        count += 1
    if count == K:
        break
result[0] = str(int(result[0]))
print("".join(result))
