def calc(N: int, S: str, t: int) -> int:
    target = str(t)
    # 左から右
    lData = []
    rData = []
    ltmp = 0
    rtmp = 0
    lsum = 0
    rsum = 0
    for i in range(N):
        if S[i] == target:
            # 2回ひっくり返す必要があるものは保留
            ltmp += 1
        else:
            lsum += (1 + ltmp * 2)
            ltmp = 0
        lData.append(lsum)
        if S[-i-1] == target:
            # 2回ひっくり返す必要があるものは保留
            rtmp += 1
        else:
            rsum += (1 + rtmp * 2)
            rtmp = 0
        rData.append(rsum)
    rData.reverse()
    result = min(lData[-1], rData[0])
    for i in range(N-1):
        result = min(lData[i] + rData[i+1], result)
    return result




T = int(input())
result = []
for t in range(T):
    N = int(input())
    S = input()
    res = calc(N, S, 0)
    res = min(calc(N, S, 1), res)
    result.append(res)
for r in result:
    print(r)
