X, Y = [int(l) for l in input().split()]
Z = Y - X
print(0 if X >= Y else Z//10 + (1 if Z%10 else 0))
