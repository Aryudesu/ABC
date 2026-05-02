X, K = map(int, input().split())
B = 10
for k in range(K):
    tmp = X % B
    if int(str(tmp)[0]) >= 5:
        X += B - tmp
    else:
        X -= tmp
    B *= 10
print(X)
