N = int(input())
A = []
for n in range(N):
    A.append([int(l) - 1 for l in input().split()])
st = 0
for i in range(N):
    if st < i:
        st = A[i][st]
    else:
        st = A[st][i]
print(st + 1)
