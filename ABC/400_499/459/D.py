from typing import Tuple

def calc(S: str)->Tuple[bool, str]:
    data = dict()
    chars = set()
    for s in S:
        data[s] = data.get(s, 0) + 1
        chars.add(s)
    m = 0
    mc = None
    for k in data:
        if m < data[k]:
            m = data[k]
            mc = k
    # 絶対できないパティーン aaabのようなのだとできない
    if 2 * m - 1 > len(S):
        return (False, "")
    # 他のパティーンを考える
    chars.discard(mc)
    idxData = dict()
    sm = 0
    for c in chars:
        if sm > m:
            for i in range(data[c]):
                tmp2 = idxData.get(i, [])
                tmp2.append(c)
                idxData[i] = tmp2
            continue
        tmp = sm + data[c]
        if tmp > m:
            for i in range(data[c]):
                idx = m - data[c] + i
                tmp3 = idxData.get(idx, [])
                tmp3.append(c)
                idxData[idx] = tmp3
        else:
            for i in range(data[c]):
                idx = sm + i
                tmp4 = idxData.get(idx, [])
                tmp4.append(c)
                idxData[idx] = tmp4
        sm += data[c]
    result = []
    for i in range(m):
        result.append(mc)
        crs = idxData.get(i, [])
        for c in crs:
            result.append(c)
    return (True, "".join(result))


T = int(input())
result = []
for _ in range(T):
    S = input()
    res1, res2 = calc(S)
    if res1:
        result.append("Yes")
        result.append(res2)
    else:
        result.append("No")
for r in result:
    print(r)
