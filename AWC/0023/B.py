N = int(input())
person = 0
for n in range(N-1):
    a, b = map(int, input().split())
    person += a
    person = max(0, person - b)
person += int(input())
print(person)
