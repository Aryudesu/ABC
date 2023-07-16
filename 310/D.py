N, T, M = [int(l) for l in input().split()]
person = dict()
Team = []
for t in range(T):
    tmp = set()
    Team.append(tmp)
for m in range(M):
    a, b = [int(l) for l in input().split()]
    tmp = person.get(a)
    if tmp is None:
        tmp = set()
    tmp.add(b)
    person[a] = tmp
    tmp = person.get(b)
    if tmp is None:
        tmp = set()
    tmp.add(a)
    person[b] = tmp

result = 0


def partition(num, N, TN):
    if N - num < T - TN:
        return
    if num == N:
        for t in Team:
            if not t:
                return
        global result
        result = result + 1
        return
    for t in range(T):
        tmp = Team[t]
        tmp2 = person.get(num + 1)
        # 相性悪い組み合わせが存在すると計算しない
        if tmp2 is not None:
            if len(tmp & tmp2):
                continue
        # チームに追加
        Team[t].add(num+1)
        partition(num+1, N, TN if t < TN else TN + 1)
        Team[t].remove(num+1)
        if not Team[t]:
            break


partition(0, N, 0)
print(result)
