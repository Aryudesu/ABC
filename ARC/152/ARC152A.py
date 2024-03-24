def calc():
    N, L = [int(l) for l in input().split()]
    A = [int(l) for l in input().split()]
    s = 0
    J = N
    for idx in range(N):
        # 座る
        s += A[idx]
        # 1つ開けられる余裕があるなら1つ開ける
        if s + 1 <= L:
            s += 1
        # これ以上座れない場合
        if s > L:
            # ループを抜ける
            J = idx
            break
    # 残りの人たちは1人ばかりなら隙間を埋められるOK
    for j in range(J, N):
        if A[j] == 2:
            return False
    return True


print("Yes" if calc() else "No")
