N, W = [int(l) for l in input().split()]
WVData = []
VData = []
for n in range(N):
    w, v = [int(l) for l in input().split()]
    if len(VData) > 0:
        VData.append(VData[-1] + (v * v)//4)
    else:
        VData.append((v * v)//4)
    WVData.append([w, v])
# print(VData)
dp = {0: 0}
result = 0
for n in range(N):
    w, v = WVData[n]
    new_dp = dict()
    for i in range(v//2 + 1):
        dv = VData[-1] - VData[n-1] if n > 0 else VData[-1]
        for now_w in dp:
            now_v = dp.get(now_w)
            if result - dv > now_v:
                continue
            new_w = now_w + w * i
            if new_w > W:
                continue
            new_v = now_v + (v * i - i * i)
            next_v = max([new_dp.get(new_w, 0), new_v])
            result = max([result, next_v])
            new_dp[new_w] = next_v
    dp = new_dp
print(result)
