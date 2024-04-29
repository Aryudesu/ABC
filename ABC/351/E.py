# もうマヂ無理…
def dist(P1, P2):
    a = abs(P1[0] - P2[0])
    b = abs(P1[1] - P2[1])
    return a if a > b else b

def calcDistSum(data):
    M = len(data)
    result = 0
    for n in range(M - 1):
        for m in range(n + 1, M):
            result += dist(data[n], data[m])
    return result

N = int(input())
XY = []
data = dict()
for n in range(N):
    x, y = [int(l) for l in input().split()]
    key = 1 if x % 2 == y % 2 else 0
    val = [x, y]
    tmp = data.get(key, [])
    tmp.append(val)
    data[key] = tmp
print(calcDistSum(data.get(0, [])) + calcDistSum(data.get(1, [])))
