def calc(N: int)->int:
    result  = (N//3) + (N//5) + (N//7)
    result -= (N//15) + (N//21) + (N//35)
    result += (N//105)
    return result

print(calc(int(input())))
