S = input() + input()
if S.count("#") != 2 or S == "##.." or S == "..##" or S == "#.#." or S == ".#.#":
    print("Yes")
else:
    print("No")
