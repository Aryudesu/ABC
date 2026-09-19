def maxSubarraySum(A: list[int], allowEmpty: bool = False) -> int:
    """
    最大連続部分列和を求める。

    Args:
        A:
            対象の配列。
        allowEmpty:
            True の場合は空区間を許し、答えは 0 以上になる。
            False の場合は 1 個以上の要素を選ぶ。

    Returns:
        最大連続部分列和。

    計算量:
        O(N)
    """
    if not A:
        if allowEmpty:
            return 0
        raise ValueError("A must not be empty")

    if allowEmpty:
        ans = 0
        current = 0

        for x in A:
            current = max(0, current + x)
            ans = max(ans, current)

        return ans

    ans = A[0]
    current = A[0]

    for x in A[1:]:
        current = max(x, current + x)
        ans = max(ans, current)

    return ans

N = int(input())
A = [int(l) - 1 for l in input().split()]
print(maxSubarraySum(A))
