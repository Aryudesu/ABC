A, B, C, D, E, F = [int(l) * 2 for l in input().split()]
G, H, I, J, K, L = [int(l) * 2 for l in input().split()]
# 中心
X1, Y1, Z1 = [(A + D) // 2, (B + E) // 2, (C + F) // 2]
X2, Y2, Z2 = [(G + J) // 2, (H + K) // 2, (I + L) // 2]
# 2つの中心 < 辺の長さ/2
if abs(X1 - X2) < (abs(A - D) + abs(G - J)) // 2 and abs(Y1 - Y2) < (abs(B - E) + abs(H - K)) // 2 and abs(Z1 - Z2) < (abs(C - F) + abs(I - L)) // 2:
    print("Yes")
else:
    print("No")

