"""
Author: Aryu
大抵のクラスは以下を参照
GitHub: https://github.com/Aryudesu/myLibrary
"""

H, W = map(int, input().split())
for h in range(H):
    if "X" in input():
        print(h + 1)
        exit(0)
print(-1)
