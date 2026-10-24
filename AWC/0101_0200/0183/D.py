"""
Author: Aryu
大抵のクラスは以下を参照
GitHub: https://github.com/Aryudesu/myLibrary
"""

N, M, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort(reverse=True)
result = 0
count = 0
idx = 0
for b in B:
    if len(A) <= idx:
        break
    while len(A) > idx:
        if A[idx] < b:
            if count < K:
                count += 1
                A.pop()
            else:
                idx += 1
        else:
            result += 1
            break
print(result)
