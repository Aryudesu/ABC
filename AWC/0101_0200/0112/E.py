from atcoder.fenwicktree import FenwickTree

def inversion_count(arr: list) -> int:
    """転倒数を計算します"""
    result = 0
    ft = FenwickTree(max(arr) + 1)
    for i, a in enumerate(arr):
        result += i - ft.sum(0, a + 1)
        ft.add(a, 1)
    return result


N, K = map(int, input().split())
P = list(map(int, input().split()))
res = inversion_count(P)
if res > K:
    print(res - K)
else:
    print((K - res) % 2)
