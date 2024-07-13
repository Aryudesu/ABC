def calc():
    xA, yA = [int(l) for l in input().split()]
    xB, yB = [int(l) for l in input().split()]
    xC, yC = [int(l) for l in input().split()]
    mnAB = (yA - yB)
    mdAB = (xA - xB)
    mnBC = (yB - yC)
    mdBC = (xB - xC)
    mnAC = (yA - yC)
    mdAC = (xA - xC)
    if mnAB * mnBC == -mdAB * mdBC:
        return True
    if mnAB * mnAC == -mdAB * mdAC:
        return True
    if mnBC * mnAC == -mdBC * mdAC:
        return True
    return False


print("Yes" if calc() else "No")
