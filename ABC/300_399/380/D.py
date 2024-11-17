S = input()
_ = int(input())
result = []
for k in [int(l) for l in input().split()]:
    result.append(S[(k - 1) % len(S)].swapcase() if ((k - 1) // len(S)).bit_count() % 2 else S[(k - 1) % len(S)])
print(*result)
