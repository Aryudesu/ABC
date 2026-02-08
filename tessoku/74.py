from atcoder.fenwicktree import FenwickTree

def inversion_count(arr: list) -> int:
    result = 0
    ft = FenwickTree(max(arr) + 1)
    for i, a in enumerate(arr):
        result += i - ft.sum(0, a + 1)
        ft.add(a, 1)
    return result

N = int(input())
HData = [None] * N
WData = [None] * N
for h in range(N):
    tmp = list(map(int, input().split()))
    for w in range(N):
        if tmp[w] != 0:
            HData[h] = tmp[w]-1
            WData[w] = tmp[w]-1
print(inversion_count(HData) + inversion_count(WData))
