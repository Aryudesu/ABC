def calc(B, W):
    result = 0
    for idx in range(min([len(B), len(W)])):
        b = B[idx]
        w = W[idx]
        if b >= 0 and w >= 0:
            result += b
            result += w
        elif b <= 0 and b + w >= 0:
            result += b
            result += w
        else:
            if b > 0:
                result += b
            else:
                break
    if len(B) > len(W):
        for idx in range(len(W), len(B)):
            b = B[idx]
            if b > 0:
                result += b
    return result


N, M = [int(l) for l in input().split()]
B = [int(l) for l in input().split()]
W = [int(l) for l in input().split()]
B.sort(reverse=True)
W.sort(reverse=True)
print(calc(B, W))
