// 24. Swap Nodes in Pairs.


// Topic: Linked List, Recursion.


/*
### Task:
---
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the 
values in the list's nodes (i.e., only nodes themselves may be changed.)

Example 1:
Input: head = [1,2,3,4]
Output: [2,1,4,3]

Example 2:
Input: head = []
Output: []

Example 3:
Input: head = [1]
Output: [1]

Constraints:
The number of nodes in the list is in the range [0, 100].
0 <= Node.val <= 100

### Testcase:
---
[1,2,3,4]
[]
[1]

### Code:
---
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 *//*
class Solution {
public:
    ListNode* swapPairs(ListNode* head) {
        
    }
};

*/
// Solution: ----------------------------------------------------------------------------------------------


/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* swapPairs(ListNode* head) {
        // Base case: if the list is empty or has only one node, return head
        if (head == nullptr || head->next == nullptr) {
            return head;
        }

        // Nodes to be swapped
        ListNode* first = head;
        ListNode* second = head->next;

        // Swapping
        first->next = swapPairs(second->next); // Recursively swap the rest of the list
        second->next = first; // Update the next pointer of the second node to point to the first node

        // Return the new head of the list
        return second;
    }
};


// Description: ====================================================================================================================
/*
To swap every two adjacent nodes in a linked list, we can use a recursive approach. The idea is to swap the first two nodes and then 
ecursively call the function for the rest of the list. The base case for the recursion is when we reach the end of the list or have 
only one node left, in which case there's nothing to swap.

Here's a step-by-step guide to implementing this solution:

1. **Base Case**: If the list is empty (`head == nullptr`) or has only one node (`head->next == nullptr`), there's nothing to swap, 
     so we return the `head`.

2. **Swapping Nodes**: For the current pair of nodes, we swap them by adjusting their `next` pointers. Let's call the first node in 
     the pair `first` and the second node `second`.

3. **Recursive Call**: After swapping the first two nodes, we make a recursive call for the rest of the list starting from the third 
     node (`second->next`). The result of this recursive call will be the new next node for the `first` node.

4. **Updating Pointers**: We update the `next` pointer of the `second` node to point to the `first` node, effectively swapping the 
     two nodes. Then, we set the `next` pointer of the `first` node to the result of the recursive call, which is the head of the 
     swapped list for the rest of the nodes.

5. **Return**: Since we swapped the first two nodes, the new head of the list is the `second` node, so we return `second`.


### Description:

- **Base Case**: The recursion terminates when it encounters an empty list or a list with a single node, as no swapping is needed.

- **Swapping Nodes**: The first two nodes are identified as `first` and `second`. The `first` node's `next` pointer is set to the 
    result of a recursive call starting from `second->next`, effectively linking the `first` node to the head of the swapped remainder 
    of the list.

- **Recursive Call**: The recursive call continues to swap pairs of nodes for the rest of the list, linking each swapped pair back to 
    the previously swapped nodes.

- **Return Value**: The `second` node becomes the new head of the list after the swap, so it is returned as the result of the 
    function call.

This recursive approach elegantly handles the swapping of adjacent nodes in pairs and works for lists of any size, including empty 
lists and lists with an odd number of nodes.

*/
