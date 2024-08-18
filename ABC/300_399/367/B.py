def calc(X):
    if (isinstance(X, float)) and X.is_integer():
        return int(X)
    return X

X = float(input())
print(calc(X))
