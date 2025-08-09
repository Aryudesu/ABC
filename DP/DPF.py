def lcs_myers(A: str, B: str) -> str:
    N, M = len(A), len(B)
    max_d = N + M
    offset = max_d
    V = [0] * (2 * max_d + 1)
    trace = []

    found = False
    for D in range(max_d + 1):
        current_V = V.copy()
        for k in range(-D, D + 1, 2):
            if k == -D or (k != D and V[k - 1 + offset] < V[k + 1 + offset]):
                x = V[k + 1 + offset]
            else:
                x = V[k - 1 + offset] + 1
            y = x - k
            # 🐍「スネーク」と呼ばれる一致部分を貪欲に進む
            while x < N and y < M and A[x] == B[y]:
                x += 1
                y += 1
            current_V[k + offset] = x
            if x >= N and y >= M:
                trace.append(current_V)
                end_D = D
                end_k = k
                found = True
                break
        trace.append(current_V)
        if found:
            break

    # 🔄 LCSを逆から復元
    x, y = N, M
    lcs_rev = []
    for D in reversed(range(end_D + 1)):
        V = trace[D]
        k = x - y
        if k == -D or (k != D and V[k - 1 + offset] < V[k + 1 + offset]):
            prev_k = k + 1
        else:
            prev_k = k - 1
        prev_x = V[prev_k + offset]
        prev_y = prev_x - prev_k
        while x > prev_x and y > prev_y:
            if x - 1 >= 0 and y - 1 >= 0:
                lcs_rev.append(A[x - 1])
            x -= 1
            y -= 1
        x = prev_x
        y = prev_y

    return ''.join(reversed(lcs_rev))


S = input()
T = input()
print(lcs_myers(S, T))
