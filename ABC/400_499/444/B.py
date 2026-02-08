def isOk(num: int, K: int)->bool:
    nst = str(num)
    s = 0
    for n in nst:
        s += int(n)
    return s == K

N, K = map(int, input().split())
result = 0
for n in range(1, N + 1):
    if isOk(n, K):
        result += 1
print(result)
