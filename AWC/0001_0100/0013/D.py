def calcDissSum(nums: list[int])->int:
    nums.sort()
    N = len(nums)
    r = sum(nums)
    l = 0
    res = 0
    for idx in range(N):
        n = nums[idx]
        res += (r - n * (N-idx)) + (idx * n - l)
        # print("debug", l, r)
        r -= n
        l += n
    return res

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
B = []
for i in range(M):
    tmp = []
    for j in range(N):
        tmp.append(A[j][i])
    B.append(tmp)
result = 0
for b in B:
    result += calcDissSum(b)
print(result//2)
