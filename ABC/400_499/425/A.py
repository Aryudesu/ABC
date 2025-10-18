N = int(input())
s = 0
for n in range(1, N + 1):
    s += ((-1) ** n) * (n ** 3)
print(s)
