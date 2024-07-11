def printBoard(N, A, B):
    for x in range(N * A):
        res = ""
        for y in range(N * B):
            if (x // A) % 2 == 0:
                if (y // B) % 2 == 0:
                    res += "."
                else:
                    res += "#"
            else:
                if (y // B) % 2 == 0:
                    res += "#"
                else:
                    res += "."
        print(res)
    return


N, A, B = [int(l) for l in input().split()]
printBoard(N, A, B)
