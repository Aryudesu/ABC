x1, y1 = [int(l) for l in input().split()]
x2, y2 = [int(l) for l in input().split()]
x3, y3 = [int(l) for l in input().split()]
x4, y4 = [int(l) for l in input().split()]
A = (0, 0)
B = (x2 - x1, y2 - y1)
C = (x3 - x1, y3 - y1)
D = (x4 - x1, y4 - y1)
a = B[0]
b = C[0] - D[0]
c = B[1]
d = C[1] - D[1]

s = (C[0] * d + C[1] * (-b)) / (a * d - b * c)
t = (- C[0] * c + C[1] * a) / (a * d - b * c)
print("Yes" if abs(s) < 1 and abs(t) < 1 else "No")
