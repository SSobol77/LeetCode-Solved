// 21. Merge Two Sorted Lists.


// Topic: Linked List, Recursion.


/*
### Task:
---
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]

Constraints:
The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.


### Testcase:
---
[1,2,4]
[1,3,4]
[]
[]
[]
[0]


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
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        
    }
};
*/


// Solution: -------------------------------------------------------------------------------------

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
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        // Base cases
        if (list1 == nullptr) return list2;
        if (list2 == nullptr) return list1;
        
        // Recursive case
        if (list1->val < list2->val) {
            list1->next = mergeTwoLists(list1->next, list2);
            return list1;
        } else {
            list2->next = mergeTwoLists(list1, list2->next);
            return list2;
        }
    }
};


// Description: ======================================================================================
/*
To merge two sorted linked lists into one sorted list, we can use a recursive approach. The idea is to compare the values of the nodes at the heads of the two lists, and recursively call the function to merge the rest of the lists, setting the next pointer of the smaller node to the result of the recursive call. This approach elegantly handles the merging process and naturally sorts the merged list.

### Description:

1. **Base Cases**: If one of the lists is empty (`nullptr`), we return the other list. This is because there's nothing left to merge if one list is empty, so the other list is already the merged result.

2. **Recursive Case**: We compare the values of the current nodes of `list1` and `list2`. 
   - If `list1`'s value is smaller, we set `list1->next` to the result of a recursive call with `list1->next` and `list2`. This effectively inserts `list1`'s current node into the merged list and continues the merge process with the rest of `list1` and `list2`.
   - If `list2`'s value is smaller or equal, we do the opposite: set `list2->next` to the result of a recursive call with `list1` and `list2->next`, inserting `list2`'s current node into the merged list.

This recursive approach ensures that at each step, the smallest node between `list1` and `list2` is added to the merged list, maintaining the sorted order. The recursion continues until both lists are fully merged, at which point the base cases terminate the recursion and the head of the merged list is returned.

*/
