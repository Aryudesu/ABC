def calc(A, B, X):
    stair = [False] * (X + 1)
    stair[0] = True
    for idx in range(X):
        if not stair[idx] or idx in B:
            continue
        for a in A:
            if a + idx == X:
                return True
            elif a + idx < X:
                stair[a + idx] = True
    return False


N = int(input())
A = [int(l) for l in input().split()]
M = int(input())
B = {int(l) for l in input().split()}
X = int(input())
print("Yes" if calc(A, B, X) else "No")
