N, M = map(int, input().split())
data = []
for m in range(M):
    l, r = map(int, input().split())
    data.append((l, -1))
    data.append((r+1, 1))
data.sort()
if M > 0:
    result = 0
    num = 0
    prev = 1
    rain = 0
    if N < data[0][0]:
        print(N)
        exit(0)
    if data[0][0] == 1:
        prev = 1
        rain = -1
    else:
        prev = data[0][0]
        num = data[0][0] - 1
        rain = -1
    for idx in range(1, 2 * M):
        d, f = data[idx]
        # 雨が降っていない場合
        if rain == 0:
            n = (d - prev)
            if num + n >= N:
                result = prev
                result += N - num - 1
                num = N + 1
                break
            num += n
        prev = d
        rain += f
    if num <= N:
        result = data[-1][0] + (N - num - 1)
    print(result)
else:
    print(N)
