N = 202501
# print((N-1)//4)
result = []
for i in range(N):
    if i ** 2 > N:
        break
    j = int((N - i ** 2) ** 0.5)
    for k in range(-1, 2):
        l = j + k
        if i ** 2 + l ** 2 == N:
            result.append((i, l))
print(result)
