N = int(input())
A = [int(input()) for _ in range(N)]
SA = sum(A)
dp = {0}
for a in A:
    nextSet = set()
    if a * 2 > SA:
        continue
    nextSet.add(a)
    for num in dp:
        nextSet.add(num)
        if (a + num) * 2 <= SA:
            nextSet.add(a + num)
    dp = nextSet
result = 0
for num in dp:
    result = max(result, min(num, SA - num))
print(result)
