def calc(N, K, A, B):
    for n in range(N):
        AB.append((B[n], A[n]))
    AB.sort()
    bsum = 0
    for k in range(K):
        bsum += AB[k][0]


T = int(input())
AB = []
for t in range(T):
    N, K = [int(l) for l in input().split()]
    A = [int(l) for l in input().split()]
    B = [int(l) for l in input().split()]
    calc(N, K, A, B)
