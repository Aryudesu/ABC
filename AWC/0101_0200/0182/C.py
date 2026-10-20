# 大抵のクラスは以下を使用
# https://github.com/Aryudesu/myLibrary
N, K = map(int, input().split())
BA = []
check = 0
for _ in range(N):
    a, b = map(int, input().split())
    BA.append((b, a))
    check += a
if check < K:
    print(-1)
    exit(0)
BA.sort(reverse=True)
c = K
result = 0
for b, a in BA:
    co = min(c, a)
    result += co * b
    c -= co
    if not co:
        break
print(result)
