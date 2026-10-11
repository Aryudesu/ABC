N = int(input())
A = list(map(int, input().split()))
c = 0
for a in A:
    c ^= a
print("Alice" if c else "Bob")
