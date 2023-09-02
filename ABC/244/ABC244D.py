def takahashi(R, G, B, AR, AG, AB):
    if R == AR and G != AG and B != AB:
        print("No")
        return
    if G == AG and R != AR and B != AB:
        print("No")
        return
    if B == AB and R != AR and G != AG:
        print("No")
        return
    print("Yes")
    return


R, G, B = input().split()
AR, AG, AB = input().split()
takahashi(R, G, B, AR, AG, AB)
