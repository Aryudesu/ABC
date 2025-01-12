def calc(K, S, T):
    nodes = set()
    if len(S) > len(T):
        S, T = T, S
    INF = len(T) * 2
    # SとTの文字，操作回数
    tmp = tuple([0, 0, 0])
    nodes.add(tmp)
    memo = dict()
    while nodes:
        new_nodes = set()
        for sidx, tidx, count in nodes:
            if sidx < len(S) and tidx < len(T):
                if S[sidx] == T[tidx]:
                    tmp = tuple([sidx + 1, tidx + 1, count])
                    check = tuple([sidx + 1, tidx + 1])
                    aaa = memo.get(check, INF)
                    if aaa > count:
                        new_nodes.add(tmp)
                        memo[check] = count
                else:
                    if count < K:
                        # 追加
                        tmp = tuple([sidx + 1, tidx, count + 1])
                        check = tuple([sidx + 1, tidx])
                        aaa = memo.get(check, INF)
                        if aaa > count:
                            new_nodes.add(tmp)
                            memo[check] = count
                        # 削除
                        tmp = tuple([sidx, tidx + 1, count + 1])
                        check = tuple([sidx, tidx + 1])
                        aaa = memo.get(check, INF)
                        if aaa > count:
                            new_nodes.add(tmp)
                            memo[check] = count
                        # 変更
                        tmp = tuple([sidx + 1, tidx + 1, count + 1])
                        check = tuple([sidx + 1, tidx + 1])
                        aaa = memo.get(check, INF)
                        if aaa > count:
                            new_nodes.add(tmp)
                            memo[check] = count
            else:
                # SとT両方到達した場合はOK
                if sidx >= len(S) and tidx >= len(T):
                    return True
                # Sは到達した場合はTに文字をその分追加する
                if sidx >= len(S) and tidx < len(T):
                    # 追加しないといけない文字数 < 操作可能な回数であればOK
                    if len(T) - tidx <= K - count:
                        return True
                # Tは到達した場合はSに文字をその分追加する
                if sidx < len(S) and tidx >= len(T):
                    # 追加しないといけない文字数 < 操作可能な回数であればOK
                    if len(S) - sidx <= K - count:
                        return True
        nodes = new_nodes
    return False

K = int(input())
S = input()
T = input()
print("Yes" if calc(K, S, T) else "No")
