// 234. Palindrome Linked List.


// Topic: Linked List, Two Pointers, Stack, Recursion.


/*
### Task:
---
Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

Example 1:
Input: head = [1,2,2,1]
Output: true

Example 2:
Input: head = [1,2]
Output: false

Constraints:
The number of nodes in the list is in the range [1, 10^5].
0 <= Node.val <= 9

Follow up: Could you do it in O(n) time and O(1) space?

### Testcase:
---
[1,2,2,1]
[1,2]


### Code:
---
**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 *
class Solution {
public:
    bool isPalindrome(ListNode* head) {
        
    }
};
*/
// Solution: --------------------------------------

class Solution {
public:
    bool isPalindrome(ListNode* head) {
        if (!head || !head->next) return true;

        // Step 1: Find the middle of the list
        ListNode *slow = head, *fast = head;
        while (fast && fast->next) {
            slow = slow->next;
            fast = fast->next->next;
        }

        // Step 2: Reverse the second half
        ListNode* prev = nullptr;
        while (slow) {
            ListNode* nextTemp = slow->next;
            slow->next = prev;
            prev = slow;
            slow = nextTemp;
        }

        // Step 3: Compare the first half and the reversed second half
        ListNode* left = head;
        ListNode* right = prev; // Start of reversed second half
        while (right) { // No need to check the first half, as it's either equal in length or one node longer
            if (left->val != right->val) return false;
            left = left->next;
            right = right->next;
        }

        // Optional Step 4: Restore the list (if needed)
        // This part would reverse the second half back to its original order
        // Not included here to meet the O(1) space requirement

        return true;
    }
};

// Description: ===================================
/*
To determine if a singly linked list is a palindrome, we need to compare the first half of the list with the reversed second half. Achieving this in O(n) time and O(1) space adds a layer of complexity, as it requires modifying the list (at least temporarily) to reverse the second half.

### Approach:
1. **Find the Middle**: Use the fast and slow pointer technique to find the middle of the list (slow pointer ends up at the middle when the fast pointer reaches the end).
2. **Reverse Second Half**: Reverse the list starting from the slow pointer, so the second half of the list is in reverse order.
3. **Compare Halves**: Compare the values from the beginning of the list and from the middle to the end (now reversed) to check if they are the same.
4. **Restore List (Optional)**: If the original list needs to be preserved, reverse the second half again to restore the list to its original state.

### Explanation:
- **Time Complexity**: O(n), where n is the number of nodes in the list. Each step of the approach (finding the middle, reversing the second half, and comparing the two halves) involves a linear scan of part of the list.
- **Space Complexity**: O(1), as we're only using a fixed number of pointers and not utilizing any additional data structures that grow with the size of the input.

### Follow-up Consideration:
- The follow-up challenge is addressed by the above solution, which runs in O(n) time and uses O(1) space. Note that while we modify the list by reversing the second half, this is done in place, maintaining constant space usage. If the problem requires the list to remain unchanged, additional steps to restore the list would slightly increase the complexity but still remain within the O(n) time and O(1) space bounds.

*/
