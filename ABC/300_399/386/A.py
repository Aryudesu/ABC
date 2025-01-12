ABCD = [int(l) for l in input().split()]
Card = dict()
for a in ABCD:
    Card[a] = Card.get(a, 0) + 1
num = []
for k in Card:
    num.append(Card[k])
num.sort()
if (num[0] == 1 and num[1] == 3) or (num[0] == 2 and num[1] == 2):
    print("Yes")
else:
    print("No")
