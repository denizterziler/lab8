from abc import ABC


class Abstract(ABC):
    address = ''

    def __init__(self, given_address):
        self.address = given_address

    def calculateFreqs(self):
        pass


class ListCount(Abstract):

    def __init__(self, address):
        Abstract.__init__(self, address)

    def calculateFreqs(self):
        strange = open(self.address, 'r').read()
        strange = strange.split()
        strange2 = []

        for i in strange:
            if i not in strange2:
                strange2.append(i)

        for i in range(0, len(strange2)):
            print(strange2[i], '=', strange.count(strange2[i]))


class DictCount(Abstract):
    def __init__(self, address):
        Abstract.__init__(self, address)

    def calculateFreqs(self):
        strange = open(self.address, 'r').read()

        dictionary = {}

        lst = strange.split()
        for elements in lst:
            dictionary[elements]  = 0
       
        for elements in lst:
            if elements[-1] == '.':
                elements = elements[0:len(elements) - 1]

            if elements in dictionary:
                dictionary[elements] += 1

            else:
                dictionary.update({elements: 1})

        for allKeys in dictionary:
            print("\"", allKeys, "\"", end=" ")
            print(dictionary[allKeys], end=" ")
            print()


print("ListCount: ")
L = ListCount('/Users/denizterziler/Desktop/strange.txt')
L.calculateFreqs()
print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
print("DictCount: ")
D = DictCount('/Users/denizterziler/Desktop/strange.txt')
D.calculateFreqs()
