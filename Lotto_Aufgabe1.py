import random


def ziehe(min, max, anz_zufall):
    arr = []
    for i in range(min,max):                   #befüllen der Liste mit Werten von 1 bis 45
        arr.append(i)

    #print(arr)
    for i in range(anz_zufall):                    # ziehen der Zufallszahlen
        index = random.randrange(len(arr) - i)
        zufall = arr[index]
        last_pos = len(arr) - 1 - i
        arr[last_pos], arr[index] = arr[index], arr[last_pos]
    print(arr)
    print(arr[-anz_zufall:])                           # letzen 6 Werte ausgeben --> das sind die gezogenen Zahlen
    return arr[-anz_zufall:]




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
        stats(ziehe(45, 6))


if __name__ == '__main__':
  #  call(1000)
  count = [0] * 45  # Array an dem pro position die Anzahl der Ziehungen pro Zahl gemappt wird
  ziehe(50, 90, 6)
