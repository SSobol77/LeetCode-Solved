// 148. Sort List.


// Topic: Linked List, Two Pointers, Divide and Conquer, Sorting, Merge Sort.

/*
### Task:
---
Given the head of a linked list, return the list after sorting it in ascending order.

Example 1:
Input: head = [4,2,1,3]
Output: [1,2,3,4]

Example 2:
Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]

Example 3:
Input: head = []
Output: []

Constraints:
The number of nodes in the list is in the range [0, 5 * 10^4].
-10^5 <= Node.val <= 10^5

Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?

### Testcase:
---
[4,2,1,3]
[-1,5,3,4,0]
[]


### Code:
---
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
    ListNode* sortList(ListNode* head) {
        
    }
};
*/
// Solution: --------------------------------------

class Solution {
public:
    // Main function to sort the linked list
    ListNode* sortList(ListNode* head) {
        // Base case: an empty list or a single node list is already sorted.
        if (!head || !head->next) return head;

        // Use fast and slow pointers to find the middle of the list.
        // `prev` will track the node before the slow pointer for splitting the list.
        ListNode *slow = head, *fast = head, *prev = nullptr;
        while (fast && fast->next) {
            prev = slow;          // Keep track of the node before slow.
            slow = slow->next;    // Slow pointer moves one step.
            fast = fast->next->next; // Fast pointer moves two steps.
        }
        prev->next = nullptr; // Split the list into two halves at the middle.

        // Recursively sort the two halves of the list.
        ListNode* l1 = sortList(head);  // Sort the first half.
        ListNode* l2 = sortList(slow);  // Sort the second half.

        // Merge the two sorted halves.
        return mergeTwoLists(l1, l2);
    }

private:
    // Helper function to merge two sorted linked lists.
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        // Dummy node acts as a starting point for the merged list.
        ListNode dummy(0);
        ListNode* tail = &dummy; // Tail pointer for building the merged list.

        // Iterate through both lists, selecting the smaller current node each time.
        while (l1 && l2) {
            if (l1->val < l2->val) {
                tail->next = l1; // Append l1 to the merged list.
                l1 = l1->next;   // Move to the next node in l1.
            } else {
                tail->next = l2; // Append l2 to the merged list.
                l2 = l2->next;   // Move to the next node in l2.
            }
            tail = tail->next; // Move the tail pointer forward.
        }

        // Connect the remaining nodes of l1 or l2 to the merged list.
        if (l1) tail->next = l1;
        if (l2) tail->next = l2;

        // The merged list starts after the dummy node.
        return dummy.next;
    }
};


// Description: ===================================
/*
To sort a linked list in ascending order with the constraints specified, the most efficient approach is to use the Merge Sort algorithm.
Merge Sort is well-suited for linked lists due to its O(n log n) time complexity and the ability to be implemented with O(1) space 
complexity, not counting the input.

Merge Sort for linked lists follows a divide-and-conquer strategy:
1. **Divide**: Recursively split the linked list into two halves. The division continues until each sublist contains only one element 
   or is empty.
2. **Conquer**: Sort each pair of elements in a merge-like fashion, and then merge the sorted sublists to form a sorted list.

Here's a step-by-step guide for implementing `sortList`:

### Function `sortList(ListNode* head)`:

- If the list is empty or contains only one element, it is already sorted, so return `head`.
- Use the fast and slow pointer technique to find the middle of the list. The slow pointer moves one step at a time, while the fast 
  pointer moves two steps. When the fast pointer reaches the end, the slow pointer will be at the middle.
- Split the list into two halves at the middle, making the `next` of the middle node `nullptr`.
- Recursively call `sortList` on the two halves to sort them individually.
- Merge the two sorted halves into a single sorted list.

### Function `mergeTwoLists(ListNode* l1, ListNode* l2)`:

- This function will merge two sorted lists into a single sorted list.
- Use a dummy head to simplify edge cases and maintain a current pointer to build the merged list.
- Iterate through both lists, appending the smaller current element to the merged list and advancing the pointer in that list.
- After reaching the end of one list, connect the remaining elements of the other list to the merged list.
- Return the next of the dummy head, which is the start of the merged list.

This solution adheres to the O(n log n) time complexity requirement due to the nature of Merge Sort and manages to keep the space 
complexity at O(1) by sorting the list in-place, meeting the follow-up challenge.

*/