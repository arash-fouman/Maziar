


lists = [[1, 4, 10, 15, 30, 70, 90, 120, 150, 330, 500] , [1, 3, 4], [2, 6], [2, 5, 8], [-17, 10, 12]]


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = Node('head')
        self.tail = self.head
    
    def insertNode(self, node):
        self.tail.next = node
        self.tail = node
    
    def printList(self):
        self.skipHead()
        x = self.head
        while (x != None):
            print(x.data, end=' ')
            x = x.next
        print('\n')

    def skipHead(self):
        if(self.head.next != None):
            self.head = self.head.next

def convertArrToLinkedList( arr ):
    
    llist = []
    for i in arr:
        temp = LinkedList()
        for j in i:
            temp.insertNode(Node(j))
        llist.append(temp)

    return llist


def merge(lists):

    n = len(lists)

    if( n == 1 ):
        return lists[0]
    
    left = merge(lists[:int(n/2)])
    right= merge(lists[int(n/2):])

    l_ptr = left.head.next    #keeps track of the last index inserted into the final list
    r_ptr = right.head.next   #keeps track of the last index inserted into the final list
    res = LinkedList()

    while (l_ptr != None and r_ptr != None): #checks to not go out of bound
        
        if(l_ptr.data < r_ptr.data):
            res.insertNode(l_ptr)
            l_ptr = l_ptr.next
        else:
            res.insertNode(r_ptr)
            r_ptr = r_ptr.next

    
    if (l_ptr != None):        #inserts the residual elements of the list to the final list
        res.insertNode(l_ptr)

    if (r_ptr != None):       #inserts the residual elements of the list to the final list
        res.insertNode(r_ptr)

    return res


lists = convertArrToLinkedList(lists)

mergedLists = merge(lists)

mergedLists.printList()

#correctly sorted output:
#[-17, 1, 1, 2, 2, 3, 4, 4, 5, 6, 8, 10, 10, 12, 15, 30, 70, 90, 120, 150, 330, 500]

