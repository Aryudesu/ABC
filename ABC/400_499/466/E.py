N, K = map(int, input().split())
# 裏返すとき
turn = [0] * (K + 1)
# 裏返さないとき
not_turn = [0] * (K + 1)
turn[0] = 0
not_turn[0] = 0
for n in range(N):
    a, b = map(int, input().split())
    next_turn = [0] * (K + 1)
    next_not_turn = [0] * (K + 1)
    # 裏返さないとき
    for k in range(min(n, K), -1, -1):
        next_not_turn[k] = max(turn[k] + a, not_turn[k] + a)
    # 裏返すとき
    for k in range(min(n + 1, K), 0, -1):
        if k == 1:
            next_turn[k] = max(turn[k] + b, not_turn[k-1] + b)
        next_turn[k] = max(turn[k] + b, not_turn[k-1] + b)
    turn = next_turn
    not_turn = next_not_turn
print(max(max(not_turn), max(turn)))
