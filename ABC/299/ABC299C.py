N = int(input())
S = input()
count = 0
max_count = 0
head = S[0] == "-"
for s in S:
    if s == "o":
        count += 1
    elif s == "-":
        if max_count < count:
            max_count = count
        count = 0
if head:
    if max_count < count:
        max_count = count
print(max_count if max_count else -1)
