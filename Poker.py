import random


def cards():
    poker_cards = [None] * 52
    colors = ["red", "black", "yellow", "green"]
    run_colors = 0
    run_values = 1
    print(colors[0])
    for i in range(0, 52):
        #print(run_colors)
        combine = colors[run_colors - 1] + str(run_values)
        poker_cards[i] = combine
        if i % 13 == 0:
            run_colors += 1
        run_values +=1
        if run_values == 13:
            run_values = 0

    return poker_cards


def ziehe(cards, howmany):
    poker_cards = cards()
    for i in range(howmany):  # ziehen der Zufallszahlen
        index = random.randrange(len(poker_cards) - i)
        last_pos = len(poker_cards) - 1 - i
        poker_cards[last_pos], poker_cards[index] = poker_cards[index], poker_cards[last_pos]

    print(poker_cards[46:51])
    return poker_cards[46:51]


if __name__ == '__main__':
    ziehe(cards, 5)
