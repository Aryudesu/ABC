def calc(a: int, N: int)-> int:
    nodes = {N}
    memo = {N}
    result = 0
    while nodes:
        nextNodes = set()
        for node in nodes:
            # 割り切れたら割る
            if node%a == 0:
                tmp = node//a
                # 既に探索済なら次の候補に入れない
                if not tmp in memo:
                    nextNodes.add(tmp)
                    memo.add(tmp)
            s = str(node)
            # 2文字目が"0"の場合は操作されない
            if len(s) >= 2:
                if s[1] == "0":
                    continue
            nextNum = int(s[1:] + s[0])
            if not nextNum in memo:
                nextNodes.add(nextNum)
                memo.add(nextNum)
        nodes = nextNodes
        result += 1
        if 1 in nodes:
            return result
    return -1

a, N = map(int, input().split())
print(calc(a, N))
