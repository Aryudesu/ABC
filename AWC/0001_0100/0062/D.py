N = int(input())
S = list(input())
S.reverse()
num = 0
b = 1
for i in range(N):
    if S[i] == "1":
        num += b
    b <<= 1
result = 0
# [l, r]について全走査   TLEすりゅぅ…
for l in range(N):
    for r in range(l, N):
        length = r - l + 1
        b = (1 << length) - 1
        target = (num >> (N - r - 1)) & b
        for idx in range(l+1, N):
            if idx + length - 1 >= N:
                break
            pattern = (num >> (N - (idx + length - 1) - 1)) & b
            f = (target ^ pattern)
            if f == 0:
                continue
            bc = (1 << (f.bit_length() - 1))
            if (target ^ pattern)^bc == 0:
                result += 1
print(result)
