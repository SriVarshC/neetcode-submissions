class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}

        self.left = Node(0,0)
        self.right = Node(0,0)

        self.left.next = self.right
        self.right.prev = self.left

    def remove(self,node):
        prev = node.prev
        nxt = node.next

        prev.next = nxt
        nxt.prev = prev

    def insert(self,node):
        prev = self.right.prev

        node.prev = prev
        node.next = self.right

        prev.next = node
        self.right.prev = node
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            node = self.cache[key]

        self.remove(node)
        self.insert(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.remove(node)
            self.insert(node)

        else:
            node = Node(key,value)
            self.cache[key] = node
            self.insert(node)

        if len(self.cache)>self.cap:
            lru = self.left.next
            self.remove(lru)

            del self.cache[lru.key]
            
        
        
