def calcMin(N, K, X, A):
    count = 0
    flag = False
    A.sort(reverse=True)
    for num in range(N):
        if A[num] > X:
            tmp = int(A[num] / X)
            if count + tmp > K:
                tmp = K - count
                flag = True
            A[num] -= X * tmp
            count += tmp
        if flag or K == count:
            break
    A.sort(reverse=True)
    result = 0
    for num in range(K - count, N):
        result += A[num]
    print(result)


N, K, X = [int(l) for l in input().split()]
A = [int(l) for l in input().split()]
calcMin(N, K, X, A)
