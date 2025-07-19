T = int(input())
for t in range(T):
    N = int(input())
    A = [(abs(int(l)), int(l)) for l in input().split()]
    A.sort()
    f = True
    data = set()
    for i in range(N-1):
        data.add(A[i][0])
        if A[i+1][1] * A[0][1] !=  A[i][1] * A[1][1]:
            f = False
    data.add(A[-1][0])
    # |公比| == 1のとき
    # print(data)
    if len(data) == 1:
        p = 0
        m = 0
        for a, b in A:
            if b > 0:
                p += 1
            else:
                m += 1
        print("Yes" if abs(p - m) <= 1 or p == 0 or m == 0 else "No")
    else:
        print("Yes" if f else "No")
