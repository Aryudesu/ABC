from bisect import bisect_left


def calcTousa():
    result = set()
    # 桁
    for h in range(1, 18):
        # 等差
        for i in range(-9, 10):
            # 開始数字
            for j in range(10):
                # 計算
                tmp = j
                res = 0
                for k in range(h + 1):
                    res = res * 10 + tmp
                    if res < 0:
                        break
                    tmp += i
                    if abs(tmp) > 10 or tmp < 0:
                        break
                if res >= 0:
                    result.add(res)
    result_list = list(result)
    result_list.sort()
    # print(result_list)
    return result_list

data = calcTousa()
N = int(input())
idx = bisect_left(data, N)
print(data[idx])
