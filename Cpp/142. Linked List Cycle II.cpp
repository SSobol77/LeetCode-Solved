// 142. Linked List Cycle II.


// Topic: Hash Table, Linked List, Two Pointers.


/*
### Task:
---
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next 
pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 
if there is no cycle. Note that pos is not passed as a parameter.

Do not modify the linked list.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.

Example 2:
Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.

Example 3:
Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.
 
Constraints:
The number of the nodes in the list is in the range [0, 104].
-10^5 <= Node.val <= 10^5
pos is -1 or a valid index in the linked-list.

Follow up: Can you solve it using O(1) (i.e. constant) memory?


### Testcase:
---
[3,2,0,-4]
1
[1,2]
0
[1]
-1


### Code:
---
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 *//*
class Solution {
public:
    ListNode *detectCycle(ListNode *head) {
        
    }
};
*/


// Solution: --------------------------------------

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *detectCycle(ListNode *head) {
        if (!head || !head->next) {
            return nullptr; // No cycle if there are 0 or 1 nodes
        }
        
        ListNode* slow = head;
        ListNode* fast = head;
        
        // Detect cycle
        while (fast && fast->next) {
            slow = slow->next;
            fast = fast->next->next;
            if (slow == fast) {
                break; // Cycle detected
            }
        }
        
        // No cycle if fast pointer reached end of list
        if (!fast || !fast->next) {
            return nullptr;
        }
        
        // Move slow pointer to head and advance both pointers at same pace until they meet
        slow = head;
        while (slow != fast) {
            slow = slow->next;
            fast = fast->next;
        }
        
        return slow; // Return the node where the cycle begins
    }
};


// Description: ===================================
/*
To find the node where the cycle begins in a linked list, we can use the "Two Pointers" approach again. We'll use the same concept 
of slow and fast pointers to detect the cycle, but with an additional step to find the starting node of the cycle.

This solution has a time complexity of O(N), where N is the number of nodes in the linked list, and a space complexity of O(1), 
since we only use constant extra space regardless of the size of the input linked list.

*/
