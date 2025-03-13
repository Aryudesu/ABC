from atcoder.twosat import TwoSAT

N, M = [int(l) for l in input().split()]
max_bit = 0
XYZ = []
for m in range(M):
    x, y, z = [int(l) for l in input().split()]
    z_bit = bin(z)
    b_len = len(z_bit) - 2
    max_bit = max([max_bit, b_len])
    XYZ.append([x, y, z, b_len])
print(max_bit)
ts = TwoSAT(M * max_bit)
for x, y, z, b in XYZ:
    pass
