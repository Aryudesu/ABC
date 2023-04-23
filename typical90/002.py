def calc(N, a, b, s, result):
    if a == N:
        result.append(s + ')' * (N - b))
    elif a < N:
        calc(N, a + 1, b, s + '(', result)
        if a > b:
            calc(N, a, b + 1, s + ')', result)


result = []
N = int(input())
if not N % 2:
    calc(N//2, 0, 0, '', result)
result.sort()
for r in result:
    print(r)
