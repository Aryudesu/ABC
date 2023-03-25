N = int(input())
SP = []
sm = 0
for n in range(N):
    s, p = [l for l in input().split()]
    sm += int(p)
    SP.append([int(p), s])
SP.sort(reverse=True)
print(SP[0][1] if 2 * SP[0][0] > sm else "atcoder")
