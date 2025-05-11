N, M = [int(l) for l in input().split()]
A = []
for n in range(N):
    A.append([int(l) for l in input().split()])
left = []
right = []
left.append(A[0][0])
right.append(A[-1][-1])
result = 0
for i in range(N - 1):
    new_left = []
    new_right = []
    if i != N - 2:
        for j in range(i+1):
            ly = j
            lx = i - j
            tmp = (left[j] * 10) % M
            if lx + 1 < N:
                new_left.append((tmp + A[ly][lx + 1]) % M)
            if ly + 1 < N:
                new_left.append((tmp + A[ly + 1][lx]) % M)
            ry = N - ly - 1
            rx = N - lx - 1
            tmp = right[j]
            if rx - 1 >= 0:
                new_right.append((A[ry][rx - 1] * pow(10, i + 1, M) + right[j]) % M)
            if ry - 1 >= 0:
                new_right.append((A[ry - 1][rx] * pow(10, i + 1, M) + right[j]) % M)
        left = new_left
        right = new_right
    elif i == N - 1:
        for j in range(i+1):
            ly = j
            lx = i - j
            ry = N - ly - 1
            rx = N - lx - 1
            tmp = right[- n - 1]
            tmp = (tmp + left[n] * pow(10, N, M)) % M
            result = max(result, (tmp + A[n][N - 1 - n] * pow(10, N - 1, M)) % M)
            result = max(result, (tmp + A[n + 1][N - 2 - n] * pow(10, N - 1, M)) % M)
            # print(n, N - 1 - n)
            # print(n + 1, N - 2 - n)
print(left, right)
# result = 0
# for n in range(2 ** (N - 1)):
#     tmp = right[- n - 1]
#     tmp = (tmp + left[n] * pow(10, N, M)) % M
#     result = max(result, (tmp + A[n][N - 1 - n] * pow(10, N - 1, M)) % M)
#     result = max(result, (tmp + A[n + 1][N - 2 - n] * pow(10, N - 1, M)) % M)
#     # print(n, N - 1 - n)
#     # print(n + 1, N - 2 - n)
# print(result)
