N = int(input())
A, B, C = [int(l) for l in input().split()]
result = 9999
for i in range(10000):
    for j in range(10000):
        tmp = i * A + j * B
        if (N - tmp) % C or N - tmp < 0:
            continue
        k = (N - tmp) // C
        if result > i + j + k:
            result = i + j + k
print(result)
