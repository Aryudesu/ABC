X, Y = [int(l) for l in input().split()]
result = 0
while Y >= X:
    Y >>= 1
    result += 1
print(result)
