import random
import sys
import re
from matplotlib import pyplot as plt


def print_cards(raw_cards):
    new_cards = []
    for c in raw_cards:
        if int(getCardInfo(c)[1]) == 11:
            new_cards.append(getCardInfo(c)[0] + ": J")
        elif int(getCardInfo(c)[1]) == 12:
            new_cards.append(getCardInfo(c)[0] + ": Q")
        elif int(getCardInfo(c)[1]) == 13:
            new_cards.append(getCardInfo(c)[0] + ": K")
        elif int(getCardInfo(c)[1]) == 14:
            new_cards.append(getCardInfo(c)[0] + ": A")
        else:
            new_cards.append(getCardInfo(c)[0] + ": " + getCardInfo(c)[1])

    print(new_cards)


def cards(number_cards, cards_per_color):
    poker_cards = [None] * number_cards
    colors = ["red", "black", "yellow", "green"]
    run_colors = 0
    run_values = 2
    for i in range(0, number_cards):  # 2 ist die niedrigste Karte
        combine = colors[run_colors - 1] + ":" + str(run_values)
        poker_cards[i - 1] = combine
        if i % cards_per_color == 0:
            run_colors += 1
        run_values += 1
        if run_values == cards_per_color + 2:  # niedrigste bei 2
            run_values = 2
    return poker_cards


def ziehe(cards, howmany):
    poker_cards = cards(52, 13)
    for i in range(howmany):  # ziehen der Zufallskarten
        index = random.randrange(len(poker_cards) - i)
        last_pos = len(poker_cards) - 1 - i
        poker_cards[last_pos], poker_cards[index] = poker_cards[index], poker_cards[last_pos]

    print_cards(sorted(poker_cards[-howmany:], key=sortby))
    return sorted(poker_cards[-howmany:], key=sortby)


def sortby(x):
    try:
        return int(x.split(':')[1])
    except ValueError:
        return float('inf')


# ----------------Poker-Kombinationen---------------------
# https://de-academic.com/dic.nsf/dewiki/785079

def getCardInfo(card):
    info = card.split(':')
    # print(info)
    return info


def getCardValues(drawnCards):
    values = []
    for x in drawnCards:
        card_val = getCardInfo(x)[1]
        values.append(int(card_val))
    return values


def getCardColors(drawnCards):
    colors = []
    for x in drawnCards:
        color = getCardInfo(x)[0]
        colors.append(color)
    return colors


def isRoyalFlush(drawnCards):
    colors = getCardColors(drawnCards)
    values = getCardValues(drawnCards)
    if all(item == "yellow" for item in colors) and min(values) == 10:
        print("---------------------------------------------------------------------------------------")
        return True
    elif all(item == "red" for item in colors) and min(values) == 10:
        print("---------------------------------------------------------------------------------------")
        return True
    elif all(item == "green" for item in colors) and min(values) == 10:
        print("---------------------------------------------------------------------------------------")
        return True
    elif all(item == "black" for item in colors) and min(values) == 10:
        print("---------------------------------------------------------------------------------------")
        return True
    else:
        return False


def testRoyalFlush():
    for x in range(100000):
        cardss = ziehe(cards, 5)
        if isRoyalFlush(cardss):
            print("flush!")
            sys.exit()


def isStraightFlush(drawnCards):
    colors = getCardColors(drawnCards)
    values = getCardValues(drawnCards)
    if all(item == "yellow" for item in colors) and checkRow(values):
        return True
    if all(item == "red" for item in colors) and checkRow(values):
        return True
    if all(item == "green" for item in colors) and checkRow(values):
        return True
    if all(item == "black" for item in colors) and checkRow(values):
        return True
    return False


def checkRow(values):
    return sorted(values) == list(range(min(values), max(values) + 1))  # Überprüfen ob Werte in Reihe sind


def testStraightFlush():
    for x in range(100000):
        cardss = ziehe(cards, 5)
        if isStraightFlush(cardss):
            print(" straight flush!")
            sys.exit()


def isFourOfAKind(drawnCards):
    values = getCardValues(drawnCards)
    val_count = {card: values.count(card) for card in values}
    if 4 in val_count.values():
        return True
    return False


def testForOfAKind():
    for x in range(100000):
        drawn = ziehe(cards, 5)
        if isFourOfAKind(drawn):
            print("4 of a kind!")
            sys.exit()


def isFullHouse(drawnCards):
    values = getCardValues(drawnCards)
    val_count = {card: values.count(card) for card in values}
    if 3 in val_count.values() and 2 in val_count.values():
        return True
    return False


def testFullHouse():
    for x in range(100000):
        cardss = ziehe(cards, 5)
        if isFullHouse(cardss):
            print("Full House!")
            sys.exit()


def isFlush(drawnCards):
    colors = getCardColors(drawnCards)
    if all(item == "yellow" for item in colors) or \
       all(item == "red" for item in colors) or \
       all(item == "black" for item in colors) or \
       all(item == "yellow" for item in colors):
        return True
    else:
        return False


def testIsFlush():
    for x in range(100000):
        drawn = ziehe(cards, 5)
        if isFlush(drawn):
            print("Flush!")
            sys.exit()


def isStraight(drawnCards):
    colors = getCardColors(drawnCards)
    values = getCardValues(drawnCards)
    if not all(x == colors for x in colors) and checkReihe(values):
        return True

    return False


