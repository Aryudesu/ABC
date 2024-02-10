N = int(input())
X = 0
Y = 0
for n in range(N):
    x, y = [int(l) for l in input().split()]
    X += x
    Y += y
if X > Y:
    print("Takahashi")
elif X == Y:
    print("Draw")
else:
    print("Aoki")
