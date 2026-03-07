N = int(input())
P = list(map(int, input().split()))
dpData = {0}
for p in P:
    nextDp = dpData.copy()
    for num in dpData:
        nextDp.add(num + p)
    dpData = nextDp
print(len(dpData))
