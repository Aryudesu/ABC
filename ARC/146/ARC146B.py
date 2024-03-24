N, M, K = [int(l) for l in input().split()]
A = [int(l) for l in input().split()]
A.sort()
print(A)
b = 1
data = []
for a in A:
    while True:
        if a <= b:
            break
        b <<= 1
    data.append([b, b- a])
print(data)
