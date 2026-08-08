N, M = map(int, input().split())
C = list(map(int, input().split()))
R = list(map(int, input().split()))
C.sort()
R.sort()
cidx = 0
ridx = 0
result = 0
for cidx in range(N):
    while ridx < M:
        if C[cidx] <= R[ridx]:
            ridx += 1
            result += 1
            break
        ridx += 1
print(result)
