def calc(A: int, B: int, C: int, D: int)->int:
    if A > C:
        A = -A
        B = -B
        C = -C
        D = -D
    if B <= D <= A <= C:
        return abs(A-C) + abs(B-D)
    if D <= B < A <= C:
        return abs(A-C) + abs(B-D)
    if A <= C <= B <= D:
        return abs(A-C) + abs(B-D)
    if A <= C < D <= B:
        return abs(A-C) + abs(B-D)
    if B < A <= D < C:
        return abs(A-C) + abs(B-D)
    if A < B <= C < D:
        return abs(A-C) + abs(B-D)
    if B < A <= C < D:
        return abs(A-C) + abs(B-D) + 1
    if A < B <= D < C:
        return abs(A-C) + abs(B-D) + 1
    if D < A == C < B:
        return abs(A-C) + abs(B-D) + 1
    if A <= D < B <= C:
        return abs(A-C) + abs(B-D) - 1
    if D <= A < B <= C:
        return abs(A-C) + abs(B-D) - 1
    if D <= A < C <= B:
        return abs(A-C) + abs(B-D) - 1
    if A <= D < C <= B:
        return abs(A-C) + abs(B-D) - 1
    raise Exception()

A, B, C, D = map(int, input().split())
print(calc(A, B, C, D))
