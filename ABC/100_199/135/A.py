A, B = [int(l) for l in input().split()]
print("IMPOSSIBLE" if (A + B) % 2 else (A + B)//2)
