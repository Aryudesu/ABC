def bubble_sort(N, P):
    result = []
    swap_flag = False
    swap_idx = -1
    if len(P) == 2 and P[0] == 2:
        return False
    for i in range(N - 1):
        # 最大値のIDXを拾う
        s_idx = 0
        for j in range(1, N - i):
            if P[j] > P[s_idx]:
                s_idx = j
        # 最後まで持っていく
        for j in range(s_idx, N - i - 1):
            if P[j] > P[j + 1]:
                P[j - 1], P[j], P[j + 1] = P[j + 1], P[j - 1], P[j]
                if not swap_flag:
                    swap_flag = True
                    swap_idx = j
            else:
                if swap_flag:
                    result.append((swap_idx, j))
                swap_flag = False
        if swap_flag:
            result.append((swap_idx, N - 2 - i))
            swap_flag = False
    if P[0] % 2 == 1:
        for i in range(P[0] // 2):
            result.append(((i + 1) * 2, i * 2))
        return True, result
    return False, []


def calc(N, P):
    judge, res = bubble_sort(N, P)
    if judge:
        print("Yes")
        print(len(res))
        for r in res:
            print(*r)
    else:
        print("No")


N = int(input())
P = [int(l) for l in input().split()]
calc(N, P)
