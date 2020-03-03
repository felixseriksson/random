# Bridge Hand Simulator

deck = [52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
spades = [52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40]
hearts = [39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27]
diamonds = [26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14]
clubs = [13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
deckcard = {52: "A", 51: "K", 50: "Q", 49: "J", 48: "T", 47: "9", 46: "8", 45: "7", 44: "6", 43: "5", 42: "4", 41: "3", 40: "2", 39: "A", 38: "K", 37: "Q", 36: "J", 35: "T", 34: "9", 33: "8", 32: "7", 31: "6", 30: "5", 29: "4", 28: "3", 27: "2", 26: "A", 25: "K", 24: "Q", 23: "J", 22: "T", 21: "9", 20: "8", 19: "7", 18: "6", 17: "5", 16: "4", 15: "3", 14: "2", 13: "A", 12: "K", 11: "Q", 10: "J", 9: "T", 8: "9", 7: "8", 6: "7", 5: "6", 4: "5", 3: "4", 2: "3", 1: "2"}
north = []
northspades = []
northhearts = []
northdiamonds = []
northclubs = []
south = []
southspades = []
southhearts = []
southdiamonds = []
southclubs = []
east = []
eastspades = []
easthearts = []
eastdiamonds = []
eastclubs = []
west = []
westspades = []
westhearts = []
westdiamonds = []
westclubs = []

import random

random.shuffle(deck)

for card in random.sample(deck, k=13):                              # Dealing south hand
    south.append(card)

for card in deck:                                                   # Dealing north hand
    if card not in south:
        north.append(card)
    if len(north) == 13:
        break

for card in deck:                                                   # Dealing east hand
    if card not in south and card not in north:
        east.append(card)
    if len(east) == 13:
        break

for card in deck:                                                   # Dealing west hand
    if card not in south and card not in north and card not in east:
        west.append(card)
    if len(west) == 13:
        break

south.sort(reverse = True)                                                        # Sorting Hands
north.sort(reverse = True)
east.sort(reverse = True)
west.sort(reverse = True)

for card in south:
    if card in spades:
        southspades.append(card)
    elif card in hearts:
        southhearts.append(card)
    elif card in diamonds:
        southdiamonds.append(card)
    else:
        southclubs.append(card)

for card in north:
    if card in spades:
        northspades.append(card)
    elif card in hearts:
        northhearts.append(card)
    elif card in diamonds:
        northdiamonds.append(card)
    else:
        northclubs.append(card)

for card in east:
    if card in spades:
        eastspades.append(card)
    elif card in hearts:
        easthearts.append(card)
    elif card in diamonds:
        eastdiamonds.append(card)
    else:
        eastclubs.append(card)

for card in west:
    if card in spades:
        westspades.append(card)
    elif card in hearts:
        westhearts.append(card)
    elif card in diamonds:
        westdiamonds.append(card)
    else:
        westclubs.append(card)


print("North Hand:")
print(northspades)
print(northhearts)
print(northdiamonds)
print(northclubs)
print("South Hand:")                                                # Printing Hands
print(southspades)
print(southhearts)
print(southdiamonds)
print(southclubs)
print("East Hand:")
print(eastspades)
print(easthearts)
print(eastdiamonds)
print(eastclubs)
print("West Hand:")
print(westspades)
print(westhearts)
print(westdiamonds)
print(westclubs)

alltrick1 = []
trick1 = []
dealtrick1 = []
outputtrick1 = []


def comp4cards(hand1card, hand2card, hand3card, hand4card, alltrick, outputtrick, northhand, southhand, easthand, westhand, hand2cardvalue, hand3cardvalue, hand4cardvalue):
    ntc = 0
    stc = 0
    etc = 0
    wtc = 0
    dealtrick = []
    trick = []
    fulldeal = []
    if hand1card in westhand:
        if hand1card > hand2cardvalue and hand1card > hand3cardvalue and hand1card > hand4cardvalue:
            wtc += 1
        elif hand2cardvalue > hand3cardvalue and hand2cardvalue > hand4cardvalue:
            ntc += 1
        elif hand3cardvalue > hand4cardvalue:
            etc += 1
        else:
            stc += 1
    elif hand1card in northhand:
        if hand1card > hand2cardvalue and hand1card > hand3cardvalue and hand1card > hand4cardvalue:
            ntc += 1
        elif hand2cardvalue > hand3cardvalue and hand2cardvalue > hand4cardvalue:
            etc += 1
        elif hand3cardvalue > hand4cardvalue:
            stc += 1
        else:
            wtc += 1
    elif hand1card in easthand:
        if hand1card > hand2cardvalue and hand1card > hand3cardvalue and hand1card > hand4cardvalue:
            etc += 1
        elif hand2cardvalue > hand3cardvalue and hand2cardvalue > hand4cardvalue:
            stc += 1
        elif hand3cardvalue > hand4cardvalue:
            wtc += 1
        else:
            ntc += 1
    else:
        if hand1card > hand2cardvalue and hand1card > hand3cardvalue and hand1card > hand4cardvalue:
            stc += 1
        elif hand2cardvalue > hand3cardvalue and hand2cardvalue > hand4cardvalue:
            wtc += 1
        elif hand3cardvalue > hand4cardvalue:
            ntc += 1
        else:
            etc += 1
    trick.append(ntc)
    trick.append(stc)
    trick.append(etc)
    trick.append(wtc)
    alltrick.append(trick)
    for card in northhand:
        if not card == hand2card:
            dealtrick.append(card)
    fulldeal.append(dealtrick)
    dealtrick = []
    for card in southhand:
        if not card == hand4card:
            dealtrick.append(card)
    fulldeal.append(dealtrick)
    dealtrick = []
    for card in easthand:
        if not card == hand3card:
            dealtrick.append(card)
    fulldeal.append(dealtrick)
    dealtrick = []
    for card in westhand:
        if not card == hand1card:
            dealtrick.append(card)
    fulldeal.append(dealtrick)
    outputtrick.append(fulldeal)
    fulldeal = []
    dealtrick = []
    trick = []
    ntc = 0
    stc = 0
    etc = 0
    wtc = 0


def anysamesuit(hand1card, hand):
    return any(((card in spades and hand1card in spades) or (card in hearts and hand1card in hearts) or (card in diamonds and hand1card in diamonds) or (card in clubs and hand1card in clubs)) for card in hand)


def samesuit(hand1card, handcard):
    if handcard and hand1card in spades or handcard and hand1card in hearts or handcard and hand1card in diamonds or handcard and hand1card in clubs:
        return True
    else:
        return False


for hand1card in west:                                                                           # Trick 1 syntax start
    for hand2card in north:
        if anysamesuit(hand1card, north):
            if samesuit(hand1card, hand2card):
                for hand3card in east:
                    if anysamesuit(hand1card, east):
                        if samesuit(hand1card, hand3card):
                            for hand4card in south:
                                if anysamesuit(hand1card, south):
                                    if samesuit(hand1card, hand4card):
                                        comp4cards(hand1card, hand2card, hand3card, hand4card, alltrick1, outputtrick1, north, south, east, west, hand2card, hand3card, hand4card)
                                    else:
                                        continue
                                else:
                                    comp4cards(hand1card, hand2card, hand3card, hand4card, alltrick1, outputtrick1, north, south, east, west, hand2card, hand3card, 0)
                        else:
                            continue
                    else:
                        for hand4card in south:
                            if anysamesuit(hand1card, south):
                                if samesuit(hand1card, hand4card):
                                    comp4cards(hand1card, hand2card, hand3card, hand4card, alltrick1, outputtrick1, north, south, east, west, hand2card, 0, hand4card)
                                else:
                                    continue
                            else:
                                comp4cards(hand1card, hand2card, hand3card, hand4card, alltrick1, outputtrick1, north, south, east, west, hand2card, 0, 0)
            else:
                continue
        else:
            for hand3card in east:
                if anysamesuit(hand1card, east):
                    if samesuit(hand1card, hand3card):
                        for hand4card in south:
                            if anysamesuit(hand1card, south):
                                if samesuit(hand1card, hand4card):
                                    comp4cards(hand1card, hand2card, hand3card, hand4card, alltrick1, outputtrick1, north, south, east, west, 0, hand3card, hand4card)
                                else:
                                    continue
                            else:
                                comp4cards(hand1card, hand2card, hand3card, hand4card, alltrick1, outputtrick1, north, south, east, west, 0, hand3card, 0)
                    else:
                        continue
                else:
                    for hand4card in south:
                        if anysamesuit(hand1card, south):
                            if samesuit(hand1card, hand4card):
                                comp4cards(hand1card, hand2card, hand3card, hand4card, alltrick1, outputtrick1, north, south, east, west, 0, 0, hand4card)
                            else:
                                continue
                        else:
                            comp4cards(hand1card, hand2card, hand3card, hand4card, alltrick1, outputtrick1, north, south, east, west, 0, 0, 0)

                                                                                                               # Trick 1 syntax end
print("Possible outcomes of trick one [N, S, E, W]:")
print(alltrick1)
print(outputtrick1[0])
print("Number of possible outcomes of trick 1:")
print(len(alltrick1))
print(len(outputtrick1[0][0]))
print(len(outputtrick1[0][1]))
print(len(outputtrick1[0][2]))
print(len(outputtrick1[0][3]))
