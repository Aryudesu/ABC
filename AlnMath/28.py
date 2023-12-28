N = int(input())
H = [int(l) for l in input().split()]
data = [10**10] * N
data[0] = 0
for n in range(N):
    i = n
    j = n + 1
    if j < N:
        if data[j] > data[i] + abs(H[i] - H[j]):
            data[j] = data[i] + abs(H[i] - H[j])
    j = n + 2
    if j < N:
        if data[j] > data[i] + abs(H[i] - H[j]):
            data[j] = data[i] + abs(H[i] - H[j])
print(data[-1])
