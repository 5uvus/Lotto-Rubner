from copy import copy
import Aufwandsklassen as ak

class DoppelteVerketteteListe:

    def __init__(self):
        self.startElement = ListElement(None)
        self.tailElement = ListElement(None)
        self.startElement.setNextElem(self.tailElement)
        self.tailElement.setPrevElem(self.startElement)

    def addLast(self, obj):
        if self.startElement.getObj() == None:
            #print("true")
            self.startElement = ListElement(obj)
            self.tailElement = self.startElement
        else:
            #print("false")
            newElement = ListElement(obj)
            lastElement = self.tailElement
            lastElement.setNextElem(newElement)
            newElement.setPrevElem(lastElement)
            self.tailElement = newElement
        
           

    def insertAfter(self, prevItem, newItem):
        newElem = ListElement(None)
        nextElem = ListElement(None)
        pointerElem = self.startElement
        while pointerElem is not None and pointerElem.getObj() != prevItem:
            pointerElem = pointerElem.getNextElem()

        newElem = ListElement(newItem)
        if pointerElem is not None:
            nextElem = pointerElem.getNextElem()
            pointerElem.setNextElem(newElem)
            newElem.setNextElem(nextElem)
            newElem.setPrevElem(pointerElem)

        if nextElem is not None:
            nextElem.setPrevElem(newElem)

    def insertBefore(self, insertItem, newItem):
        newElem = ListElement(newItem)
        pointerElem = self.startElement.getNextElem()
        while pointerElem is not None:
            if pointerElem.getObj() ==insertItem:
                newElem.setPrevElem(pointerElem.getPrevElem())
                pointerElem.getPrevElem().setNextElem(newElem)
                pointerElem.setPrevElem(newElem)
                newElem.setNextElem(pointerElem)
                break

            pointerElem = pointerElem.getNextElem()

    def delete(self, o):
        le = self.startElement
        while le.getNextElem() is not None and le.getObj() is not o:
            if le.getNextElem().getObj() == o:
                if le.getNextElem().getNextElem() is not None:
                    le.setNextElem(le.getNextElem().getNextElem())
                    le.getNextElem().setPrevElem(le)
                else:                       #falls delete an letzter Stelle
                    le.setNextElem(None)    
                    break

            le = le.getNextElem()

    def find(self, o):
        le = self.startElement
        while le is not None:
            if le.getObj() == o:
                return True
            le = le.nextElement
        return False

    def getFirstElem(self):
        return self.startElement

    def getLastElement(self):
        le = self.startElement
        while le.getNextElem() != None:
            le = le.getNextElem();
        
        return le;

    def writeList(self):
        le = self.startElement
        while le is not None:
            print(le.getObj())
            le = le.getNextElem()

    def getLength(self):
        le = self.startElement
        cnt = 0
        while le is not None:
            cnt += 1
            le = le.nextElement
        return cnt

    def index(self, o):
        le = self.startElement
        cnt = 0
        while le is not None:
            cnt += 1
            if le.nextElement.getObj() == o:
                return cnt
            le = le.nextElement
        return None

    def clearList(self):
        le = self.startElement
        while le is not None:
            self.delete(le.getObj())

    def copyList(self):
        copied = DoppelteVerketteteListe()
        le = self.startElement
        while le is not None:
            if le.getNextElem() is not None:
                le = le.getNextElem()
                copied.addLast(le.getObj())
            else:
                return copied

    def extend(self, secondList):
        le = secondList.startElement.nextElement
        # print(le.getObj())
        # print(self.writeList())
        while le is not None:
            self.addLast(le.getObj())
            le = le.nextElement

    def pop(self, index):
        le = self.startElement
        cnt = 0
        for cnt in range(index - 1):
            le = le.getNextElem()
        self.delete(le.getObj())
        print(le.getObj())
        return le.getObj()

    def sortList(self):
        for i in range(self.getLength()):
            current = self.startElement
            for j in range(self.getLength() - i - 1):
                if current.getObj() > current.getNextElem().getObj():
                    current.obj, current.nextElement.obj = current.getNextElem().getObj(), current.getObj()
                current = current.nextElement

        
class ListElement:

    def __init__(self, obj):
        self.obj = obj
        self.nextElement = None
        self.prevElement = None

    def setNextElem(self, nextElem):
        self.nextElement = nextElem

    def setPrevElem(self, prevElem):
        self.prevElement = prevElem

    def getNextElem(self):
        return self.nextElement

    def getPrevElem(self):
        return self.prevElement
    def getObj(self):
        return self.obj


if __name__ == "__main__":
    run = True
    list = DoppelteVerketteteListe()
    list.addLast("1")
    list.addLast("9")
    list.addLast("3")
    list.addLast("4")
    list.addLast("5")
    
    
    
    while run:
        print("-------------------")
        list.writeList()
        print("-------------------")
        print("0 --> Add Element")
        print("1 --> Insert before Element")
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
        if inp == "0":
            add = input("Which number do you want to add?")
            list.addLast(add)
        if inp == "1":
            insert = input("Before which element do you want to add a new element? e.g. 1:2")
            insert = insert.split(":")
            list.insertBefore(insert[0], insert[1])
        elif inp == "2":
            insert = input("After which element do you want to add a new element? e.g. 1:2")
            insert = insert.split(":")
            list.insertAfter(insert[0], insert[1])
        elif inp == "3":
            delete = input("Which element do you want to delete?")
            list.delete(delete)
        elif inp =="4":
            find = input("Find element")
            print(list.find(find))
        elif inp == "5":
            print(list.getFirstElem().getObj())
        elif inp == "6":
            print(list.getLastElement().getObj())
        elif inp == "7":
            list.writeList()
        elif inp == "8":
            index = input("Which element do you want to get the index from")
            print(list.index(index))
        elif inp == "9":
            list.clearList()
        elif inp == "11":
            second = input("Enter list to extend...")
            second = second.split(",")
            newList = DoppelteVerketteteListe()
            for s in second:
                newList.addLast(s)
            list.extend(newList)
            list.writeList()
        elif inp == "10":
            copied = list.copyList()
            print(copied.writeList())
        elif inp == "12":
            pop = input("Which elemente at what index do you want to pop")
            list.pop(int(pop))
        elif inp == "13":
            list.sortList()
        elif inp == "14":
            ak.stats()

   # print("Clearing list")
    #list.clearList()
    #list.writeList()

    #print("Pop...")
    #list.pop(2)
   
   # print("First Element: " + list.getFirstElem().getObj())
   # print("Is 3 included? ", + list.find("3"))
   # print("IS 5 included?, ", list.find("5"))
   # print("Last Element: " + list.getLastElement().getObj())

   # print("Sorting...")
    #newList = list.sortList()
    #newList.writeList()

    # print("Copy list...")
    # copied = list.copyList()
    # print(copied.writeList())
    # print(copied.getLength())

    #list1 = VerketteteListe()
    #list1.addLast("6")
    #list1.addLast("7")

    #print("Extend second list...")
    #list.extend(list1)
    #list.writeList()

    # print("Pop...")
    # list.pop(2)
    # list.writeList()

   # print("Sorting...")
    #newList = list.sortList()
    #newList.writeList()
