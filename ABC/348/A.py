N = int(input())
result = ""
for n in range(N):
    result += "o" if (n + 1) % 3 else "x"
print(result)
