# ヘビ数かどうか
def isSnake(snum):
    h = int(snum[0])
    for i in range(1, len(snum)):
        if h <= int(snum[i]):
            return False
    return True

N = 9999
result = 0
for i in range(9000, N + 1):
    s = str(i)
    if isSnake(s):
        result += 1
print(result)
