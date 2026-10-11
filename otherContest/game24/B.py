H, W, N = map(int, input().split())
minR = H
maxR = 0
minC = W
maxC = 0
for _ in range(N):
    r, c = map(int, input().split())
    minR = min(minR, r)
    maxR = max(maxR, r)
    minC = min(minC, c)
    maxC = max(maxC, c)
A = [minR-1, H-maxR, minC-1, W-maxC]
nim = 0
for a in A:
    nim ^= a
print("Alice" if nim else "Bob")
