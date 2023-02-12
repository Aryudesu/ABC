def calc(N, A):
    result = 0
    while True:
        for n in range(N):
            if A[n] & 1 or A[n] == 0:
                return result
            A[n] >>= 1
        result += 1


N = int(input())
A = [int(l) for l in input().split()]
print(calc(N, A))
