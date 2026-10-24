"""
Author: Aryu
大抵のクラスは以下を参照
GitHub: https://github.com/Aryudesu/myLibrary
"""

A, B, K = map(int, input().split())
print(max(K * (A - B), 0))

