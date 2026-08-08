N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
prevZero = 0
prevOne = 0
if A[0] % 2 == 0:
    prevZero = 0
    prevOne = 1
else:
    prevZero = 1
    prevOne = 0
for i in range(1, N):
    nextZero = 0
    nextOne = 0
    if B[i-1] == 0:
        if A[i] % 2 == 0:
            nextZero = prevZero
            nextOne = prevOne + 1
        else:
            nextZero = prevZero + 1
            nextOne = prevOne
    else:
        if A[i] % 2 == 0:
            nextZero = prevOne
            nextOne = prevZero + 1
        else:
            nextZero = prevOne + 1
            nextOne = prevZero
    prevZero = nextZero
    prevOne = nextOne
print(min(prevZero, prevOne))
