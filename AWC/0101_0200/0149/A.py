H, W = map(int, input().split())
R, C = map(int, input().split())
S = [input() for _ in range(R)]
field = [[False] * W for _ in range(H)]
N = int(input())
for _ in range(N):
    r, c = map(int, input().split())
    r, c = r-1, c-1
    for dh in range(R):
        for dw in range(C):
            if not (0 <= r + dh < H):
                continue
            if not (0 <= c + dw < W):
                continue
            if S[dh][dw] == "#":
                field[r + dh][c + dw] = True
for fld in field:
    res = ""
    for f in fld:
        res += "#" if f else "."
    print(res)

