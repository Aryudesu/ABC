def calc(N, S):
    if N == 3:
        if S == "101":
            return 1
        elif S == "000":
            return 0
        else:
            return -1
    count = 0
    for s in S:
        if s == "1":
            count += 1
    # 4枚以上で表が2枚のみで隣り合ってる場合
    if count == 2:
        if "11" in S:
            if S == "0110":
                return 3
            else:
                return 2
    # 奇数なら駄目
    if count % 2 == 1:
        return -1
    return count // 2


T = int(input())
result = []
for t in range(T):
    N = int(input())
    S = input()
    result.append(calc(N, S))
for r in result:
    print(r)
