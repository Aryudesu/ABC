H, W = [int(l) for l in input().split()]
start = [0, 0]
goal = [0, 0]
C = 0
for h in range(H):
    S = input()
    for n in range(len(S)):
        if C == 0:
            if S[n] == 'o':
                start = [h, n]
                C = 1
        elif C == 1:
            if S[n] == 'o':
                goal = [h, n]
                C = 2
res = abs(start[0] - goal[0]) + abs(start[1] - goal[1])
print(res)
