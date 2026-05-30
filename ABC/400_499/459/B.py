def trans(s: str)->str:
    if s in "abc":
        return "2"
    if s in "def":
        return "3"
    if s in "ghi":
        return "4"
    if s in "jkl":
        return "5"
    if s in "mno":
        return "6"
    if s in "pqrs":
        return "7"
    if s in "tuv":
        return "8"
    if s in "wxyz":
        return "9"
    raise ValueError()

N = int(input())
S = input().split()
result = ""
for s in S:
    result += trans(s[0])
print(result)
