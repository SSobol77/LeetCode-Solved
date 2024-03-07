// 876. Middle of the Linked List.


// Topic: Linked List, Two Pointers.


/*
### Task:
---
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

Example 1:
Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.

Example 2:
Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.

Constraints:
The number of nodes in the list is in the range [1, 100].
1 <= Node.val <= 100

### Testcase:
---
[1,2,3,4,5]
[1,2,3,4,5,6]


### Code:
---
//**
// * Definition for singly-linked list.
// * struct ListNode {
// *     int val;
// *     ListNode *next;
// *     ListNode() : val(0), next(nullptr) {}
// *     ListNode(int x) : val(x), next(nullptr) {}
// *     ListNode(int x, ListNode *next) : val(x), next(next) {}
// * };

class Solution {
public:
    ListNode* middleNode(ListNode* head) {
        
    }
};

*/


// Solution: -------------------------------------------------------------------------


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
    ListNode* middleNode(ListNode* head) {
        ListNode *slow = head, *fast = head;

        // Loop until fast reaches the end of the list
        while (fast != nullptr && fast->next != nullptr) {
            slow = slow->next;      // Move slow pointer one step
            fast = fast->next->next; // Move fast pointer two steps
        }

        // When fast reaches the end, slow is at the middle
        return slow;
    }
};



// Description: =======================================================================================================
/*
To solve the "Middle of the Linked List" task, you can employ the two-pointer technique, also known as the "slow and fast pointer" method. 
This approach involves having two pointers traverse the linked list at different speeds: the slow pointer moves one node at a time, while 
the fast pointer moves two nodes at a time. When the fast pointer reaches the end of the list, the slow pointer will be at the midpoint of 
the list. If the list has an even number of nodes, the slow pointer will end up at the second of the two middle nodes, satisfying the 
problem's requirement to return the second middle node in such cases.

Here's a step-by-step breakdown of the solution:

1. Initialize two pointers, `slow` and `fast`, at the head of the linked list.
2. Traverse the list with both pointers until the fast pointer reaches the end of the list. For each iteration, move `slow` one node 
   forward (`slow = slow->next`), and `fast` two nodes forward (`fast = fast->next->next`), checking at each step that `fast` and 
   `fast->next` are not `nullptr` to avoid accessing a non-existent node.
3. When the loop terminates, `slow` will be at the middle node (or the second middle node in the case of an even number of nodes in the 
   list). Return `slow`.

### Description:
This code defines a function `middleNode` that takes the head of a singly linked list and returns the middle node. It utilizes the 
two-pointer technique to efficiently find the middle by advancing one pointer (`slow`) at half the speed of the other (`fast`). 
This ensures that when `fast` reaches the end, `slow` will be at the middle. The function handles both odd and even lengths of lists, 
returning the second middle node for even-length lists as per the problem statement.

*/
