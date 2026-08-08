from collections import defaultdict
from bisect import bisect_right

N, Q = map(int, input().split())
data = defaultdict(list)
for n in range(N):
    s, v = input().split()
    v = int(v)
    data[v].append((s, n))
result = []
kakaku = list(data.keys())
kakaku.sort()
for _ in range(Q):
    X = int(input())
    if X in data:
        res = [s for s, _ in data[X]]
        print(*res)
    else:
        idx = bisect_right(kakaku, X)
        if idx == 0:
            k = kakaku[idx]
            print(data[k][0][0])
        elif idx == len(kakaku):
            res1 = data[kakaku[idx-1]][0][0]
            print(res1)
        else:
            if abs(X - kakaku[idx-1]) < abs(X - kakaku[idx]):
                res1 = data[kakaku[idx-1]][0][0]
                print(res1)
            elif abs(X - kakaku[idx-1]) > abs(X - kakaku[idx]):
                res1 = data[kakaku[idx]][0][0]
                print(res1)           
            else:
                s1, res1 = data[kakaku[idx - 1]][0]
                s2, res2 = data[kakaku[idx]][0]
                if res1 == res2:
                    print(s1)
                elif res1 < res2:
                    print(s1)
                else:
                    print(s2)
