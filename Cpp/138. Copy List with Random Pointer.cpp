// 138. Copy List with Random Pointer.


// Topic: Hash Table, Linked List.


/*
### Task:
---
A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

    val: an integer representing Node.val
    random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.

Your code will only be given the head of the original linked list.

Example 1:
Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

Example 2:
Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]

Example 3:
Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]

Constraints:
0 <= n <= 1000
-10^4 <= Node.val <= 10^4
Node.random is null or is pointing to some node in the linked list.

Hint 1:
Just iterate the linked list and create copies of the nodes on the go. Since a node can be referenced from multiple nodes due to the random pointers, ensure you are not making multiple copies of the same node.
Hint 2:
You may want to use extra space to keep old_node ---> new_node mapping to prevent creating multiple copies of the same node.
Hint 3:
We can avoid using extra space for old_node ---> new_node mapping by tweaking the original linked list. Simply interweave the nodes of the old and copied list. For example: Old List: A --> B --> C --> D InterWeaved List: A --> A' --> B --> B' --> C --> C' --> D --> D'
Hint 4:
The interweaving is done using next pointers and we can make use of interweaved structure to get the correct reference nodes for random pointers.

### Testcase:
---
[[7,null],[13,0],[11,4],[10,2],[1,0]]
[[1,1],[2,1]]
[[3,null],[3,0],[3,null]]


### Code:
---
/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*//*

class Solution {
public:
    Node* copyRandomList(Node* head) {
        
    }
};

*/
// Solution: ----------------------------------------------------------------------------------------


/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/
class Solution {
public:
    Node* copyRandomList(Node* head) {
        if (!head) return nullptr; // If the list is empty, return null

        // Step 1: Clone and interweave
        Node* curr = head;
        while (curr) {
            Node* clone = new Node(curr->val); // Create a new node with the value of the current node
            clone->next = curr->next; // Link the clone's next pointer to the current node's next
            curr->next = clone; // Insert the clone right after the current node
            curr = clone->next; // Move to the next original node
        }

        // Step 2: Update random pointers for the cloned nodes
        curr = head;
        while (curr) {
            if (curr->random) {
                curr->next->random = curr->random->next; // Set the clone's random pointer to the clone of the current node's random
            }
            curr = curr->next->next; // Move to the next original node
        }

        // Step 3: Unweave the lists to separate the original and the cloned list
        Node* dummy = new Node(0); // Dummy head for the cloned list
        Node* cloneCurr = dummy; // Pointer to build the cloned list
        curr = head; // Reset curr to the head of the interweaved list
        while (curr) {
            cloneCurr->next = curr->next; // Link the cloned node to the cloned list
            cloneCurr = cloneCurr->next; // Move the cloneCurr pointer forward
            curr->next = curr->next->next; // Restore the original list's next pointers
            curr = curr->next; // Move to the next original node
        }

        return dummy->next; // The cloned list starts at dummy's next
    }
};


// Description: ===========================================================================================================
/*
To create a deep copy of a linked list with a random pointer, we can follow the hints provided and use an approach that interweaves 
the original and copied nodes. This method eliminates the need for extra space for old-to-new node mapping. The process can be broken 
down into three main steps:

1. **Clone and Interweave**: Iterate through the original list and create a cloned node for each original node. Insert each cloned 
     node immediately after its original node, effectively interweaving the original and cloned nodes.

2. **Update Random Pointers**: Iterate through the list again, this time updating the random pointers of the cloned nodes. Given 
     an original node `A`, `A.next` will be its clone, and `A.random.next` will be the clone of `A.random` (if `A.random` is not `null`).

3. **Unweave**: Separate the interwoven list into the original list and the cloned list, restoring the original list and extracting the 
     cloned list.


### Description:

- **Step 1 (Clone and Interweave)**: For each node in the original list, a cloned node is created and placed immediately after it. This step modifies the original list but sets up a structure that simplifies the next steps.

- **Step 2 (Update Random Pointers)**: The cloned nodes' random pointers are updated. Since each cloned node is immediately after its original, `curr->next` is the clone of `curr`, and `curr->random->next` is the clone of `curr->random`.

- **Step 3 (Unweave)**: The original and cloned lists are separated. A dummy head is used for the cloned list to simplify the process. The `next` pointers of the original nodes are restored, and the cloned list is built simultaneously.

This approach efficiently creates a deep copy of the list with random pointers without using extra space for node mapping, adhering to the O(1) space complexity constraint.

*/
