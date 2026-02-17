from heapq import heappop, heappush

H, W, N = map(int, input().split())
HW = []
WH = []
for n in range(N):
    h, w = map(int, input().split())
    heappush(HW, (-h, -w, n))
    heappush(WH, (-w, -h, n))
ignoreHW = dict()
ignoreWH = dict()
result = [[None, None] for _ in range(N)]
lu = [0, 0]
while HW and WH:
    if len(HW) > 0:
        hw_h, hw_w, hw_n = HW[0]
        tmp1 = (hw_h, hw_w)
        if not ignoreHW.get(tmp1) is None:
            if ignoreHW[tmp1] > 0:
                heappop(HW)
                ignoreHW[tmp1] -= 1
                continue
        if -hw_h == H:
            heappop(HW)
            ignoreWH[tmp1] = ignoreWH.get(tmp1, 0) + 1
            result[hw_n] = [lu[0] + 1, lu[1] + 1]
            lu = [lu[0], lu[1]-hw_w]
            W += hw_w
            continue
    if len(WH) > 0:
        wh_w, wh_h, wh_n = WH[0]
        tmp2 = (wh_h, wh_w)
        if not ignoreWH.get(tmp2) is None:
            if ignoreWH[tmp2] > 0:
                heappop(WH)
                ignoreWH[tmp2] -= 1
                continue
        if -wh_w == W:
            heappop(WH)
            ignoreHW[tmp2] = ignoreHW.get(tmp2, 0) + 1
            result[wh_n] = [lu[0] + 1, lu[1] + 1]
            lu = [lu[0]-wh_h, lu[1]]
            H += wh_h
            continue
#     print(H, W)
#     print(HW, WH)
#     print(ignoreHW, ignoreWH)
# print("======")
for r in result:
    print(*r)
