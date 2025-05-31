N = int(input())
result = 0
for i in range(1, 10 ** 6 + 1):
    l = len(str(i))
    num = i * (10 ** l) + i
    if num <= N:
        result += 1
    else:
        break
print(result)
