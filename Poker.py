import random


def cards(number_cards, cards_per_color):
    poker_cards = [None] * number_cards
    colors = ["red", "black", "yellow", "green"]
    run_colors = 0
    run_values = 1
    print(colors[0])
    for i in range(0, number_cards):
        #print(run_colors)
        combine = colors[run_colors - 1] + str(run_values)
        poker_cards[i] = combine
        if i % cards_per_color == 0:
            run_colors += 1
        run_values +=1
        if run_values == cards_per_color:
            run_values = 0

    return poker_cards


def ziehe(cards, howmany):
    poker_cards = cards(52, 13)
    for i in range(howmany):  # ziehen der Zufallszahlen
        index = random.randrange(len(poker_cards) - i)
        last_pos = len(poker_cards) - 1 - i
        poker_cards[last_pos], poker_cards[index] = poker_cards[index], poker_cards[last_pos]

    print(poker_cards[len(poker_cards) -1 - howmany:len(poker_cards) -1])
    return poker_cards[len(poker_cards) -1 - howmany:len(poker_cards) -1]


if __name__ == '__main__':
    ziehe(cards, 5)
