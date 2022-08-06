def FullHouse(Card):
    if Card[0] == Card[1] and Card[3] == Card[4]:
        if Card[0] == Card[2] or Card[4] == Card[2]:
            return 'Yes'
    return 'No'


Card = [int(l) for l in input().split()]
Card.sort()
print(FullHouse(Card))
