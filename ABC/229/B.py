def calc(A, B):
    A.reverse()
    B.reverse()
    for idx in range(min([len(A), len(B)])):
        a = int(A[idx])
        b = int(B[idx])
        if a + b >= 10:
            return "Hard"
    return "Easy"


A, B = [list(l) for l in input().split()]
print(calc(A, B))
