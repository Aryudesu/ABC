# 大抵のクラスは以下を使用
# https://github.com/Aryudesu/myLibrary

N = int(input())
for _ in range(N):
    a, b = map(int, input().split())
    if a == b:
        print("Balanced")
    elif a > b:
        print("Left")
    else:
        print("Right")
