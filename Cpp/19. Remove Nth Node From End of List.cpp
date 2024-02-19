// 19. Remove Nth Node From End of List.

// Topic: Linked List, Two Pointers.


/*
### Task:
---
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]

Constraints:
The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz

Hint 1:
Maintain two pointers and update one with a delay of n steps.

### Testcase:
---
[1,2,3,4,5]
2
[1]
1
[1,2]
1


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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        
    }
};


*/
// Solution: --------------------------------------

class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode dummy(0); // Dummy node to handle edge cases, like removing the head
        dummy.next = head;
        ListNode* fast = &dummy;
        ListNode* slow = &dummy;

        // Advance fast pointer so that the gap between fast and slow is n nodes apart
        for (int i = 0; i <= n; ++i) {
            fast = fast->next;
        }

        // Move fast to the end, maintaining the gap
        while (fast != nullptr) {
            slow = slow->next;
            fast = fast->next;
        }

        // Skip the desired node
        ListNode* toDelete = slow->next;
        slow->next = slow->next->next;

        // Free memory if necessary (depending on the environment)
        delete toDelete;

        return dummy.next; // Return the new head
    }
};


// Description: ===================================
/*
To solve the "Remove Nth Node From End of List" problem, we can use the two-pointer technique, also known as the "fast and slow pointer" technique. This approach allows us to locate the nth node from the end of the list in a single pass, making the solution efficient.

### Steps:
1. **Initialize Two Pointers**: Start with two pointers, `fast` and `slow`, both pointing to the head of the list.
2. **Advance `fast` Pointer**: Move the `fast` pointer `n` steps ahead. This creates a gap of `n` nodes between `fast` and `slow`.
3. **Move Both Pointers**: Move both `fast` and `slow` pointers simultaneously until `fast` reaches the last node. At this point, `slow` will be just before the node to be removed.
4. **Remove Nth Node**: Adjust the `next` pointer of the `slow` node to skip the nth node from the end.
5. **Edge Case - Removing the First Node**: If the node to be removed is the first node, the `fast` pointer will reach the end after the initial advance, and `slow` will still point to the head. In this case, return `head->next`.


### Explanation:
- The `dummy` node simplifies edge cases, especially when the head of the list needs to be removed.
- The `fast` pointer is advanced `n + 1` steps from the dummy (which is effectively `n` steps from the head), creating the required gap.
- Both pointers are then moved together until `fast` reaches the end. At this point, `slow` is just before the node to be removed.
- The node after `slow` is then skipped over, effectively removing it from the list.
- The function returns `dummy.next`, which is the head of the modified list.

### Complexity:
- **Time Complexity**: O(L), where L is the number of nodes in the list. The algorithm makes one pass through the list.
- **Space Complexity**: O(1), as it uses a constant amount of space regardless of the input list size.

*/
