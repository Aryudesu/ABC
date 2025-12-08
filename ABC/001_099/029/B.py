result = 0
for _ in range(12):
    result += 1 if "r" in set(list(input())) else 0
print(result)
