def calc(N):
    T = N // 5
    # 5Mおき
    U = N % 5
    # 次の給水所との差
    V = 5 - U
    # 手前より奥のほうが近い
    if U > V:
        T += 1
    return T * 5


N = int(input())
print(calc(N))
