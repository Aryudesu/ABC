from collections import defaultdict

alpLen = 26
MOD = 998244353
N = int(input())
S1, S2, S3 = input().split()
graphTo = defaultdict(set)
s2i = dict()
blank = ""
bNode = 0

prev = blank
s2i[prev] = 0
counter = 1
for i in range(1, len(S1) + 1):
    tmp = S1[:i]
    if tmp not in s2i:
        s2i[tmp] = counter
        counter += 1
    graphTo[s2i[prev]].add(s2i[tmp])
    prev = tmp

prev = ""
for i in range(1, len(S2) + 1):
    tmp = S2[:i]
    if tmp not in s2i:
        s2i[tmp] = counter
        counter += 1
    graphTo[s2i[prev]].add(s2i[tmp])
    prev = tmp

prev = ""
for i in range(1, len(S3) + 1):
    tmp = S3[:i]
    if tmp not in s2i:
        s2i[tmp] = counter
        counter += 1
    graphTo[s2i[prev]].add(s2i[tmp])
    prev = tmp

leafs = set()
for c in range(counter):
    if len(graphTo[c]) == 0:
        leafs.add(c)
ends = set()
ends.add(s2i[S1])
ends.add(s2i[S2])
ends.add(s2i[S3])

dp = [0] * counter
dp[bNode] = 1
for n in range(N):
    nextDP = dp.copy()
    nowNodes = {0}
    while nowNodes:
        nextNodes = set()
        for node in nowNodes:
            nextDP[node] = (nextDP[node] + dp[node] * (alpLen - len(graphTo[node]))) % MOD
            # 遷移元からの計算
            for nextNode in graphTo[node]:
                nextDP[nextNode] = (nextDP[nextNode] + dp[node]) % MOD
                nextNodes.add(nextNode)
        nowNodes = nextNodes
    dp = nextDP

delNum = 0
# 重複分考えないといけない………
delNum2 = 0
nodes = {0}
while nodes:
    nextNodes = set()
    for node in nodes:
        for nextNode in graphTo[node]:
            if nextNode in ends:
                delNum += dp[nextNode]
                continue
            nextNodes.add(nextNode)
    nodes = nextNodes

result = (pow(26, N, MOD) - delNum + delNum2) % MOD
print(result)
