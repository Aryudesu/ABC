from collections import defaultdict

alp = "abcdefghijklmnopqrstuvwxyz"
alpIdx = dict()
for i in range(len(alp)):
    alpIdx[alp[i]] = i

N = int(input())
data = defaultdict(int)
for n in range(N):
    tmp = [0] * len(alp)
    S = input()
    for s in S:
        tmp[alpIdx[s]] += 1
    data[tuple(tmp)] += 1

result = 0
for dat in data:
    tmp = data[dat]
    result += (tmp * (tmp - 1)) // 2
print(result)
