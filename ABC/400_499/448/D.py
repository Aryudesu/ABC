from collections import defaultdict
import pypyjit
import sys
sys.setrecursionlimit(10**6)
pypyjit.set_param('max_unroll_recursion=-1')
N = int(input())
A = list(map(int, input().split()))
graph = defaultdict(list)
for n in range(N-1):
    u, v = map(int, input().split())
    graph[u-1].append(v-1)
    graph[v-1].append(u-1)
RESULT = [False] * N
def dfs(graph: dict[int, list[int]], nowNode: int, memo: set, nums: dict[int, int], numList: list[int], isDup: bool):
    nextNodes = graph[nowNode]
    for nextNode in nextNodes:
        if nextNode in memo:
            continue
        isOk = False
        tmp = nums.get(numList[nextNode], 0)
        if tmp > 0:
            isOk = True
        RESULT[nextNode] = isDup or isOk
        nums[numList[nextNode]] = tmp + 1
        memo.add(nextNode)
        dfs(graph, nextNode, memo, nums, numList, isDup or isOk)
        nums[numList[nextNode]] = tmp
        memo.discard(nextNode)

nums = {A[0]:1}
memo = {0}
dfs(graph, 0, memo, nums, A, False)
for r in RESULT:
    print("Yes" if r else "No")
