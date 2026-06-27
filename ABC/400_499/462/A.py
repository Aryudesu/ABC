S = input()
nums = set([str(i) for i in range(10)])
result = ""
for s in S:
    if s in nums:
        result += s
print(result)
