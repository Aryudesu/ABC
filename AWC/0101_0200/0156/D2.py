N = int(input())
A = [int(input()) for _ in range(N)]
SA = sum(A)
mask = (1 << (SA // 2 + 1)) - 1
data = 1
for a in A:
    data = (data | (data << a)) & mask
print(data.bit_length() - 1)
# 通ってくれ
