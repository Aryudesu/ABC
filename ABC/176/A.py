N, X, T = [int(l) for l in input().split()]
num = 0
result = 0
while num < N:
    result += T
    num += X
print(result)
