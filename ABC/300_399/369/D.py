N = int(input())
A = [int(l) for l in input().split()]
if N >= 2:
    # 奇数回
    o = max([A[0], A[1]])
    # 偶数回
    e = A[0] + A[1] * 2
    for i in range(2, N):
        tmp_e = max([e, o + 2 * A[i]])
        tmp_o = max([o, e + A[i]])
        e = tmp_e
        o = tmp_o
    print(max([e, o]))
else:
    print(A[0])
