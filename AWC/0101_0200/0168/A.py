N = int(input())
S = input()
T = input()
count = 0
result = 0
for s, t in zip(S, T):
    if s != t:
        result = max(result, count)
        count = 0
    else:
        count += 1
print(max(result, count))
