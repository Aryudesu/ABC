N, L, R = [int(l) for l in input().split()]
data = [i for i in range(1, N + 1)]
d1 = data[:L-1]
d2 = data[L-1:R]
d2.reverse()
d3 = data[R:]
result = d1 + d2 + d3
print(*result)
# print(d1, d2, d3)
