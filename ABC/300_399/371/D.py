import bisect


def calc(data, L, R):
    l = bisect.bisect_left(data, (L, 0))
    r = bisect.bisect_left(data, (R, 0))
    # print("l, r", l, r)
    # LとRが同じ場合
    if L == R:
        # indexがデータの範囲内か
        if l < len(data):
            # そこがちょうど村である場合
            if L == data[l][0]:
                # 一番左の場合は一番左の人数
                if l == 0:
                    return data[l][1]
                # そうでない場合は累積和での計算
                else:
                    return data[l][1] - data[l-1][1]
            else:
                return 0
        # 範囲外
        else:
            return 0
    else:
        if l < len(data):
            l_num = data[l][1]
            if l == 0:
                l_num = 0
            elif data[l][0] < L:
                l_num = data[l][1]
            else:
                l_num = data[l - 1][1]

            if len(data) <= r:
                r = len(data) - 1

            r_num = data[r][1]
            if r == 0:
                if R < data[r][0]:
                    r_num = 0
                else:
                    r_num = data[r][1]
            elif data[r][0] <= R:
                r_num = data[r][1]
            else:
                r_num = data[r - 1][1]
            # print("l_num, r_num", l_num, r_num)
            return r_num - l_num
        else:
            # 範囲外
            return 0

N = int(input())
X = [int(l) for l in input().split()]
P = [int(l) for l in input().split()]

data = []
num = 0
for i in range(N):
    x = X[i]
    num += P[i]
    data.append((x, num))

# print(data)
Q = int(input())
result = []
for q in range(Q):
    L, R = [int(l) for l in input().split()]
    tmp = calc(data, L, R)
    result.append(tmp)
for r in result:
    print(r)
