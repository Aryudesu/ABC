def calc(S, A):
    data = {0}
    for a in A:
        new_data = set()
        for dat in data:
            new_data.add(dat)
            tmp = dat + a
            if tmp == S:
                return True
            if tmp < S:
                new_data.add(tmp)
        data = new_data
    return False


N, S = [int(l) for l in input().split()]
A = [int(l) for l in input().split()]
print("Yes" if calc(S, A) else "No")
