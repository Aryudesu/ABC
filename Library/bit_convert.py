from itertools import product

N = 3
for bits in product([0, 1], repeat=N):
    mask = sum((bit << i) for i, bit in enumerate(bits))


bits = [(mask >> i) & 1 for i in range(N)]

