# 大抵のクラスは以下を使用
# https://github.com/Aryudesu/myLibrary

N, C = map(int, input().split())
W = list(map(int, input().split()))
W.sort(reverse=True)
result = 0
weight = 0
while W:
    w = W.pop()
    if weight + w > C:
        W.append(w)
        break
    weight += w
    result += 1
result += len(W) > 0
print(result)
