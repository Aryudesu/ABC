N = int(input())
lResult = []
rResult = []
for i in range(1, N + 1):
    if i * i > N:
        break
    if N % i == 0:
        lResult.append(i)
        if i * i != N:
            rResult.append(N // i)
rResult.reverse()
for n in lResult:
    print(n)
for n in rResult:
    print(n)
