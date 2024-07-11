N = int(input())
p = [int(l) for l in input().split()]
data = [0] * N
for n in range(3 * N):data[(p[n // 3] - (n // 3) + (n % 3 - 1)) % N] += 1
print(max(data))
