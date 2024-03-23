# sとtのl文字目からが一致するか
def isEq(s, t, l):
    if l + len(s) >= len(t):
        return False
    for i in range(len(s)):
        if s[i] != t[l + i]:
            return False
    return True


T = input()
lenT = len(T)
N = int(input())
S = []
# [n文字目] = コスト
memo = dict()
memo[0] = 0
for n in range(N):
    a, *s = [l for l in input().split()]
    S.append(s)
# 各まとまりについて
for s in S:
    new_memo = dict()
    # 各文字列について
    for d in s:
        # 各データについて
        for m in memo:
            new_memo[m] = min(new_memo[m], memo[m])
            if isEq(d, T, m):
                pass
    nemo = new_memo
