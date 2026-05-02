from atcoder.fenwicktree import FenwickTree

def inversion_count(arr: list) -> int:
    """転倒数を計算します"""
    result = 0
    ft = FenwickTree(max(arr) + 1)
    for i, a in enumerate(arr):
        result += i - ft.sum(0, a + 1)
        ft.add(a, 1)
    return result

N = int(input())
vIdx = []
pIdx = []
nums = [-1] * N
for n in range(N):
    p, v = map(int, input().split())
    vIdx.append((v, n))
    pIdx.append((p, n))
vIdx.sort()
pIdx.sort()
for n in range(N):
    v, i = vIdx[n]
    nums[i] = n
sortData = [-1] * N
for n in range(N):
    p, i = pIdx[n]
    sortData[n] = nums[i]
print(inversion_count(sortData))
