N = int(input())
A = [int(l) for l in input().split()]
A.sort()
num = []
memo = set()
data = dict()
for a in A:
    data[a] = data.get(a, 0) + 1
    if not a in memo:
        num.append(a)
        memo.add(a)
result = 0
for n in num:
    if n < 50000:
        m = 100000 - n
        result += data.get(m, 0) * data.get(n, 0)
    elif n == 50000:
        m = data.get(n, 0)
        if m != 0:
            result += (m * (m - 1)) // 2
        break
print(result)
