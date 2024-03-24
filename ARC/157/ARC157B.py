def calc(N, K, S):
    x_data = [-1]
    y_data = [-1]
    x_count = 0
    y_count = 0
    # Xの位置を保存しておく
    for idx in range(N):
        if S[idx] == "X":
            x_data.append(idx)
            x_count += 1
        else:
            y_data.append(idx)
            y_count += 1
    x_data.append(N)
    y_data.append(N)
    # もともと全部Yだった場合
    if x_count == 0:
        # 全部ひっくり返す必要があったとき
        if N == K:
            return 0
        # 端のK個をXにする
        return N - K - 1
    # Xの数がK個だった場合:
    if x_count == K:
        return N - 1
    # Xの数がKよりも多い場合、Yの連続個数が最大となる数を探索
    if x_count > K:
        result = 0
        for idx in range(x_count + 1 - K):
            tmp = x_data[idx + K + 1] - x_data[idx] - 1
            if result < tmp:
                result = tmp
        if result == 0:
            return 0
        return result - 1
    # Xの数がKよりも少ない場合、YとXを逆転して同様に考える
    # print(y_data)
    L = y_count - K + x_count
    # print("L", L)
    if x_count < K:
        result = 0
        for idx in range(y_count + 2 - L):
            if idx == 1 and idx + L == y_count:
                continue
            # print(idx+L, idx)
            tmp = y_data[idx + L] - y_data[idx]
            if result < tmp:
                result = tmp
        if result == 0:
            return 0
        return result
    raise Exception()


N, K = [int(l) for l in input().split()]
S = input()
print(calc(N, K, S))
