N = int(input())
S = input()
memo = []
count = 0
for i in range(N):
    if S[i] == "0":
        memo.append(i)
        count += 1
data = list(range(count))
res = 0
for i in range(count):
    res += abs(memo[i] - data[i])
# print(res)
tmp = res
for i in range(count):
    tmp -= abs(memo[-i - 1] - data[-i - 1])
    data[-i - 1] = N - 1 - i
    tmp += abs(memo[-i - 1] - data[-i - 1])
    res = min([res, tmp])
print(res)
