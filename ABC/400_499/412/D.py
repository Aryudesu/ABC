from itertools import permutations


def calc(N, M, AB):
    if N == 3:
        return 3 - M
    elif N == 4:
        nodes = [3]
    elif N == 5:
        nodes = [4]
    elif N == 6:
        nodes = [2, 5]
    elif N == 7:
        nodes = [2, 3, 6]
    elif N == 8:
        nodes = [2, 3, 4, 7]
    result = 10**10
    # 並び替え全通り
    for data in permutations(range(N)):
        # 切れ目
        for point in nodes:
            AB_tmp = {ab for ab in AB}
            count = 0
            for idx in range(N):
                # 最後のノード
                if idx == N - 1:
                    # 切れ目が一番右端に設定されている時
                    if idx == point:
                        # 存在するノードは残す
                        if (data[0], data[idx]) in AB or (data[idx], data[0]) in AB:
                            AB_tmp.discard((data[0], data[idx]))
                            AB_tmp.discard((data[idx], data[0]))
                        else:
                            # 存在しなければ足す
                            count += 1
                    # 切れ端が真ん中にあるとき
                    else:
                        # 存在するノードは残す
                        if (data[point + 1], data[idx]) in AB or (data[idx], data[point + 1]) in AB:
                            AB_tmp.discard((data[point + 1], data[idx]))
                            AB_tmp.discard((data[idx], data[point + 1]))
                        else:
                            # 存在しなければ足す
                            count += 1
                else:
                    # 真ん中の切れ端
                    if idx == point:
                        # 存在するノードは残す
                        if (data[0], data[idx]) in AB or (data[idx], data[0]) in AB:
                            AB_tmp.discard((data[0], data[idx]))
                            AB_tmp.discard((data[idx], data[0]))
                        else:
                            # 存在しなければ足す
                            count += 1
                    else:
                        # 切れ端でもない場合は隣同士を繋げる
                        if (data[idx], data[idx + 1]) in AB or (data[idx + 1], data[idx]) in AB:
                            AB_tmp.discard((data[idx], data[idx + 1]))
                            AB_tmp.discard((data[idx + 1], data[idx]))
                        else:
                            # 存在しなければ足す
                            count += 1
            result = min(result, count + len(AB_tmp))
    return result

N, M = [int(l) for l in input().split()]
AB = set()
for m in range(M):
    tmp = tuple([int(l) - 1 for l in input().split()])
    AB.add(tmp)
print(calc(N, M, AB))
