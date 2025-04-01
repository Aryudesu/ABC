def calc(N, A, X):
    Asum = sum(A)
    num = X // Asum
    amari = X % Asum
    s = 0
    count = 0
    for a in A:
        s += a
        count += 1
        if s > amari:
            break
    return num * N + count

N = int(input())
A = [int(l) for l in input().split()]
X = int(input())
print(calc(N, A, X))
