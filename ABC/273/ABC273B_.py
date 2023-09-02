X, K = [int(l) for l in input().split()]
for k in range(K):
    tmp = X // (10 ** k)
    X = (tmp//10 + (1 if tmp % 10 >= 5 else 0))*10 * (10 ** k)
print(X)
