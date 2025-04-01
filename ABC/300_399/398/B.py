def calc(card):
    if len(card) < 2:
        return False
    othree = set()
    otwo = set()
    for a in card:
        if card[a] >= 3:
            othree.add(a)
            otwo.add(a)
        if card[a] >= 2:
            otwo.add(a)
    return len(othree) >= 1 and len(otwo) >= 2

A = [int(l) for l in input().split()]
card = dict()
for a in A:
    card[a] = card.get(a, 0) + 1
print("Yes" if calc(card) else "No")
