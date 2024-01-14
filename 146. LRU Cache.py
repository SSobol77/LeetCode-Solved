# 146. LRU Cache.

# Topic: Hash Table, Linked List, Design, Doubly-Linked List.

"""
### Task: 
---
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

  -  LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
  -  int get(int key) Return the value of the key if the key exists, otherwise return -1.
  -  void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to 
     the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.

he functions get and put must each run in O(1) average time complexity.

#Example 1:
Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
 
#Constraints:
1 <= capacity <= 3000
0 <= key <= 10^4
0 <= value <= 10^5
At most 2 * 10^5 calls will be made to get and put.


### Testcase:
---
["LRUCache","put","put","get","put","get","put","get","get","get"]
[[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]


### Code:
---
class LRUCache:

    def __init__(self, capacity: int):
        

    def get(self, key: int) -> int:
        

    def put(self, key: int, value: int) -> None:
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

"""
### Solution: --------------------------------------------------------------------------------------

class ListNode:
    def __init__(self, key, value):
        # Initialize a ListNode with a key and value, and set prev and next pointers to None
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        # Initialize the LRUCache with a given capacity
        self.capacity = capacity
        self.cache = {}  # A hash table to store key-node pairs
        self.head = ListNode(0, 0)  # Dummy head node for the doubly-linked list
        self.tail = ListNode(0, 0)  # Dummy tail node for the doubly-linked list
        self.head.next = self.tail  # Connect head to tail
        self.tail.prev = self.head  # Connect tail to head

    def _remove(self, node):
        # Helper function to remove a node from the doubly-linked list
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add_to_head(self, node):
        # Helper function to add a node to the front of the doubly-linked list
        node.next = self.head.next
        node.prev = self.head
        self.head.next = node
        node.next.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            # Key exists in the cache, move it to the front of the list (most recently used)
            node = self.cache[key]
            self._remove(node)  # Remove the node from its current position
            self._add_to_head(node)  # Add it to the front
            return node.value
        return -1  # Key not found in the cache

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Key already exists, update its value and move it to the front
            node = self.cache[key]
            node.value = value
            self._remove(node)  # Remove the node from its current position
            self._add_to_head(node)  # Add it to the front
        else:
            if len(self.cache) >= self.capacity:
                # Cache is full, remove the least recently used item (tail)
                tail_key = self.tail.prev.key
                self._remove(self.tail.prev)  # Remove the tail node
                del self.cache[tail_key]  # Remove the corresponding entry from the cache

            # Create a new node for the key-value pair and add it to the front
            new_node = ListNode(key, value)
            self.cache[key] = new_node
            self._add_to_head(new_node)  # Add it to the front


### Description: -----------------------------------------------------------------------------------
'''
### In this implementation:

- ListNode represents a node in the doubly-linked list with key and value fields.
- LRUCache initializes the cache with a given capacity, and it uses a hash table (self.cache) to store key-value pairs.
- The get method returns the value for a given key if it exists in the cache. It also updates the order of the keys based on 
  their usage by moving the accessed key to the front of the doubly-linked list.
- The put method inserts or updates a key-value pair in the cache. If the cache is full, it removes the least recently used i
  tem (tail) before adding the new key-value pair to the front of the doubly-linked list.
- This implementation ensures O(1) average time complexity for both get and put operations.


**Problem Description:**

An LRU (Least Recently Used) cache is a data structure that maintains a fixed-size collection of key-value pairs. It has the following properties and functionalities:

1. It has a specified capacity, which limits the number of key-value pairs it can store.

2. It allows you to retrieve the value associated with a given key (`get` operation). When you access a key, it becomes the most recently used key.

3. It allows you to add or update a key-value pair (`put` operation). If the cache is full, it removes the least recently used key-value pair to make space for the new one.

4. The goal is to design an efficient data structure that performs `get` and `put` operations in O(1) average time complexity.

**Solution Approach:**

To implement an LRU cache efficiently, we can use a combination of a hash table and a doubly-linked list. Here's how the `LRUCache` class is structured:

1. **Initialization:** The class is initialized with a specified capacity. It uses a hash table (`self.cache`) to store key-node pairs, where each node contains a key, a value, and pointers to the previous and next nodes in the doubly-linked list. There are also dummy head and tail nodes to simplify insertion and removal operations.

2. **Helper Functions:**
   - `_remove(node)`: This function removes a node from the doubly-linked list.
   - `_add_to_head(node)`: This function adds a node to the front of the doubly-linked list.

3. **`get` Method:**
   - When you call `get(key)` to retrieve a value, it checks if the key exists in the cache. If the key exists, it moves the corresponding node to the front of the doubly-linked list to mark it as the most recently used.
   - If the key is not found, it returns -1 to indicate that the key is not in the cache.

4. **`put` Method:**
   - When you call `put(key, value)` to insert or update a key-value pair, it first checks if the key already exists in the cache.
   - If the key exists, it updates the value and moves the corresponding node to the front of the doubly-linked list.
   - If the key is new, it checks if the cache is at its capacity. If so, it removes the least recently used item (tail node) by calling `_remove` and deleting it from the cache.
   - Finally, it creates a new node for the key-value pair, adds it to the front of the doubly-linked list using `_add_to_head`, and stores it in the cache.

**Time Complexity:**

The `get` and `put` operations both have an average time complexity of O(1) because the hash table allows direct access to nodes, and the doubly-linked list enables efficient reordering of elements for LRU management.

In summary, the `LRUCache` class efficiently implements an LRU cache with a specified capacity, ensuring that the most recently used items are retained while evicting the least recently used items when the cache is full.
'''