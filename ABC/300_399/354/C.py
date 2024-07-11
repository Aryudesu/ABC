N = int(input())
AC = []
for n in range(N):
    a, c = [int(l) for l in input().split()]
    AC.append([a, c, n + 1])
AC.sort(reverse=True)
# print(AC)
m = 10 ** 9
result = []
for a, c, n in AC:
    if c < m:
        result.append(n)
        m = c
result.sort()
print(len(result))
print(*result)
