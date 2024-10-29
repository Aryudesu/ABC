def get_pos(num, i, j):
    if num == 0:
        return i, i + j
    elif num == 1:
        return i + j, N - i - 1
    elif num == 2:
        return N - i - 1, N - i - j - 1
    elif num == 3:
        return N - i - j - 1, i
    raise Exception()

def calc(N, A):
    # 右90度
    result = [[" " for n in range(N)] for n in range(N)]
    for i in range(N//2 + 1):
        for j in range(N - i * 2):
            for k in range(4):
                n_y, n_x = get_pos(k, i, j)
                y, x = get_pos((k - i - 1) % 4, i, j)
                result[n_y][n_x] = A[y][x]
    return result


N = int(input())
result = calc(N, [list(input()) for n in range(N)])
for i in range(N):
    for j in range(N):
        print(result[i][j], end="")
    print()
