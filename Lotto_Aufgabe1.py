import random


def ziehe():
    arr = []
    for i in range(1, 46, 1):
        arr.append(i)
    for i in range(0, 6, 1):
        index = random.randrange(len(arr) - i)
        zufall = arr[index]
        arr[len(arr) - 1 - i] = zufall
        arr[index] = len(arr) - i
    print(arr[39:45])
    return arr


count = [0] * 45


def stats(ziehung):
    final = [""] * 45
    for b in range(39, 45, 1):
        value = ziehung[b]
        count[value - 1] = count[value - 1] + 1
    for i in range(0, 45, 1):
        final[i] = str(i + 1) + ":" + str(count[i])
    print(final)


def call(wieoft):
    for wieoft in range(0, wieoft, 1):
        stats(ziehe())


if __name__ == '__main__':
    call(1000)
