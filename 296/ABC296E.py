def calc_loop(N, A):
    note = [None] * N
    mem = [None] * N
    loop_number = set()
    for n in range(N):
        if note[n]:
            continue
        idx = n
        l_idx = None
        while True:
            note[idx] = n
            idx = A[idx] - 1
            if not note[idx] is None:
                l_idx = A[idx] - 1
                break
        if note[l_idx] != n:
            continue
        while True:
            loop_number.add(l_idx)
            mem[l_idx] = True
            l_idx = A[l_idx] - 1
            if mem[l_idx]:
                break
    return len(loop_number)


N = int(input())
A = [int(l) for l in input().split()]
print(calc_loop(N, A))
