T = int(input())
result = []
for _ in range(T):
    N, A, B = [int(l) for l in input().split()]
    if N < A:
        result.append(False)
    else:
        # ポーンを置く最大数
        PMax = 0
        if N % 2 == 0:
            PMax = (N ** 2) // 2
        else:
            PMax = (N * (N + 1)) // 2
        # ポーンが残る数
        P = 0
        # ポーンを置いていない行にルークを置く
        if (N + 1)//2 <= A:
            # あああ
            P = PMax - A * (N + 1) // 2
        else:
            P = PMax - ((N + 1) // 2) ** 2
        result.append(B <= P)
for r in result:
    print("Yes" if r else "No")

