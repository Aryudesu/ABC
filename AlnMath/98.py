N = int(input())
XY = []
for n in range(N):
    x, y = map(int, input().split())
    XY.append((x, y))
A, B = map(int, input().split())
for n in range(N + 1):
    x1, y1 = XY[n]
    x2, y2 = XY[(n+1) % N]
    
