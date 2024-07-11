N = int(input())
S = input()
zeros, ones, result = 0, 0, 0
for s in S:
    if s == "0":
        result += ones + zeros
        zeros, ones = 1, ones + zeros
    elif s == "1":
        result += zeros + 1
        zeros, ones = ones + 1, zeros
print(result)
