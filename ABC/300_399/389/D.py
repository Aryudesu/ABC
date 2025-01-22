r = int(input())
R = r * 2
result = 0
for i in range(3, R, 2):
    x = int((R ** 2 - i**2) ** 0.5)
    result += (x - 1) // 2
# print(result * 4)
result *= 4
result += ((r - 1) * 4 + 1)
print(result)
