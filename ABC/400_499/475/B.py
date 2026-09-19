N = int(input())
A = list(map(int, input().split()))
oneRes = 0
tenRes = 0
hunRes = 0
for a in A:
    if a % 1000 == 0:
        continue
    num = 1000 - (a % 1000)
    oneRes += num % 10
    tenRes += (num % 100) // 10
    hunRes += (num % 1000) // 100
print(oneRes, tenRes, hunRes)
