N, S, L = map(int, input().split())
A = list(map(int, input().split()))
left = [0]
right = [0]
for l in range(S-2, -1, -1):
    left.append(left[-1] + A[l])
for r in range(S-1, N-1):
    right.append(right[-1] + A[r])
result = 0
for lIdx in range(len(left)):
    for rIdx in range(len(right)):
        dist = min(left[lIdx] * 2 + right[rIdx], left[lIdx] + right[rIdx] * 2)
        if dist > L:
            break
        result = max(result, lIdx + rIdx + 1)
print(result)
