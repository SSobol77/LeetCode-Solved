# 138. Copy List with Random Pointer.

# Topic: Hash Table, Linked List.

"""
### Task:
---
A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value 
of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the 
pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the 
original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied 
list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. 
Each node is represented as a pair of [val, random_index] where:

    val: an integer representing Node.val
    random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.

Your code will only be given the head of the original linked list.

#Example 1:
Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

#Example 2:
Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]

#Example 3:
Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]

#Constraints:
0 <= n <= 1000
-10^4 <= Node.val <= 10^4
Node.random is null or is pointing to some node in the linked list.

Hint 1:
Just iterate the linked list and create copies of the nodes on the go. Since a node can be referenced from multiple nodes 
due to the random pointers, ensure you are not making multiple copies of the same node.
Hint 2:
You may want to use extra space to keep old_node ---> new_node mapping to prevent creating multiple copies of the same node.
Hint 3:
We can avoid using extra space for old_node ---> new_node mapping by tweaking the original linked list. Simply interweave the 
nodes of the old and copied list. For example: Old List: A --> B --> C --> D InterWeaved List: A --> A' --> B --> B' --> C --> C' --> D --> D'
Hint 4:
The interweaving is done using next pointers and we can make use of interweaved structure to get the correct reference nodes 
for random pointers.


### Testcase:
---
[[7,null],[13,0],[11,4],[10,2],[1,0]]
[[1,1],[2,1]]
[[3,null],[3,0],[3,null]]

### Code:
---
'''
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
'''
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
             
"""
### Solution: -------------------------------------------------------------------------------------------------------------------------

class Node:
    """
    Node of a linked list with a random pointer.
    """
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        Creates a deep copy of a linked list where each node has a random pointer.

        Args:
        head (Optional[Node]): The head of the original linked list.

        Returns:
        Optional[Node]: The head of the deep copied linked list.
        """

        if not head:
            # If the original list is empty, return None
            return None

        # Step 1: Create a new node for each original node and interweave them
        current = head
        while current:
            new_node = Node(current.val, current.next)
            current.next = new_node
            current = new_node.next

        # Step 2: Update random pointers in the new nodes
        current = head
        while current:
            if current.random:
                current.next.random = current.random.next
            current = current.next.next

        # Step 3: Separate the interweaved list into the original and the copied list
        current_original = head
        current_new = head.next
        new_head = head.next  # This will be the head of the copied list

        while current_original:
            # Restore the next pointers of the original nodes
            current_original.next = current_original.next.next

            # Update the next pointers of the copied nodes
            current_new.next = current_new.next.next if current_new.next else None

            # Move to the next nodes in the respective lists
            current_original = current_original.next
            current_new = current_new.next

        return new_head


### Description: -----------------------------------------------------------------------------------------------------------------------
'''
### Code Explanation:

- **Class Node:** Represents a node in the linked list, each node having a `val`, `next`, and `random` pointer.
- **Function copyRandomList:**
  - **Input:** The head of the original linked list.
  - **Output:** The head of the new, deep-copied linked list.
  - **Process:**
    - **Interweaving Nodes:** For each node in the original list, a new node is created and placed next to it. 
        This step helps to keep a reference to the corresponding new node.
    - **Setting Random Pointers:** Random pointers of the new nodes are updated. If an original node's random 
        pointer points to some node, the corresponding new node's random pointer is set to point to the new node 
        next to the original node's random target.
    - **Separating Lists:** The original and new lists are separated. Each original node is reconnected to its 
        original `next` node, and each new node is connected to the next new node. The lists are separated into 
        their individual linked structures.

This code methodically constructs a deep copy of a linked list with random pointers, ensuring that the structure 
and connections in the new list precisely mirror those of the original list, without any shared nodes.


To create a deep copy of a linked list with a random pointer, we need to ensure that each new node in the copied list has the same 
value as its corresponding node in the original list, and its `next` and `random` pointers point to the new nodes in the copied list, 
not the original list.

### Algorithm:
1. **Iterate and Interweave:** 
   - First, iterate through the original list and create a new node for each existing node, placing the new node immediately after its 
   corresponding original node. This creates an interweaved list of original and copied nodes.

2. **Update Random Pointers:** 
   - Then, iterate through the list again and update the random pointers of the new nodes. The new node's random pointer should point 
   to the `next` of the original node's random pointer.

3. **Restore Original List and Extract Copy:** 
   - Finally, iterate through the list once more to separate the original and copied lists. Restore the original list by setting the
     `next` pointers of the original nodes as they were before and similarly update the `next` pointers of the copied nodes to separate 
     them from the interweaved list.


### Description:
- **Interweaving:** Creates new nodes and places them between the original nodes.
- **Updating Random Pointers:** Sets the `random` pointers of new nodes to the correct node in the copied list.
- **Separating Lists:** Restores the original list and constructs the copied list simultaneously.

This approach effectively creates a deep copy of the list with minimal space complexity, avoiding the need for additional hash tables to map
old nodes to new nodes. The interweaving technique allows us to maintain the connection between the original and copied nodes, simplifying the 
update of the `random` pointers.

'''
