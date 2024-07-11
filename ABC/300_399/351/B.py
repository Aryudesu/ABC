N = int(input())
A = []
B = []
for n in range(N):
    A.append(input())
for n in range(N):
    B.append(input())
for i in range(N):
    for j in range(N):
        if (A[i][j] != B[i][j]):
            print(i + 1, j + 1)
