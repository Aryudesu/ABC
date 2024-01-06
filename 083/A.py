A, B, C, D = [int(l) for l in input().split()]
tmp = A + B - C - D
print("Left" if tmp > 0 else "Right" if tmp else "Balanced")