def testIsStraight():
    for x in range(100000):
        drawn = ziehe(cards, 5)
        if isStraight(drawn):
            print("Straight!")
            sys.exit()


def isTriplet(nrTriplets, drawnCards):
    values = getCardValues(drawnCards)

    sum_triplets = 0
    val_count = {card: values.count(card) for card in values}
    for x in val_count.values():
        if x == 3:
            sum_triplets += 1

    if sum_triplets == nrTriplets:
        return True

    return False


def testIsTriplet():
    for x in range(100000):
        drawn = ziehe(cards, 5)
        if isTriplet(drawn):
            print("Triplet!")
            sys.exit()


def isTwoPair(drawnCards):
    values = getCardValues(drawnCards)
    val_count = {card: values.count(card) for card in values}
    sum_pairs = 0
    for x in val_count.values():
        if x == 2:
            sum_pairs += 1
    if sum_pairs == 2:
        return True

    return False


def testIsTwoPair():
    for x in range(100000):
        drawn = ziehe(cards, 5)
        if isTwoPair(drawn):
            print("Pair!")
            sys.exit()


def isPair(drawnCards):
    colors = getCardColors(drawnCards)
    values = getCardValues(drawnCards)

    val_count = {card: values.count(card) for card in values}
    sum_pairs = 0
    for x in val_count.values():
        if x == 2:
            sum_pairs += 1
    if sum_pairs == 1:
        return True
    return False


def testIsPair():
    for x in range(100000):
        drawn = ziehe(cards, 5)
        if isPair(drawn):
            print("Pair!")
            sys.exit()


def isPairVar(nrPairs, drawnCards):
    values = getCardValues(drawnCards)
    val_count = {card: values.count(card) for card in values}
    sum_pairs = 0
    for x in val_count.values():
        if x == 2:
            sum_pairs += 1
    if sum_pairs == nrPairs:
        return True
    return False


def isHighestCard(drawnCards):
    if not isPair(drawnCards) and not isTwoPair(drawnCards) and not isTriplet(drawnCards) and not isFlush(drawnCards) \
            and not isRoyalFlush(drawnCards) and not isStraightFlush(drawnCards) and not isFourOfAKind(drawnCards) \
            and not isStraight(drawnCards):
        return drawnCards[4]


def testHighestCard():
    for x in range(100000):
        drawn = ziehe(cards, 5)
        if isHighestCard(drawn):
            print("HighestCard!: " + isHighestCard(drawn))
            sys.exit()


def stats(howOften, nr_cards):
    sum_OnePair = sum_TwoPair = sum_Triple = sum_FourOfAKind0 = sum_Flush = sum_StraightFlush = sum_RoyalFlush
    = sum_FullHouse = sum_Straight = 0
    for x in range(howOften):
        cardss = ziehe(cards, nr_cards)
        if isPairVar(1, cardss):
            sum_OnePair += 1
        if isPairVar(2, cardss):
            sum_TwoPair += 1
        if isTriplet(1, cardss):
            sum_Triple += 1
        if isFlush(cardss):
            sum_Flush += 1
        if isFourOfAKind(cardss):
            sum_FourOfAKind += 1
        if isStraightFlush(cardss):
            sum_StraightFlush += 1
        if isRoyalFlush(cardss):
            sum_RoyalFlush += 1
        if isFullHouse(cardss):
            sum_FullHouse += 1
        if isStraight(cardss):
            sum_Straight += 1

        prop_OnePair = sum_OnePair / howOften * 100
        prop_TwoPair = sum_TwoPair / howOften * 100
        prop_Triple = sum_Triple / howOften * 100
        prop_FourOfAKind = sum_FourOfAKind / howOften * 100
        prop_Flush = sum_Flush / howOften * 100
        prop_StraightFlush = sum_StraightFlush / howOften * 100
        prop_RoyalFlush = sum_RoyalFlush / howOften * 100
        prop_FullHouse = sum_FullHouse / howOften * 100
        prop_Straight = sum_Straight / howOften * 100

    print("-----------------------------------------------------------------")
    print("Number of drawn cards: ", nr_cards)
    print("Number of Rounds: ", howOften)
    print("One-Pair: ", str(prop_OnePair))
    print("Two-Pair: ", str(prop_TwoPair))
    print("Triple: ", str(prop_Triple))
    print("Four-Of-A-Kind: ", str(prop_FourOfAKind))
    print("Flush: ", str(prop_Flush))
    print("Straight-Flush: ", str(prop_StraightFlush))
    print("Royal-Flush: ", str(prop_RoyalFlush))
    print("Full-House: ", str(prop_FullHouse))
    print("Straight: ", str(prop_Straight))

    x = ["One-Pair", "Two-Pair", "Triple", "Four-Of-A-Kind", "Flush", "Straight-Flush", "Royal-Flush",
         "Full-House", "Straight"]
    y = [prop_OnePair, prop_TwoPair, prop_Triple, prop_FourOfAKind, prop_Flush, prop_StraightFlush,
         prop_RoyalFlush, prop_FullHouse, prop_Straight]
    plt.bar(x, y, align="center")
    plt.title("Poker-Combinations")
    plt.xlabel("Combination")
    plt.ylabel("Probability in %")
    plt.xticks(rotation=90)
    plt.show()


if __name__ == '__main__':
    stats(100000, 5)
