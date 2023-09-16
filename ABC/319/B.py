def calc(num, i):
    for j in range(1, 10):
        if num % j == 0:
            if i % (num // j) == 0:
                return str(j)
    return "-"


N = int(input())
result = ""
for i in range(N + 1):
    result += calc(N, i)
print(result)
