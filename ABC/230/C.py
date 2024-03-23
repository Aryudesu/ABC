N, A, B = [int(l) for l in input().split()]
P, Q, R, S = [int(l) for l in input().split()]
for y in range(P, Q + 1):
    tmp = ""
    for x in range(R, S + 1):
        print("#" if abs(y - A) == abs(x - B) else ".", end="")
    print()
