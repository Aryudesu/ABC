def calc(A, X):
    for a in A:
        if (X + a) in A:
            return True
    False


N, X = [int(l) for l in input().split()]
A = {int(l) for l in input().split()}
print("Yes" if calc(A, X) else "No")
