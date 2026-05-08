from sortedcontainers import SortedList

N = int(input())
A = list(map(int, input().split()))
indexes = SortedList(range(N))
nums = A[:]
data = SortedList()
for i in range(N-1):
    data.add((A[i] + A[i+1], i, i + 1))
result = 0
while len(data) > 0:
    n, l, r = data.pop(0)
    result += n
    newNum = n
    lIdx = indexes.bisect_left(l)
    if lIdx - 1 >= 0:
        ll = indexes[lIdx - 1]
        lNum = nums[l] + nums[ll]
        data.discard((lNum, ll, l))
        data.add((newNum + nums[ll], ll, l))
    rIdx = indexes.bisect_left(r)
    if rIdx + 1 < len(indexes):
        rr = indexes[rIdx + 1]
        rNum = nums[r] + nums[rr]
        data.discard((rNum, r, rr))
        data.add((newNum + nums[rr], l, rr))
    nums[l], nums[r] = newNum, 0
    indexes.discard(r)
print(result)
