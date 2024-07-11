import sys

sys.setrecursionlimit(10**7)

S = input()
LDATA = dict()
RDATA = dict()
alp = "abcdefghijklmnopqrstuvwxyz"
ALP = alp.upper()
alpData = dict()
for idx in range(len(alp)):
    alpData[alp[idx]] = ALP[idx]
    alpData[ALP[idx]] = alp[idx]
# RESULT = []

def disp(idx, eidx, d):
    """結果を描画します
    @param idx: 開始インデックス
    @param eidx: 終了インデックス
    @param d: 方向（1が右，-1が左）
    @return None
    """
    index = idx
    while True:
        if index == eidx:
            return
        s = S[index]
        if s == "(":
            # 左方向に移動している場合
            if d == -1:
                return
            # 右方向に移動している場合
            elif d == 1:
                disp(LDATA[index] - 1, index, -d)
                index = LDATA[index]
        elif s == ")":
            # 右方向に移動している場合
            if d == 1:
                # 対応括弧に到達した場合
                return
            # 左方向に移動している場合
            elif d == -1:
                disp(RDATA[index] + 1, index, -d)
                index = RDATA[index]
        else:
            if d == 1:
                print(s, end="")
            else:
                print(alpData.get(s, ""), end="")
        index += d

data = dict()
count = 0
for idx in range(len(S)):
    s = S[idx]
    if s == "(":
        data[count] = idx
        count += 1
    elif s == ")":
        count -= 1
        LDATA[data[count]] = idx
        RDATA[idx] = data[count]

idx = 0
disp(0, len(S), 1)
# print("".join(RESULT))
