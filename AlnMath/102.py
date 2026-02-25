N = int(input())
C = list(input())
while len(C) > 1:
    nextC = []
    for i in range(len(C)-1):
        if C[i] == "W" and C[i+1] == "W":
            nextC.append("W")
        elif C[i] == "W" and C[i+1] == "R":
            nextC.append("B")
        elif C[i] == "W" and C[i+1] == "B":
            nextC.append("R")
        elif C[i] == "B" and C[i+1] == "W":
            nextC.append("R")
        elif C[i] == "B" and C[i+1] == "R":
            nextC.append("W")
        elif C[i] == "B" and C[i+1] == "B":
            nextC.append("B")
        elif C[i] == "R" and C[i+1] == "W":
            nextC.append("B")
        elif C[i] == "R" and C[i+1] == "R":
            nextC.append("R")
        elif C[i] == "R" and C[i+1] == "B":
            nextC.append("W")
    C = nextC
print(C[0])
