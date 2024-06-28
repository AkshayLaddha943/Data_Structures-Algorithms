class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
    # def setData(self, data):
    #     self.data = data
        
    # # function to get data of a particular node
    # def getData(self):
    #     return self.data
    
    # # function to set next node
    # def setNext(self, next):
    #     self.next = next
        
    # # function to get the next node
    # def getNext(self):
    #     return self.next
    

class LinkedList(object):
    def __init__(self):
        self.head = None
    
    def printlist(self):
        temp = self.head
        while (temp):
            print(temp.data, end=' ')
            temp = temp.next
    
    def insertstart(self, data):
        newnode = Node(data)
        newnode.next = self.head
        self.head = newnode
    
    def insertmiddle(self, prevnode, data):
        if (prevnode.next is None):
            print("prev node should have next node")
        else:
            newnode = Node(data)
            newnode.next = prevnode.next
            prevnode.next = newnode
    
    def insertend(self, data):
        newnode = Node(data)
        temp = self.head
        while (temp.next is not None):
            temp = temp.next
        temp.next = newnode
        
    def search(self, node, data):
        if node == None:
            return False
        if node.data == data:
            return True
        return self.search(node.getNext(), data)
    
    def delete(self, node):
        if self.head is None:
            return
        
        temp = self.head
        
        if node == 0:
            self.head = temp.next
            temp = None
            return
        
        for i in range(node-1):
            temp = temp.next
            
    
    def reverselist(self):
        prev = None
        current = self.head
        while (current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
            
        
            

if __name__ == '__main__':
    List = LinkedList()
    List.head = Node(1)                   # create the head node
    node2 = Node(2)
    List.head.next(node2)           # head node's next --> node2
    node3 = Node(3)
    node2.next(node3)                # node2's next --> node3
    List.insertstart(4)                   # node4's next --> head-node --> node2 --> node3
    List.insertmiddle(node2, 5)     # node2's next --> node5
    List.printlist()
    print()
    List.reverselist()
    List.printlist()
        