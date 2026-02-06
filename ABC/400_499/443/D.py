def calc(N: int, R: list[int])->int:
    R_origin = R.copy()
    nums = [set() for _ in range(N)]
    for idx in range(N):
        nums[R[idx]].add(idx)
    for num in range(N):
        for idx in nums[num]:
            if idx + 1 < N:
                if R[idx+1] > num + 1:
                    nums[R[idx + 1]].discard(idx + 1)
                    nums[num + 1].add(idx + 1)
                    R[idx+1] = num + 1
            if idx - 1 >= 0:
                if R[idx-1] > num + 1:
                    nums[R[idx - 1]].discard(idx - 1)
                    nums[num + 1].add(idx - 1)
                    R[idx-1] = num + 1
    result = 0
    for idx in range(N):
        result += R_origin[idx] - R[idx]
    return result

result = []
T = int(input())
for _ in range(T):
    N = int(input())
    R = [int(l) - 1 for l in input().split()]
    res = calc(N, R)
    result.append(res)
for r in result:
    print(r)
