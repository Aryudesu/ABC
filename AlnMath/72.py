def calc(A: int, B: int)->int:
    for g in range(B-A, 0, -1):
        a = A//g
        if A%g != 0:
            a += 1
        if A <= a * g <= (a + 1) * g <= B:
            return g

A, B = map(int, input().split())
print(calc(A, B))
