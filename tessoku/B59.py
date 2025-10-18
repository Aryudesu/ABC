from atcoder.fenwicktree import FenwickTree

def inversion_count(arr: list) -> int:
    result = 0
    ft = FenwickTree(max(arr) + 1)
    for i, a in enumerate(arr):
        result += i - ft.sum(0, a + 1)
        ft.add(a, 1)
    return result


N = int(input())
print(inversion_count([int(l) for l in input().split()]))
