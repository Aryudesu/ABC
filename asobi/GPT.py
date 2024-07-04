N = 1000
result = 0
num = [3, 5, 7]
for n in range(N + 1):
    count = 0
    for m in num:
        if n % m == 0:
            count += 1
    if count >= 2:
        result += n
print(result)
