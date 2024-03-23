N = int(input())
result = 0
tmp = 1
while tmp <= N:
    result += 1
    tmp <<= 1
print(result-1)
