def rotate(A, N):
    result = []
    for y in range(N):
        tmp = []
        for x in range(N):
            tmp.append(A[N - x - 1][y])
        result.append(tmp)
    return result


def is_ok(A, B, N):
    for y in range(N):
        for x in range(N):
            if A[y][x] == 1 and B[y][x] != 1:
                return False
    return True


def print_a(A):
    for a in A:
        print(a)


def calc(A, B, N):
    # print_a(A)
    if is_ok(A, B, N):
        return True
    A = rotate(A, N)
    # print_a(A)
    if is_ok(A, B, N):
        return True
    A = rotate(A, N)
    # print_a(A)
    if is_ok(A, B, N):
        return True
    A = rotate(A, N)
    # print_a(A)
    if is_ok(A, B, N):
        return True
    return False


N = int(input())
A = [[int(l) for l in input().split()] for _ in range(N)]
B = [[int(l) for l in input().split()] for _ in range(N)]
print("Yes" if calc(A, B, N) else "No")
