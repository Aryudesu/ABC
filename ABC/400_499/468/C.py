def nextPermutation(data):
    """next_permutation"""
    size = len(data)
    left = size - 2
    while left >= 0 and data[left] >= data[left + 1]:
        left -= 1
    if left < 0:
        return 0
    right = size - 1
    while data[left] >= data[right]:
        right -= 1
    data[left], data[right] = data[right], data[left]
    left += 1
    right = size - 1
    while left < right:
        data[left], data[right] = data[right], data[left]
        left += 1
        right -= 1
    return 1

N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))
count = 0
nextPermutation(P)
while P < Q:
    nextPermutation(P)
    count += 1
print(count)
