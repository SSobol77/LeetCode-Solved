// 25. Reverse Nodes in k-Group

/*
### Task:
--------
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes
is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

#Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]

#Example 2:
Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]

#Constraints:
The number of nodes in the list is n.
1 <= k <= n <= 5000
0 <= Node.val <= 1000

### Code:
------

 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };

class Solution {
public:
    ListNode* reverseKGroup(ListNode* head, int k) {

    }
};



*/

// Solution:
class Solution {
public:
    ListNode* reverseKGroup(ListNode* head, int k) {
        // Create a dummy node to serve as the new head
        ListNode* dummy = new ListNode(0);
        dummy->next = head;

        ListNode* prev_group_end = dummy; // Initialize the previous group's end

        while (true) {
            ListNode* group_start = prev_group_end->next; // Start of the current group
            ListNode* group_end = group_start; // Initialize the end of the current group

            // Check if there are k nodes in the current group
            for (int i = 0; i < k; i++) {
                if (!group_end) {
                    return dummy->next; // Not enough nodes to reverse, return the list
                }
                group_end = group_end->next;
            }

            // Reverse the k nodes in the current group
            ListNode* prev = nullptr;
            ListNode* current = group_start;

            while (current != group_end) {
                ListNode* next_temp = current->next;
                current->next = prev;
                prev = current;
                current = next_temp;
            }

            // Connect the reversed group to the previous group
            prev_group_end->next = prev;
            group_start->next = current;

            // Update the previous group's end to the current group's end
            prev_group_end = group_start;
        }

        return dummy->next; // Return the modified linked list
    }
};

// Description:
/*
This code reverses nodes in groups of k in the linked list iteratively. It maintains a dummy
node as the new head and uses prev_group_end to keep track of the end of the previous group.
It iterates through the list, reverses each group of k nodes, and connects them to the previous
group. The process continues until there are no more groups of k nodes to reverse.

The time complexity of this solution is O(n), where n is the number of nodes in the linked list.

*/
