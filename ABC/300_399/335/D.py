N = int(input())
M = N * N - 1
field = []
for n in range(N):
    field.append([None for _ in range(N)])
field[(N-1)//2][(N-1)//2] = "T"
field[0][0] = "1"
pos_x = 0
pos_y = 0
d = 0
count = 2
while count <= M:
    while True:
        new_pos_x = pos_x
        new_pos_y = pos_y
        if d == 0:
            new_pos_x = pos_x + 1
        elif d == 1:
            new_pos_y = pos_y + 1
        elif d == 2:
            new_pos_x = pos_x - 1
        elif d == 3:
            new_pos_y = pos_y - 1
        if new_pos_x < 0 or new_pos_x >= N or new_pos_y < 0 or new_pos_y >= N:
            d = (d + 1) % 4
        elif field[new_pos_y][new_pos_x] is None:
                break
        else:
            d = (d + 1) % 4
    pos_x = new_pos_x
    pos_y = new_pos_y
    field[pos_y][pos_x] = str(count)
    count += 1
for f in field:
    print(" ".join(f))
