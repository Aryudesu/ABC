N = 60
nums = [1, 2, 3]
data = [0] * (N + 1)
data[0] = 1
for i in range(0, N + 1):
    for n in nums:
        if i + n <= N:
            data[i + n] += data[i]
print(data)
print(sum(data))
