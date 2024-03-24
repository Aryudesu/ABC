def determine_one(N):
    result = 0
    for i in range(1, N):
        print(f"? {i + 1} {i + 1} {result + 1}")
        res = input()
        if res == "No":
            result = i
    return result


def is_bigger(one, i, j):
    print(f"? {i + 1} {one + 1} {j + 1}")
    return input() == "Yes"


def merge(one, A, B, left, mid, right):
    i = left
    j = mid
    k = 0
    while i < mid and j < right:
        k += 1
        if is_bigger(one, A[j], A[i]):
            i += 1
            B[k] = A[i]
        else:
            j += 1
    if i == mid:
        while j < right:
            k += 1
            j += 1
            B[k] = A[j]
    else:
        while i < mid:
            k += 1
            i += 1
            B[k] = A[i]
    for l in range(k):
        A[left + l] = B[l]
    return


def merge_sort(one, A, B, left, right):
    if left == right or left == right - 1:
        return
    mid = (left + right)//2
    merge_sort(one, A, B, left, mid)
    merge_sort(one, A, B, mid, right)
    merge(one, A, B, left, mid, right)


N = int(input())
one = determine_one(N)
A = [l for l in range(N)]
B = [0 for _ in range(N)]
merge_sort(one, A, B, 0, N)
print(*A)
