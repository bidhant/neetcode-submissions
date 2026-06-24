class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        # Dummy head and tail nodes to avoid edge cases
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def remove_node(self, node):
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

    def add_node_to_head(self, node):
        node.next = self.head.next
        node.prev = self.head

        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove_node(node)      # Fixed method name
            self.add_node_to_head(node)
            return node.val
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.remove_node(node)      # Fixed name and added argument
            self.add_node_to_head(node) # Added argument
        else: 
            new_node = Node(key, value)
            self.cache[key] = new_node
            self.add_node_to_head(new_node)

            if len(self.cache) > self.capacity: 
                lru_node = self.tail.prev
                self.remove_node(lru_node) # Fixed method name
                del self.cache[lru_node.key]