N, Q = map(int, input().split())
S = input()
T = list(map(int, input().split()))
nums = []
memo = []
s = 0
counts = [0] * (N + 1)
mx = 0
for idx in range(N):
    match S[idx]:
        case "(":
            s += 1
            counts[s] += 1
        case ")":
            if s == 0:
                s = 1
            else:
                s -= 1
        case _:
            raise ValueError()
    mx = max(mx, s)
    nums.append(s)

data = [0] * (N + 1)
for n in range(2, N):
    for m in range(n, mx + 1, n):
        data[n] += counts[m]
# print(counts)
# print(data)
# print(nums)
result = []
for t in T:
    if t == 1:
        result.append(N)
        continue
    else:
        result.append(data[t])
print(*result, sep="\n")
# ああああああああ無理だあああああああああああああああorz
