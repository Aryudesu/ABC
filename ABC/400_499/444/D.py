from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))
data = defaultdict(int)
for a in A:
    data[a] += 1
s = len(A)
idx = 1
kuriagari = 0
result = []
while s > 0 or kuriagari > 0:
    result.append((kuriagari + s) % 10)
    kuriagari = (kuriagari + s) // 10
    s -= data[idx]
    idx += 1
result.reverse()
for r in result:
    print(r, end="")
print()
