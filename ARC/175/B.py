N, A, B = [int(l) for l in input().split()]
S = [1 if l == "(" else -1 for l in input()]
Base = 0
c = 0
result = 0
for idx in range(2 * N):
    c += S[idx]
# )と(を入れ替えても良いから統一したい
if c > 0:
    S.reverse()
    S = [-s for s in S]
if c != 0:
    # 変えないと不釣り合いにやるやつ
    bNum = abs(c//2)
    # どこを変えるか　とりあえず悪いカッコ列の原因を潰したい
    d = 0
    co = 0
    for idx in range(2 * N):
        d += S[idx]
        if d < 0:
            S[idx] = -S[idx]
            d += 2
            co += 1
            result += B
            if co == bNum:
                break
minusMin = 0
# print(S)
# print(result)
e = 0
for s in S:
    e += s
    if e < 0:
        minusMin = min([minusMin, e])
# print(minusMin)
# print(((-minusMin) // 2) + ((-minusMin) % 2))
tmp1 = (((-minusMin) // 2) + ((-minusMin) % 2)) * A
tmp2 = (((-minusMin) // 2) + ((-minusMin) % 2)) * 2 * B
# print(tmp1, tmp2)
result += min([tmp1, tmp2])
print(result)
