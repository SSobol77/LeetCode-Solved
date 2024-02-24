// 206. Reverse Linked List.

// Topic: Linked List, Recursion.


/*
### Task:
---
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []
 
Constraints:
The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
 
Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?

### Testcase:
---
[1,2,3,4,5]
[1,2]
[]


### Code:
---
// *
// * Definition for singly-linked list.
// * struct ListNode {
// *     int val;
// *     ListNode *next;
// *     ListNode() : val(0), next(nullptr) {}
// *     ListNode(int x) : val(x), next(nullptr) {}
// *     ListNode(int x, ListNode *next) : val(x), next(next) {}
// * };
// *
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        
    }
};
*/
// Solution: --------------------------------------

class Solution {
public:
    // Function that matches the test call, using the iterative approach
    ListNode* reverseList(ListNode* head) {
        return reverseListIterative(head);
    }

private:
    // Iterative solution for reversing the linked list
    ListNode* reverseListIterative(ListNode* head) {
        ListNode *prev = nullptr, *curr = head, *next = nullptr;
        while (curr) {
            next = curr->next;  // Store next node
            curr->next = prev;  // Reverse current node's pointer
            prev = curr;        // Move pointers one position ahead
            curr = next;
        }
        return prev;  // New head of the reversed list
    }

    // Recursive solution for reversing the linked list
    ListNode* reverseListRecursive(ListNode* head) {
        if (!head || !head->next) return head; // Base case: empty list or single node
        ListNode* restReversed = reverseListRecursive(head->next); // Recursively reverse the rest of the list
        head->next->next = head; // Set next node's next to current node
        head->next = nullptr;    // Set current node's next to nullptr
        return restReversed;     // Return the new head of the reversed list
    }
};



// Description: ===================================
/*
This solution provides two approaches to reverse a singly linked list: iterative and recursive. Both methods aim to rewire the `next` pointers of the nodes so that they point to their previous nodes, effectively reversing the direction of the list.

### Iterative Approach:
- **Initialization**: Start with three pointers: `prev` (initially `nullptr`), `curr` (pointing to the head of the list), and `next` (used to temporarily store the next node).
- **Traversal and Reversal**: Iterate through the list with `curr`, at each step:
  - Temporarily store the next node (`next = curr->next`).
  - Reverse the current node's pointer (`curr->next = prev`).
  - Move `prev` and `curr` pointers one step forward.
- **Termination**: When `curr` becomes `nullptr`, `prev` will be pointing at the new head of the reversed list, which is then returned.

### Recursive Approach:
- **Base Case**: If the list is empty (`head == nullptr`) or has only one node (`head->next == nullptr`), return `head` as it is already "reversed".
- **Recursive Step**: Assume the rest of the list is reversed, and you are left with the task of adding the initial head to the end of the reversed list.
  - Recursively reverse the rest of the list starting from the second node (`reverseListRecursive(head->next)`).
  - Make the next node of the original head (`head->next`, which is now the last node of the reversed sublist) point back to the head.
  - Set `head->next` to `nullptr` to break the original next link, making the original head the new tail.
- **Termination**: Return the head of the reversed list obtained from the recursive call, which bubbles up as the final result.

### Implementation:
The provided code defines a `Solution` class with three public methods: `reverseList`, `reverseListIterative`, and `reverseListRecursive`. The `reverseList` method is designed to be the primary interface, which internally calls the iterative approach (`reverseListIterative`). However, it can be easily modified to use the recursive approach by changing its implementation to call `reverseListRecursive`.

### Usage:
- The iterative method is straightforward and generally more efficient in terms of space usage as it does not incur the overhead of recursive calls.
- The recursive method, while elegant and a good demonstration of the divide-and-conquer strategy, uses additional stack space for recursive calls, which could be a concern for very long lists.

Both methods achieve the reversal of the linked list with linear time complexity, \( O(n) \), where \( n \) is the number of nodes in the list. The space complexity of the iterative method is \( O(1) \), while the recursive method has a space complexity of \( O(n) \) due to the recursive call stack.

*/
