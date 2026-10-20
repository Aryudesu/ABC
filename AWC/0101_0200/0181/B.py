# 大抵のクラスは以下を使用
# https://github.com/Aryudesu/myLibrary

H, W = map(int, input().split())
print(sum("x" not in input() for _ in range(H)))
