N, M, K = map(int, input().split())
A = list(map(int, input().split()))
UVB = []
for m in range(M):
    u, v, b = map(int, input().split())
    UVB.append(((1 << (u-1)) | (1 << (v-1)), b))
VALUE = [0] * (1 << N)
for mask in range(1 << N):
    tmp = 0
    for n in range(N):
        if (1 << n) & mask:
            tmp += A[n]
    VALUE[mask] = tmp
result = -(10 ** 18)
for mask in range(1 << N):
    if mask.bit_count() != K:
        continue
    minus = 0
    for m, b in UVB:
        if mask & m == m:
            minus += b
    result = max(result, VALUE[mask] - minus)
print(result)
