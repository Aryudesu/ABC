S, A, B, X = [int(l) for l in input().split()]
result = 0
a = 0
b = 0
for x in range(X):
    if a < A:
        result += S
        a += 1
        b = 0
    else:
        b += 1
        if b == B:
            a = 0
            b = 0
print(result)
