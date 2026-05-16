N, K = map(int, input().split())
A = []
for n in range(N):
    l, *a = list(map(int, input().split()))
    A.append(a)
C = list(map(int, input().split()))
k = 0
for n in range(N):
    a = A[n]
    l = len(a)
    # 追加する長さ
    dk = l * C[n]
    if k + dk >= K:
        # print(a, k, dk, K)
        print(a[(K-k-1)%l])
        break
    k += dk
