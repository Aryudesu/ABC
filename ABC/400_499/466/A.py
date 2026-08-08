N = int(input())
X = list(map(int, input().split()))
isOk = True
for x in X:
    if x >= 0:
        isOk = False
print("Yes" if isOk else "No")
