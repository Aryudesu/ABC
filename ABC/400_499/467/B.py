N = int(input())
allTake = 10000
result = 10000
for _ in range(N):
    a, b, s = input().split()
    a, b = int(a), int(b)
    allTake -= a
    if s == "take":
        result -= a
    else:
        result -= b
print(allTake - result)
