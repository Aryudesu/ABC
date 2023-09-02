def calc_x(A, x, N):
    data = set()
    data.add(A[0])
    for n in range((N//2) + (N % 2) - 1):
        n_data = set()
        for dat in data:
            n_data.add(dat + A[n * 2 + 2])
            n_data.add(dat - A[n * 2 + 2])
        data = n_data
    return x in data


def calc_y(A, y, N):
    data = set()
    data.add(0)
    for n in range((N//2)):
        n_data = set()
        for dat in data:
            n_data.add(dat + A[n * 2 + 1])
            n_data.add(dat - A[n * 2 + 1])
        data = n_data
    return y in data


N, x, y = [int(l) for l in input().split()]
A = [int(l) for l in input().split()]
if calc_x(A, x, N) and calc_y(A, y, N):
    print('Yes')
else:
    print('No')
