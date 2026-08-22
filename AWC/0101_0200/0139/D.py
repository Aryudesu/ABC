from sortedcontainers import SortedList

N, H = map(int, input().split())
D = list(map(int, input().split()))
D[0] = 10 ** 13
D.reverse()
data = SortedList()
for n in range(N):
    d = D[n]
    S = H
    while data:
        if S == 0:
            break
        if data[0] <= S:
            e = data.pop(0)
            S -= e
        else:
            e = data.pop(0)
            e -= S
            S = 0
            data.add(e)
    data.add(d)
print(N - len(data))
