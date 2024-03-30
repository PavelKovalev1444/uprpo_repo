class Node:
    def __init__(self, data, prev = None, next = None):
        self.__data = data
        self.__prev__ = prev
        self.__next__ = next
    
    
    def get_data(self):
        return self.__data
    
    
    def __str__(self):
        if(self.__prev__):
            prev = self.__prev__.__data
        else:
            prev = None
        if (self.__next__):
            next_1 = self.__next__.__data
        else:
            next_1 = None
        return "data: {}, prev: {}, next: {}".format(self.__data, prev.__str__(), next_1.__str__())

    
class LinkedList(list):
    def __init__(self, first = None, last = None):
        self.__first__ = None
        self.__last__ = None
        self.__length = 0
        if (first == None) and (last != None):
            raise ValueError("invalid value for last")
        elif (first != None) and (last == None):
            node = Node(first)
            self.__first__ = node
            self.__last__ = node
            self.__length = 1
        elif (first != None) and (last != None):
            node1 = Node(first)
            node2 = Node(last)
            node1.__next__ = node2
            node2.__prev__ = node1
            self.__first__ = node1
            self.__last__ = node2
            self.__length = 2
    
    
    def __len__(self):  
        return self.__length


    def __str__(self):
        if self.__length == 0:
            return "LinkedList[]"
        element = self.__first__
        array = []
        while element != None:
            array.append(str(element))
            element = element.__next__
        return "LinkedList[length = {}, [".format(self.__length) + "; ".join(array) + "]]"     
    
    
    def append(self, element):
        node = Node(element)
        self.__length += 1
        if self.__first__ == None:
            self.__first__ = node
            self.__last__ = node
        else:
            node.__prev__ = self.__last__
            self.__last__.__next__ = node
            self.__last__ = node        


    def pop(self):
        if self.__length == 0:
            raise IndexError("LinkedList is empty!")
        else:
            self.__last__.__prev__.__next__ = None
            self.__length -= 1



    def popitem(self, other):    
        if len(self) == 0:
            raise KeyError("{} doesn't exist!".format(other))
        else:
            element = self.__first__
            while element:
                if element.get_data() == other:
                    self.__length -= 1
                    if element.__prev__ != None:
                        element.__prev__.__next__ = element.__next__
                    else:
                        self.__first__ = element.__next__
                    if element.__next__ != None:
                        element.__next__.__prev__ = element.__prev__
                    else:
                        self.__last__ = element.__prev__
                    break
                element = element.__next__
                if (element.__next__ == None) and (element.get_data() != other):
                    raise KeyError("{} doesn't exist!".format(other))    

        
    def clear(self):
        self.__first__ = None
        self.__last__ = None
        self.__length = 0