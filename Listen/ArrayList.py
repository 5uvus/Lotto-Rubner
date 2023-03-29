from copy import deepcopy
import Aufwandsklassen as ak

class ArrayList:
    def __init__(self):
        self.items = []

    def append(self, item):
        self.items.append(item)

    def extend(self, lst):
        self.items.extend(lst)

    def insert(self, index, item):
        self.items.insert(index, item)

    def remove(self, item):
        self.items.remove(item)

    def pop(self, index=-1):
        return self.items.pop(index)

    def clear(self):
        self.items.clear()

    def index(self, item, start=0, end=None):
        return self.items.index(item, start, end)

    def count(self, item):
        return self.items.count(item)

    def sort(self, key=None, reverse=False):
        self.items.sort(key=key, reverse=reverse)

    def reverse(self):
        self.items.reverse()

    def len(self):
        return len(self.items)

    def getItem(self, index):
        return self.items[index]

    def setItem(self, index, value):
        self.items[index] = value

    def delItem(self, index):
        del self.items[index]
    
    def writeList(self):
        for item in self.items:
            print(item)
    
    def copy(self):
        newList = ArrayList()
        newList.items = deepcopy(self.items)
        return newList

if __name__ == "__main__":
    run = True
    list = ArrayList()
    list.append(1)
    list.append(2)
    list.append(3)
    list.append(4)
    list.writeList()
    
    
    while run:
        print("-------------------")
        list.writeList()
        print("-------------------")
        print("1 --> Add Element")
        print("2 --> Insert after element")
        print("3 --> Delete element")
        print("4 --> Find element")
        print("5 --> Show first element")
        print("6 --> Show last element")
        print("7 --> Print list")
        print("8 --> Show index of element")
        print("9 --> Clear list")
        print("10 --> Copy list")
        print("11 --> Extend List")
        print("12 --> Pop element")
        print("13 --> Sort list")
        print("14 --> Show Statistics")
        inp = input("Choose what u want to do...")
        if inp == "1":
            add = input("Which number do you want to add?")
            list.append(int(add))
        elif inp == "2":
            insert = input("After which element do you want to add a new element? e.g. 1:2")
            insert = insert.split(":")
            list.insert(int(insert[0]), int(insert[1]))
        elif inp == "3":
            delete = input("Which element do you want to delete?")
            list.remove(int(delete))
        elif inp =="4":
            find = input("Find element at specific index:")
            print(list.index(int(find)))
        elif inp == "5":
            print(list[0])
        elif inp == "6":
            print(list[list.len()-1])
        elif inp == "7":
            list.writeList()
        elif inp == "8":
            index = input("Which element do you want to get the index from?")
            print(list.getItem(int(index)))
        elif inp == "9":
            list.clear()
        elif inp == "11":
            second = input("Enter list to extend...")
            second = second.split(",")
            
            list.extend(list(map(int, second)))
        elif inp == "10":
            copied = list.copy()
            print(copied.writeList())
        elif inp == "12":
            pop = input("Which elemente at what index do you want to pop")
            list.pop(int(pop))
        elif inp == "13":
            print(list.sort())
        elif inp =="14":
             ak.stats()
