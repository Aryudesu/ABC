N, K = map(int, input().split())
X = list(map(int, input().split()))
L = []
R = []
for x in X:
    if x < 0:
        L.append(x)
    else:
        R.append(x)
L.sort(reverse=True)
R.sort()
result = 0
while L:
    result += abs(L.pop())
    for k in range(K-1):
        if not L:
            break
        L.pop()
while R:
    result += abs(R.pop())
    for k in range(K-1):
        if not R:
            break
        R.pop()
print(result * 2)
