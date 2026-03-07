def calc(S: str, T: str)->int:
    result = 0
    sIdx = 0
    for t in T:
        # Sが終わった場合
        if sIdx >= len(S):
            # AならAを挿入できるがそれ以外なら無理
            if t != "A":
                return -1
            else:
                result += 1
                continue
        # 文字が同じならスルー
        if S[sIdx] == t:
            sIdx += 1
        # 違う場合
        elif S[sIdx] != t:
            # tがAならSに挿入
            if t == "A":
                result += 1
                continue
            if S[sIdx] == "A":
                # sがAならAの間ずっと削除
                while sIdx < len(S) and S[sIdx] == "A":
                    result += 1
                    sIdx += 1
                # 範囲外になったら無理
                if sIdx >= len(S):
                    return -1
                # SとT違う文字なら無理
                if S[sIdx] != t:
                    return -1
            else:
                # どうしようもないなら無理
                return -1
            sIdx += 1
    # SについてるAをひたすら外す
    while sIdx < len(S):
        if S[sIdx] != "A":
            return -1
        sIdx += 1
        result += 1
    return result



S = input()
T = input()
print(calc(S, T))
