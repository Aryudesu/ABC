from fractions import Fraction

class Point:
    def __init__(self, x: int, y: int):
        self.x = Fraction(x, 1)
        self.y = Fraction(y, 1)

    def __repr__(self):
        return f"{self.x} {self.y}"

class Line:
    def __init__(self, p1: Point, p2: Point):
        if p1.x != p2.x:
            self.a = (p1.y - p2.y)/(p1.x - p2.x)
            self.b = p1.y - self.a * p1.x
        else:
            self.a = None
            self.b = p1.x
    
    def crossPoint(self, other: "Line")->Point|None:
        if self.a is None and other.a is None:
            if self.b == other.b:
                return self.b
            else:
                return None
        if self.a is None:
            return other.b
        if other.a is None:
            return self.b
        if self.b == other.b:
            return self.b
        x = (other.b - self.b)/(self.a - other.a)
        y = (self.a * other.b - other.a * self.b)/(self.a - other.a)
        return Point(x, y)

x1, y1 = [int(l) for l in input().split()]
x2, y2 = [int(l) for l in input().split()]
x3, y3 = [int(l) for l in input().split()]
x4, y4 = [int(l) for l in input().split()]
l1 = Line(Point(x1, y1), Point(x2, y2))
l2 = Line(Point(x3, y3), Point(x4, y4))
p = l1.crossPoint(l2)
f = False
if isinstance(p, Fraction):
    f = True
elif isinstance(p, Point):
    if min(x1, x2) <= p.x <= max(x1, x2) and min(x3, x4) <= p.x <= max(x3, x4):
        if min(y1, y2) <= p.y <= max(y1, y2) and min(y3, y4) <= p.y <= max(y3, y4):
            f = True
print("Yes" if f else "No")
