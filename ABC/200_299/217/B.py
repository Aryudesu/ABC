data = {"ABC", "ARC", "AGC", "AHC"}
S = {input() for _ in range(3)}
for d in data:
    if not d in S:
        print(d)
        break
