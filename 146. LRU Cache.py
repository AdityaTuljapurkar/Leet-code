class Node:
    def __init__(self,key,value):
        # prev , next 
        self.key = key 
        self.value = value 
        self.prev = self.next = None
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity 
        self.cache = {}
        self.leftNode = self.rightNode = Node(0,0)
        self.leftNode.next = self.rightNode 
        self.rightNode.next = self.leftNode 

        
    def insert(self,node):
        prv , right = self.rightNode.prev , self.rightNode 
        prv.next , node.prev = node , prv 
        right.prev , node.next = node , right 

    def remove(self,node):
        prv , nxt = node.prev , node.next 
        prv.next , nxt.prev = nxt , prv 

    def get(self, key: int) -> int:
        if key in self.cache :
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key]  = Node(key,value)
        self.insert(self.cache[key])
        if len(self.cache)> self.cap :
            lru = self.leftNode.next 
            self.remove(lru)
            del self.cache[lru.key]
        
class Node:
    def __init__(self, key, value):
        self.key = key 
        self.value = value   # ✅ renamed consistently (you used `value`, not `val`)
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity 
        self.cache = {}

        # ❌ You had:
        # self.leftNode = self.rightNode = Node(0,0)
        # This makes both variables point to the SAME node.
        # ✅ Fix: create TWO separate dummy nodes
        self.leftNode, self.rightNode = Node(0,0), Node(0,0)

        # ❌ You had: self.rightNode.next = self.leftNode
        # That creates a forward link from tail -> head (wrong).
        # ✅ Correct: doubly linked list with head <-> tail
        self.leftNode.next = self.rightNode
        self.rightNode.prev = self.leftNode

    def insert(self, node):
        # Insert node at the right (just before dummy tail)
        prev = self.rightNode.prev
        nxt = self.rightNode

        # ✅ safer step-by-step assignment instead of tuple unpacking
        prev.next = node
        node.prev = prev
        node.next = nxt
        nxt.prev = node

    def remove(self, node):
        prev, nxt = node.prev, node.next
        # ❌ You had tuple assignment: prv.next, nxt.prev = nxt, prv
        # Works but less clear; ✅ rewritten step-by-step for clarity
        prev.next = nxt
        nxt.prev = prev

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)

            # ❌ You had: return self.cache[key].val (wrong attribute)
            # ✅ Fix: return node.value
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])  # remove old node if exists

        # insert new node
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            # Remove LRU node (node just after dummy head)
            lru = self.leftNode.next
            self.remove(lru)
            del self.cache[lru.key]
