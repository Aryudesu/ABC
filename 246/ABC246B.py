import math

A, B = [int(l) for l in input().split()]
param = []
param.append(str(A / math.sqrt(A * A + B * B)))
param.append(str(B / math.sqrt(A * A + B * B)))
print(" ".join(param))
