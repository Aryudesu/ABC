def makeMaze(N, M, K):
    data = [[False] * M for _ in range(N)]
    Mtmp = M - 1
    Ktmp = K - N
    print("+" * (2 * M - 1) + "S" + "+")
    for n in range(N):
        pass
    print("+" * (2 * M - 1) + "G" + "+")




def calc(N, M, K):
    if (K - N) % 2:
        print("No")
        return
    print("Yes")
    makeMaze(N, M, K)

N, M, K = [int(l) for l in input().split()]
calc(N, M, K)
