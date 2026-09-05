N = int(input())
A = list(map(int, input().split()))
result = [None] * N
ones = []
twos = []
c = 0
for idx in range(N):
    if A[idx] == 0:
        # print(c)
        if result[idx] is None:
            result[idx] = c
            c += 1
        if result[(idx-1)%N] is None and A[(idx-1)%N] == 1:
            ones.append((idx - 1)%N)
        if result[(idx+1)%N] is None and A[(idx+1)%N] == 1:
            ones.append((idx + 1)%N)
        if result[(idx-1)%N] is None and A[(idx-1)%N] == 2:
            twos.append((idx - 1)%N)
        if result[(idx+1)%N] is None and A[(idx+1)%N] == 2:
            twos.append((idx + 1)%N)
while ones:
    nextOnes = []
    for idx in ones:
        # print(c)
        if result[idx] is None:
            result[idx] = c
            c += 1
        if result[(idx-1)%N] is None and A[(idx-1)%N] == 1:
            nextOnes.append((idx - 1)%N)
        if result[(idx+1)%N] is None and A[(idx+1)%N] == 1:
            nextOnes.append((idx + 1)%N)
        if result[(idx-1)%N] is None and A[(idx-1)%N] == 2:
            twos.append((idx - 1)%N)
        if result[(idx+1)%N] is None and A[(idx+1)%N] == 2:
            twos.append((idx + 1)%N)
    ones = nextOnes
for idx in twos:
    if result[idx] is None:
        result[idx] = c
        c += 1
isOk = True
if None in result:
    isOk = False
else:
    for idx in range(N):
        result[idx] += 1
        if (result[(idx-1)%N] < result[idx]) + (result[((idx+1)%N)] < result[idx]) != A[idx]:
            isOk = False
if isOk:
    print(*result)
else:
    print(-1)
