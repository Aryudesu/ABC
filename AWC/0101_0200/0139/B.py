def calc(N: int)->int:
    result = 1
    for a in range(1, N + 1):
        if a * a > N:
            break
        if N % a == 0:
            b = N // a
            result = max(result, min(a, b))
    return result


Q = int(input())
result = []
for _ in range(Q):
    N = int(input())
    result.append(calc(N))
print(*result, sep="\n")
