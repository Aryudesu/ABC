N, X = [int(l) for l in input().split()]
AB = []
for n in range(N):
    AB.append([int(l) for l in input().split()])

min = (2*(10**9))*(10**9)
tmp = 0
for n in range(N):
    if X < n:
        break
    tmp += AB[n][0] + AB[n][1]
    tmp_ = tmp + (X - n - 1) * AB[n][1]
    if min > tmp_:
        min = tmp_
print(min)
