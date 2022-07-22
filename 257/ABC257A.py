import math

N, X = [int(l) for l in input().split()]
S = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
print(S[math.ceil(X/N) - 1])