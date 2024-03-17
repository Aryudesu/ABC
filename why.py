result = 0
for i in range(0, 100):
    if (i % 3) * (i % 5) == 0:
        result += i
print(result)
