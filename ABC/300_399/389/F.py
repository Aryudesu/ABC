# 入力の読み取り
import sys

input = sys.stdin.read
data = input().split()

# 初期入力
N = int(data[0])
index = 1

# コンテストの範囲入力
MAX_RATING = 500000
change = [0] * (MAX_RATING + 2)

for _ in range(N):
    L, R = map(int, (data[index], data[index + 1]))
    change[L] += 1
    change[R + 1] -= 1
    index += 2

# クエリ入力
Q = int(data[index])
index += 1
queries = list(map(int, data[index:index + Q]))

# 累積和を計算
ratingIncrease = [0] * (MAX_RATING + 2)
for i in range(1, MAX_RATING + 1):
    ratingIncrease[i] = ratingIncrease[i - 1] + change[i]

# クエリごとに結果を計算
results = []
for X in queries:
    rating = X
    while rating <= MAX_RATING and ratingIncrease[rating] > 0:
        rating += ratingIncrease[rating]
    results.append(rating)

# 結果を出力
sys.stdout.write("\n".join(map(str, results)) + "\n")
