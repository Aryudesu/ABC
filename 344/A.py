S = input()
result = ""
mem = True
for s in S:
    if s == "|":
        mem = not mem
        continue
    if mem:
        result += s
print(result)
