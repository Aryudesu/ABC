def calc(a: int, b: int, c: int, d: int)->bool:
    return 2*a + c > 2*b + d

T = int(input())
result = []
for _ in range(T):
    a, b, c, d = map(int, input().split())
    result.append("Bob" if calc(a, b, c, d) else "Alice")
print(*result, sep="\n")
