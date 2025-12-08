import sys
sys.setrecursionlimit(10**6)

def calc(S: str, start: int, operator: str, result: list[str])-> int:
    idx = start
    num = ""
    while idx < len(S):
        if S[idx] == "+" or S[idx] == "-" or S[idx] == "*" or S[idx] == "/":
            idx = calc(S, idx + 1, S[idx], result)
            appended = True
        elif S[idx] == "(":
            result.append("(")
        elif S[idx] == ")":
            result.append(num)
            result.append(")")
            return idx
        elif S[idx] == ",":
            # print(S[idx], appended, operator)
            result.append(num)
            result.append(operator)
            appended = True
            num = ""
        else:
            num += S[idx]
        idx += 1

S: str = input()
result = []
if S[0] == "+" or S[0] == "-" or S[0] == "*" or S[0] == "/":
    calc(S, 0, "", result)
else:
    result.append(S)
print("".join(result))
