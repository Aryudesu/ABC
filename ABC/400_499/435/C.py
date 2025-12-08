N = int(input())
A = list(map(int, input().split()))
# 1番目のドミノを倒す
M = 0 + A[0]
count = 1
for i in range(1, N):
    # print(i, M)
    if M <= i:
        break
    M = max(i + A[i], M)
    count += 1
print(count)
