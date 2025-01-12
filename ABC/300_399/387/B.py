X = int(input())
result = 0
for i in range(1, 10):
    for j in range(1, 10):
        t = i * j
        if t != X:
            result += t
print(result)
