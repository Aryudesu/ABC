def calc(A):
    data = dict()
    for a in A:
        data[a] = data.get(a, 0) + 1
    result = -1
    max_num = -1
    for n in range(N):
        a = A[n]
        if data[a] == 1:
            if max_num < a:
                result = n + 1
                max_num = a
    return result


N = int(input())
A = [int(l) for l in input().split()]
print(calc(A))
