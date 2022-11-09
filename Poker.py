import random
import sys
import re
from matplotlib import pyplot as plt


def print_cards(raw_cards, cards_in_total):
    # Method which prints the drawn cards to make them more easier to read
    new_cards = []
    cards_per_color = cards_in_total / 4
    for c in raw_cards:
        # lowest card has value of 2 --> + 1
        if int(getCardInfo(c)[1]) == cards_per_color + 1 - 3:
            new_cards.append(getCardInfo(c)[0] + ": J")
        elif int(getCardInfo(c)[1]) == cards_per_color + 1 - 2:
            new_cards.append(getCardInfo(c)[0] + ": Q")
        elif int(getCardInfo(c)[1]) == cards_per_color + 1 - 1:
            new_cards.append(getCardInfo(c)[0] + ": K")
        elif int(getCardInfo(c)[1]) == cards_per_color + 1:
            new_cards.append(getCardInfo(c)[0] + ": A")
        else:
            new_cards.append(getCardInfo(c)[0] + ": " + getCardInfo(c)[1])

    print(new_cards)


def cards(cards_in_total):
    # Method which creates a list that contains all
    # possible cards in a poker card-deck
    poker_cards = [None] * cards_in_total
    cards_per_color = cards_in_total / 4
    colors = ["diamond", "heart", "spade", "clover"]
    run_colors = 0
    run_values = 2
    for i in range(0, cards_in_total):
        # combine a color and a value to a new card
        combine = colors[run_colors - 1] + ":" + str(run_values)
        # assign the new card to the list
        poker_cards[i] = combine
        # if we reach the highest number of a color --> next color
        if i % cards_per_color == 0:
            run_colors += 1
        run_values += 1
        if run_values == cards_per_color + 2:
            # lowest card has value of 2 --> + 2
            run_values = 2
    return poker_cards


def draw(all_cards, howmany, cards_in_total):
    # Method which draws 'howmany' cards of the 'cards_in_total'
    poker_cards = all_cards
    for i in range(howmany):
        # get the index of the random drawn card
        index = random.randrange(len(poker_cards) - i)
        last_pos = len(poker_cards) - 1 - i
        poker_cards[last_pos], poker_cards[index] \
            = poker_cards[index], poker_cards[last_pos]  # switch cards

    # prints the randomly drawn cards(sorted
    print_cards(sorted(poker_cards[-howmany:], key=sortby), cards_in_total)
    # returns the randomly drawn cards (sorted)
    return sorted(poker_cards[-howmany:], key=sortby)


def sortby(x):
    # Method used as key to sort the drawn cards by value
    return int(x.split(':')[1])


# ----------------Poker-Combinations---------------------
# shorturl.at/JMOW7

def getCardInfo(card):
    # Method that returns a List which contains the color and value
    # of a single card
    info = card.split(':')
    return info


def getCardValues(drawnCards):
    # Method that returns a List which contains the values of the drawn cards
    values = []
    for x in drawnCards:
        card_val = getCardInfo(x)[1]
        values.append(int(card_val))
    return values


def getCardColors(drawnCards):
    # Method that returns a List which contains the colors of the drawn cards
    colors = []
    for x in drawnCards:
        color = getCardInfo(x)[0]
        colors.append(color)
    return colors


def isRoyalFlush(drawnCards, howmany, cards_in_total):
    # Method that checks if the drawn cards consist of a Royal Flush
    colors = getCardColors(drawnCards)
    values = getCardValues(drawnCards)
    cards_per_color = int(cards_in_total / 4)
    if all(item == "yellow" for item in colors) \
            and min(values) == cards_per_color - howmany + 2 and checkRow(values):
        return True
    elif all(item == "red" for item in colors) \
            and min(values) == cards_per_color - howmany + 2 and checkRow(values):
        return True
    elif all(item == "green" for item in colors) \
            and min(values) == cards_per_color - howmany + 2 and checkRow(values):
        return True
    elif all(item == "black" for item in colors) \
            and min(values) == cards_per_color - howmany + 2 and checkRow(values):
        return True
    else:
        return False


def isStraightFlush(drawnCards):
    # Method that checks if the drawn cards consist of a Straight Flush
    colors = getCardColors(drawnCards)
    values = getCardValues(drawnCards)
    if all(item == "diamond" for item in colors) and checkRow(values):
        return True
    if all(item == "heart" for item in colors) and checkRow(values):
        return True
    if all(item == "spade" for item in colors) and checkRow(values):
        return True
    if all(item == "clover" for item in colors) and checkRow(values):
        return True
    return False


def checkRow(values):
    # Überprüfen ob Werte in Reihe sind
    return sorted(values) == list(range(min(values), max(values) + 1))


