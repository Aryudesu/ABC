match input():
    case "B":
        print("Y")
    case "Y":
        print("R")
    case "R":
        print("B")
    case _:
        raise ValueError()
