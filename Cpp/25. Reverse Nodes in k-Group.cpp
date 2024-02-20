// 25. Reverse Nodes in k-Group.     - HARD -


// Topic: Linked List, Recursion.


/*
### Task:
---
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. 
If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]

Example 2:
Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]

Constraints:
The number of nodes in the list is n.
1 <= k <= n <= 5000
0 <= Node.val <= 1000

Follow-up: Can you solve the problem in O(1) extra memory space?

### Testcase:
---
[1,2,3,4,5]
2
[1,2,3,4,5]
3


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
    ListNode* reverseKGroup(ListNode* head, int k) {
        
    }
};

*/
// Solution: --------------------------------------------------------------------------------------

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
    ListNode* reverseKGroup(ListNode* head, int k) {
        if (!head || k == 1) return head;

        // Dummy node to simplify edge cases
        ListNode dummy(0);
        dummy.next = head;
        
        // Initialize pointers
        ListNode *cur = &dummy, *nex = &dummy, *pre = &dummy;
        int count = 0;
        
        // Count the number of nodes in the list
        while (cur->next) {
            cur = cur->next;
            count++;
        }

        // Loop through the list to reverse every k nodes
        while (count >= k) {
            cur = pre->next; // The current node to start reversing
            nex = cur->next; // The next node to be processed
            for (int i = 1; i < k; i++) {
                cur->next = nex->next;
                nex->next = pre->next;
                pre->next = nex;
                nex = cur->next;
            }
            pre = cur;
            count -= k;
        }

        return dummy.next;
    }
};


// Description: ==============================================================================================================
/*
Reversing nodes in k-group in a linked list is a more complex problem that involves reversing parts of the list while keeping 
the rest intact. This can be achieved through a combination of iterative or recursive approaches. Here, we'll discuss an iterative 
approach that uses constant extra space, aligning with the follow-up challenge to solve the problem in O(1) extra memory space.

The key steps in the iterative approach are:

1. **Count the Nodes**: Determine the length of the linked list to know how many complete groups of `k` we have to reverse.

2. **Reverse in Groups**: For each group of `k` nodes, reverse them. This involves standard linked list reversal techniques but 
     applied to a subsection of the list.

3. **Linking Groups**: After reversing a group, ensure that the reversed group is correctly connected to the rest of the list.

4. **Handling the Remainder**: If the list's length is not a multiple of `k`, the final set of nodes less than `k` will remain as is, 
     as per the problem statement.


### Description:

- **Dummy Node**: A dummy node is used to simplify edge cases, particularly when reversing the first group of nodes. It acts as a 
    previous node to the head of the list.

- **Counting Nodes**: The first loop counts the total number of nodes in the list to determine how many complete groups of `k` we have.

- **Reversing Groups**: The main while loop handles the reversal of each group. Within this loop, a for loop reverses the nodes in 
    the current group. The key here is to adjust the pointers correctly to reverse the nodes and then connect the reversed group back 
    to the main list.

- **Linking Groups**: After reversing a group, the `pre` pointer is moved to the last node of the reversed group, which is now the 
    starting point for the next group's reversal.

- **Handling Remainder**: The loop condition `count >= k` ensures that if there are fewer than `k` nodes remaining at the end of the 
    list, they are left as is, fulfilling the problem's requirement.

This solution effectively reverses nodes in groups of `k` while maintaining the overall structure of the list and uses O(1) extra space, 
as it only manipulates pointers without using additional data structures.

*/
