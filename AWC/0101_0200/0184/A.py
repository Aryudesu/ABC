"""
Author: Aryu
大抵のクラスは以下を参照
GitHub: https://github.com/Aryudesu/myLibrary
"""

N, C = map(int, input().split())
for _ in range(N):
    w, a = map(int, input().split())
    print(max(w * a - C, 0))
