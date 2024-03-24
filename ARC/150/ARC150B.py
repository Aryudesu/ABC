T = int(input())
for t in range(T):
    A, B = [int(l) for l in input().split()]
    C = B//A
    if A * C == B:
        print(0)
        continue
    elif B < A:
        print(A - B)
        continue
    else:
        T = C - B % C
        Y = 0 if T == C else T
        print('Y = ', Y)
        C += 1
        T = C - B % C
        Y = 0 if T == C else T
        print('Y = ', Y)
        X = (B + Y)//C - A
        XY = X + Y
        print(XY)
