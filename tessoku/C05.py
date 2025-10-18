N = int(input()) - 1
result = []
for _ in range(10):
    result.append("7" if N % 2 else "4")
    N //= 2
result.reverse()
print("".join(result))
