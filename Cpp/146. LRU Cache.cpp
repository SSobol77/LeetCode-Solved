// 146. LRU Cache.


// Topic: Hash Table, Linked List, Design, Doubly-Linked List.

/*
### Task:
---
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

    - LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
    - int get(int key) Return the value of the key if the key exists, otherwise return -1.
    - void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.

The functions get and put must each run in O(1) average time complexity.

Example 1:
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
 
Constraints:
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
class LRUCache {
public:
    LRUCache(int capacity) {
        
    }
    
    int get(int key) {
        
    }
    
    void put(int key, int value) {
        
    }
};
*/
/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */

// Solution: ---------------------------------------------------------------------------------------------------


#include <unordered_map>
using namespace std;

// Node for the doubly linked list
struct DLinkedNode {
    int key, value;
    DLinkedNode* prev;
    DLinkedNode* next;
    DLinkedNode(): key(0), value(0), prev(nullptr), next(nullptr) {}
    DLinkedNode(int _key, int _value): key(_key), value(_value), prev(nullptr), next(nullptr) {}
};

class LRUCache {
private:
    unordered_map<int, DLinkedNode*> cache; // Hashmap to store key-value pairs for O(1) access
    DLinkedNode* head; // Dummy head of the doubly linked list
    DLinkedNode* tail; // Dummy tail of the doubly linked list
    int size; // Current size of the cache
    int capacity; // Maximum capacity of the cache

    // Adds a node right after the head
    void addNode(DLinkedNode* node) {
        node->prev = head;
        node->next = head->next;
        head->next->prev = node;
        head->next = node;
    }

    // Removes an existing node from the linked list
    void removeNode(DLinkedNode* node) {
        DLinkedNode* prev = node->prev;
        DLinkedNode* next = node->next;
        prev->next = next;
        next->prev = prev;
    }

    // Moves a node to the head of the list to mark it as recently used
    void moveToHead(DLinkedNode* node) {
        removeNode(node);
        addNode(node);
    }

    // Pops the current tail, removing the least recently used element
    DLinkedNode* popTail() {
        DLinkedNode* res = tail->prev;
        removeNode(res);
        return res;
    }

public:
    LRUCache(int capacity) : capacity(capacity), size(0) {
        // Initialize dummy head and tail
        head = new DLinkedNode();
        tail = new DLinkedNode();
        head->next = tail;
        tail->prev = head;
    }
    
    // Returns the value of the key if it exists, or -1 if it doesn't
    int get(int key) {
        if (cache.find(key) == cache.end()) return -1; // Key not found
        
        // Key found, move the node to the head to mark as recently used
        DLinkedNode* node = cache[key];
        moveToHead(node);
        return node->value;
    }
    
    // Updates the value of the key if it exists, or adds the key-value pair if it doesn't
    void put(int key, int value) {
        if (cache.find(key) != cache.end()) {
            // Key exists, update the value and move to head
            DLinkedNode* node = cache[key];
            node->value = value;
            moveToHead(node);
        } else {
            // Key doesn't exist, create a new node and add to the head
            DLinkedNode* newNode = new DLinkedNode(key, value);
            cache[key] = newNode;
            addNode(newNode);
            ++size;
            
            // If capacity is exceeded, remove the least recently used item
            if (size > capacity) {
                DLinkedNode* tail = popTail();
                cache.erase(tail->key); // Remove from hashmap
                delete tail; // Free the memory
                --size;
            }
        }
    }
};



// Description: =======================================================================================================================================
/*

To design an LRU (Least Recently Used) cache as specified, we need a combination of a hash table and a doubly-linked list. The hash table provides O(1) 
access time to cache items by key, while the doubly-linked list maintains the order of items based on their usage, allowing for O(1) update time when 
accessing or inserting items. When the cache exceeds its capacity, the least recently used item (at the tail of the list) can be removed quickly.

### Explanation:

- **DLinkedNode**: A structure for doubly linked list nodes containing `key`, `value`, and pointers to the previous and next nodes.
- **LRUCache**: The main class implementing the LRU cache with methods `get` and `put`.
  - **addNode**: Helper function to add a new node right after the head.
  - **removeNode**: Helper function to remove an existing node from the linked list.
  - **moveToHead**: Helper function to move a node to the head of the linked list to mark it as recently used.
  - **popTail**: Helper function to pop the tail node from the linked list, which is the least recently used element.
- The cache uses a hash table to map keys to their corresponding nodes in the doubly linked list, enabling O(1) access time. The doubly linked list maintains 
  the LRU order with the most recently used items near the head and the least recently used items near the tail. When the cache reaches its capacity, the least 
  recently used item is removed from the tail of the list.

*/
