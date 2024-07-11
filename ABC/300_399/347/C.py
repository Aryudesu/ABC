def calc(N, A, B, D):
    data = []
    for d in D:
        data.append(d % (A + B))
    data.sort()
    data.append(data[0] + (A + B))
    # print(data)
    for idx in range(N):
        if abs(data[idx] - data[(idx + 1) % (N + 1)]) > B:
            return True
    return False


N, A, B = [int(l) for l in input().split()]
D = [int(l) for l in input().split()]
print("Yes" if calc(N, A, B, D) else "No")
