Coin = []
A = int(input()) + 1
B = int(input()) + 1
C = int(input()) + 1
X = int(input())
result = 0
for a in range(A):
    for b in range(B):
        for c in range(C):
            if X == a * 500 + b * 100 + c * 50:
                result += 1
print(result)
