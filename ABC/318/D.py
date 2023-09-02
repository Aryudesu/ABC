N = int(input())
graph = dict()
for n in range(N - 1):
    D = [int(l) for l in input().split()]
    for m in range(N - n - 1):
        c = (1 << n) | (1 << (m + n + 1))
        graph[c] = D[m]
dp = dict()
dp[0] = 0

for n in range(N//2):
    new_dp = dict()
    for num in dp:
        for branch in graph:
            if not (num & branch):
                c = branch | num
                w = dp.get(num, 0)
                bw = graph.get(branch, 0)
                tmp = new_dp.get(c, 0)
                if tmp < w + bw:
                    new_dp[c] = w + bw
    dp = new_dp
result = 0
for d in dp:
    tmp = dp.get(d, 0)
    if result < tmp:
        result = tmp
print(result)
