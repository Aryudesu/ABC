def calc(S, T):
    lenS = len(S)
    # 区切り文字数
    for w in range(1, lenS - 1):
        # 実際に区切る
        tmp = [S[i: i+w] for i in range(0, len(S), w)]
        # 区切り文字
        for c in range(w):
            data = ""
            for i in range(len(tmp)):
                if c >= len(tmp[i]):
                    break
                data += tmp[i][c]
            if T == data:
                return True
    return False

S, T = input().split()
print("Yes" if calc(S, T) else  "No")
