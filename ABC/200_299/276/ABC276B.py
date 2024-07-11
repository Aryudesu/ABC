N, M = [int(l) for l in input().split()]
AB = dict()
for m in range(M):
    A, B = [int(l) for l in input().split()]
    tmpA = AB.setdefault(A, [])
    tmpB = AB.setdefault(B, [])
    tmpA.append(B)
    tmpB.append(A)
    AB[A] = tmpA
    AB[B] = tmpB
for n in range(N):
    tmp = AB.setdefault(n + 1, [])
    tmp.sort()
    print(str(len(tmp)) + " ", end="")
    print(*tmp)
