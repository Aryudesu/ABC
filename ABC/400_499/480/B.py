# 大抵のクラスは以下を使用
# https://github.com/Aryudesu/myLibrary

def isSame(S: str, T: str)->int:
    if S == T:
        return 1
    if len(S) != len(T):
        return 0
    cnt = 0
    for s, t in zip(S, T):
        if s != t:
            cnt += 1
    return 2 if cnt == 1 else 0

N, M = map(int, input().split())
S = [input() for _ in range(N)]
T = [input() for _ in range(M)]
data = dict()
for s in S:
    data[s] = 0
for t in T:
    cnt = 0
    memo = set()
    for s in S:
        check = isSame(s, t)
        match check:
            case 0:
                continue
            case 1:
                data[s] += 1
                memo = set()
                break
            case 2:
                memo.add(s)
            case _:
                raise ValueError()
    if len(memo) == 1:
        u = memo.pop()
        data[u] += 1
result = []
for s in S:
    result.append(data[s])
print(*result, sep="\n")