def isOfAKind(howManyOfKind, howOften, drawnCards):
    # Method that checks if the drawn cards consist of a Two/Tree-Of-A-Kind
    values = getCardValues(drawnCards)
    sum_ofAKind = 0
    val_count = {card: values.count(card) for card in values}
    for x in val_count.values():
        if x == howManyOfKind:
            sum_ofAKind += 1

    if sum_ofAKind == howOften:
        return True

    return False


def isFullHouse(drawnCards):
    # Method that checks if the drawn cards consist of a Full House
    values = getCardValues(drawnCards)
    colors = getCardColors(drawnCards)

    val_count = {card: values.count(card) for card in values}
    col_count = {card: colors.count(card) for card in colors}
    if 3 in val_count.values() and 2 in val_count.values():
        return True
    return False


def isFlush(drawnCards):
    # Method that checks if the drawn cards consist of a Flush
    colors = getCardColors(drawnCards)
    if all(item == "diamong" for item in colors) or \
            all(item == "heart" for item in colors) or \
            all(item == "spade" for item in colors) or \
            all(item == "clover" for item in colors):
        return True
    else:
        return False


def isStraight(drawnCards):
    # Method that checks if the drawn cards consist of a Straight
    colors = getCardColors(drawnCards)
    values = getCardValues(drawnCards)
    if not all(x == colors for x in colors) and checkRow(values):
        return True

    return False


def isPairVar(nrPairs, drawnCards):
    # Method that checks if the drawn cards consist of one or two Pair/s
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
    # Method that returns the highest card of the drawn cards
    return drawnCards[len(drawnCards) - 1]


def stats(howOften, nr_cards, cards_in_total):
    # Method that performs a certain number of draws and returns the probabilities
    # of the combinations in a statistic
    if cards_in_total % 4 != 0:
        print("The number of cards must be a multiple of 4")
        sys.exit()
    sum_highestCard = sum_OnePair = sum_TwoPair = sum_Triple = sum_FourOfAKind = \
        sum_Flush = sum_StraightFlush = \
        sum_RoyalFlush = sum_FullHouse = sum_Straight = 0
    for x in range(howOften):
        drawn = draw(cards(cards_in_total), nr_cards, cards_in_total)
        if isRoyalFlush(drawn, nr_cards, cards_in_total):
            sum_RoyalFlush += 1
        elif isStraightFlush(drawn):
            sum_StraightFlush += 1
        elif isOfAKind(4, 1, drawn):
            sum_FourOfAKind += 1
        elif isFullHouse(drawn):
            sum_FullHouse += 1
        elif isFlush(drawn):
            sum_Flush += 1
        elif isStraight(drawn):
            sum_Straight += 1
        elif isOfAKind(3, 1, drawn):
            sum_Triple += 1
        elif isPairVar(2, drawn):
            sum_TwoPair += 1
        elif isPairVar(1, drawn):
            sum_OnePair += 1
        else:
            sum_highestCard += 1

        prop_highestCard = sum_highestCard / howOften * 100
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
    print("Number of drawn cards:     \t", nr_cards)
    print("Number of Rounds:          \t", howOften)
    print("Highest-Card:              \t", str(round(prop_highestCard, 4)), " %")
    print("One-Pair:                  \t", str(round(prop_OnePair, 4)), " %")
    print("Two-Pair:                  \t", str(round(prop_TwoPair, 4)), " %")
    print("Triple:                    \t", str(round(prop_Triple, 4)), " %")
    print("Straight:                  \t", str(round(prop_Straight, 4)), " %")
    print("Flush:                     \t", str(round(prop_Flush, 4)), " %")
    print("Full-House:                \t", str(round(prop_FullHouse, 4)), " %")
    print("Four-Of-A-Kind:            \t", str(round(prop_FourOfAKind, 4)), " %")
    print("Straight-Flush:            \t", str(round(prop_StraightFlush, 4)), " %")
    print("Royal-Flush:               \t", str(round(prop_RoyalFlush, 4)), " %")

    x = ["Highest-Card", "One-Pair", "Two-Pair", "Triple", "Straight", "Flush",
         "Full-House", "Four-Of-A-Kind", "Straight-Flush", "Royal-Flush"]
    y = [round(prop_highestCard, 4), round(prop_OnePair, 4), round(prop_TwoPair, 4),
         round(prop_Triple, 4), round(prop_Straight, 4), round(prop_Flush, 4),
         round(prop_FullHouse, 4), round(prop_FourOfAKind, 4),
         round(prop_StraightFlush, 4), round(prop_RoyalFlush, 4)]
    plt.bar(x, y, align="center")
    plt.title("Poker-Combinations")
    plt.xlabel("Combination")
    plt.ylabel("Probability in %")
    plt.xticks(rotation=90)
    plt.show()


if __name__ == '__main__':
    stats(100000, 5, 52)
