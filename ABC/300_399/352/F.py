def solve_queries(N, M, constraints):
    # 各人の順位を初期化
    rankings = [-1] * N
    
    # 各制約について順位を更新
    for i in range(M):
        x, y, c = constraints[i]
        x -= 1  # 0-indexedに変換
        y -= 1
        
        # 既に順位が決まっている場合
        if rankings[x] != -1:
            rank_y = rankings[x] - c
            if 1 <= rank_y <= N and rankings[y] == -1:
                rankings[y] = rank_y
            else:
                return [-1] * N
        elif rankings[y] != -1:
            rank_x = rankings[y] + c
            if 1 <= rank_x <= N and rankings[x] == -1:
                rankings[x] = rank_x
            else:
                return [-1] * N
        else:
            # どちらの順位もまだ決まっていない場合
            if 1 <= c + 1 <= N:
                rankings[x] = c + 1
                rankings[y] = 1
            else:
                return [-1] * N
    
    # 残りの人の順位を埋める
    for i in range(N):
        if rankings[i] == -1:
            rankings[i] = N
            break
    
    return rankings

# 入力例
N, M = [int(l) for l in input().split()]
constraints = []
for m in range(M):
    constraints.append([int(l) for l in input().split()])

# クエリを解く
results = solve_queries(N, M, constraints)
print(*results)