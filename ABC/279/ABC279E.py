N, M = [int(l) for l in input().split()]
A = [int(l) for l in input().split()]
all_one = 1
rev_res = []
# 一旦すべての場合
for m in range(M):
    if A[m] == all_one:
        all_one = A[m] + 1
    elif A[m] + 1 == all_one:
        all_one = A[m]
# 逆順に考える
# 最後の到達点
nums = {k + 1: k + 1 for k in range(N)}
one = all_one
for m in range(M):
    a = A[-1 - m]
    # 1つ前の状態
    if a + 1 == one:
        one = a
    elif a == one:
        one = a + 1
    rev_res.append(nums[one])
    nums[a], nums[a + 1] = nums[a + 1], nums[a]

rev_res.reverse()
for r in rev_res:
    print(r)
