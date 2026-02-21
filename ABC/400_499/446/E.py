from typing import Tuple
import sys
sys.setrecursionlimit(10**6)

def dfs(node: int, M: int, mTimesMemo: list[bool], memo: set[int])->bool:
    s1, s2 = node//M, node%M
    s3 = (A * s2 + B * s1) % M
    if node in memo:
        if mTimesMemo[node] is None:
            mTimesMemo[node] = False
            memo.add(node)
            return False
        return mTimesMemo[node]
    memo.add(node)
    if s1 == 0 or s2 == 0:
        mTimesMemo[node] = True
        return True
    nextNode = s2 * M + s3
    if mTimesMemo[node] is None:
        res = dfs(nextNode, M, mTimesMemo, memo)
        mTimesMemo[node] = res
    return mTimesMemo[node]

def xy2num(x: int, y: int, M: int)-> int:
    return x * M + y

def num2xy(num: int, M: int)-> Tuple[int, int]:
    return (num//M, num%M)

M, A, B = map(int, input().split())
mTimesMemo = [None] * (M * M)
memo = set()
for n in range(M*M):
    dfs(n, M, mTimesMemo, memo)
print(mTimesMemo.count(False))
