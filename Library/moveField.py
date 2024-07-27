class Field:
    def __init__(self, H=1, W=1, field=[]) -> None:
        self.H = H
        self.W = W
        self.field = field
        self.pos = (0, 0)
        self.command = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}

    def put_pos(self, pos):
        self.pos = pos

    def canMove(self, pos, dpos):
        """posからdposに移動"""
        y = pos[0] + dpos[0]
        x = pos[1] + dpos[1]
        if y >= H or y < 0 or x >= W or x < 0:
            return False
        if not self.isOk(y, x):
            return False
        return True

    def move(self, c):
        command = self.command.get(c, (0, 0))
        if self.canMove(self.pos, command):
            self.pos = (self.pos[0] + command[0], self.pos[1] + command[1])

    def isOk(self, y, x):
        return self.field[y][x] != "#"

    def getPos(self):
        return self.pos

H, W = [int(l) for l in input().split()]
pos = tuple([int(l) - 1 for l in input().split()])

C = [input() for _ in range(H)]
X = input()
field = Field(H, W, C)
field.put_pos(pos)
for x in X:
    field.move(x)
res = field.getPos()
print(res[0] + 1, res[1] + 1)
