def calc(D, M):
    count = 0
    dat = 0
    for d in D:
        dat += d
        count += 1
        if dat > M:
            break
    return count


N, X, Y = [int(l) for l in input().split()]
A = [int(l) for l in input().split()]
B = [int(l) for l in input().split()]
A.sort(reverse=True)
B.sort(reverse=True)
print(min([calc(A, X), calc(B, Y)]))
