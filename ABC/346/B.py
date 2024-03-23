def calc(W, B):
    C = W + B
    data = "wbwbwwbwbwbw" * C
    LD = len(data)
    w, b = 0, 0
    for i in range(LD - C):
        w = 0
        b = 0
        for j in range(i, i + C):
            if data[j] == "w":
                w += 1
            else:
                b += 1
        if w == W and b == B:
            return True
    return False

W, B = [int(l) for l in input().split()]
print("Yes" if calc(W, B) else "No")
