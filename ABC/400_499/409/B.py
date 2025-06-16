N = int(input())
A = [int(l) for l in input().split()]
# 答え
result = 0
# 答え全探索
for i in range(N+1):
    # カウント用
    count = 0
    # 全部の要素カウント
    for j in range(N):
        # 答え以上の数の個数カウント
        if i <= A[j]:
            count += 1
    if i <= count:
        result = max(result, i)
print(result)
