def HitAndBlow(A, B, N):
    Hit = 0
    Blow = 0
    for Aindex in range(N):
        for Bindex in range(N):
            if A[Aindex] == B[Bindex]:
                if Aindex == Bindex:
                    Hit += 1
                else:
                    Blow += 1
    print(Hit)
    print(Blow)


N = int(input())
A = [int(l) for l in input().split()]
B = [int(l) for l in input().split()]
HitAndBlow(A, B, N)
