class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None
        
class LinkedList:
    def __init__(self, capacity):
        self.capacity = capacity
        self.head = None  # points to most recently used element
        self.rear = None    # points to least recently used element
        self.address = dict()
        self.length = 0
        
    def addNewNode(self, key, value):
        if self.head == None:
            self.head = Node(key, value)
            self.rear = self.head
        else:
            newNode = Node(key, value)
            self.head.next = newNode
            temp = self.head
            self.head = self.head.next
            self.head.prev = temp
        self.address[key] = self.head
    
    def moveToHeadNode(self, key):
        # next is none -> is at head
        same = self.address[key]
        if self.head == same:
            return
        
        # node is at rear -> same.prev = Null
        if self.rear == same:
            self.rear = self.rear.next
            
        if same.prev:
            same.prev.next = same.next
        same.next.prev = same.prev
        same.next = None
        same.prev = self.head
        self.head.next = same
        self.head = same
        
        
    def removeRearNode(self):
        key = self.rear.key
        # corner case : capacity = 1, rear.next = None
        if self.rear.next is None:
            self.head = None 
        else:
            temp = self.rear
            self.rear = self.rear.next
            self.rear.prev = None
            temp.next = None
        del self.address[key]
        
    def addNode(self, key, value):
        # self.length+=1 # this is a bug
        if self.length < self.capacity and key not in self.address:
            self.addNewNode(key, value)
            self.length += 1
            
        elif key in self.address:
            # remove from that position and add to head
            self.moveToHeadNode(key)
            if self.head.value != value:
                self.head.value = value
        else:
            # remove then add
            self.removeRearNode()
            self.addNewNode(key, value)
        #print(self.address.keys(), self.head.key, self.rear.key)
    def __repr__(self) -> None:
        s=""
        curr = self.head
        while curr != None:
            s = s + f"({curr.key}->{curr.value})"
            curr = curr.prev
        return s

class LRUCache:

    def __init__(self, capacity: int):
        self.ll = LinkedList(capacity)

    def get(self, key: int) -> int:
        if key in self.ll.address:
            self.ll.moveToHeadNode(key)
            #print(key, self.ll.address.keys(), self.ll.head.key, self.ll.rear.key)
            return self.ll.address[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        self.ll.addNode(key, value)
    def __repr__(self) -> str:
        return repr(self.ll)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
