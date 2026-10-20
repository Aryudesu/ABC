# 大抵のクラスは以下を使用
# https://github.com/Aryudesu/myLibrary

N = int(input())
A = list(map(int, input().split()))
f = 0
result = []
for a in A:
    if not a and not f:
        f = 1
    result.append("ox"[f])
print("".join(result))
