// 2. Add Two Numbers.


// Topic: Linked List, Math, Recursion.

/*
### Task:
---
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and 
each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 
Constraints:
The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.


### Testcase:
---
[2,4,3]
[5,6,4]
[0]
[0]
[9,9,9,9,9,9,9]
[9,9,9,9]


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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        
    }
};

*/

// Solution: ----------------------------------------------------------------------------------------------------

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        // Create a dummy head node to simplify adding new nodes to the result list
        ListNode dummyHead(0);
        // Use a pointer 'current' to keep track of the current node in the result list
        ListNode* current = &dummyHead;
        // Initialize 'carry' to store the carry-over value when summing digits
        int carry = 0;

        // Iterate through both linked lists until reaching the end of both
        while (l1 != nullptr || l2 != nullptr) {
            // Get the current value of l1, or 0 if l1 is null
            int x = (l1 != nullptr) ? l1->val : 0;
            // Get the current value of l2, or 0 if l2 is null
            int y = (l2 != nullptr) ? l2->val : 0;
            // Calculate the sum of the current digits and the carry
            int sum = carry + x + y;
            // Update 'carry' for the next iteration
            carry = sum / 10;
            // Create a new node with the digit value (sum % 10) and add it to the result list
            current->next = new ListNode(sum % 10);
            // Move 'current' to the newly added node
            current = current->next;

            // Move to the next node in l1 and l2, if available
            if (l1 != nullptr) l1 = l1->next;
            if (l2 != nullptr) l2 = l2->next;
        }

        // After processing both lists, if there's a remaining carry, add a new node for it
        if (carry > 0) {
            current->next = new ListNode(carry);
        }

        // The result list is next to the dummy head, so return dummyHead.next
        return dummyHead.next;
    }
};


// Description: =========================================================================================================
/*
### Explanation:
- **Dummy Head**: A dummy head node is used to simplify the logic for adding new nodes to the result list. It eliminates the need to handle the special case of initializing the head of the result list.
- **Current Pointer**: This pointer tracks the current node in the result list, allowing us to easily add new nodes.
- **Carry**: This variable holds the carry-over value when the sum of two digits exceeds 9.
- **While Loop**: The loop continues until both `l1` and `l2` have been fully traversed. It handles cases where `l1` and `l2` have different lengths by treating missing nodes as having a value of 0.
- **Sum Calculation**: For each pair of nodes, the sum includes the current digits from `l1` and `l2` and any carry from the previous addition.
- **New Node Creation**: A new node is created for each digit of the sum, and the carry is updated for the next iteration.
- **Remaining Carry**: If there's a carry left after the last addition, it's added as a new node at the end of the result list.
- **Return Statement**: The result list starts from `dummyHead.next`, skipping the dummy head node.

The solution to the "Add Two Numbers" problem involves adding two numbers represented by two linked lists, where each node contains a single digit of the number in reverse order. The goal is to return a new linked list representing the sum of the two numbers, also in reverse order. The solution employs a straightforward approach that closely mimics the manual addition process, digit by digit, taking care to handle the carry that may occur when the sum of two digits exceeds 9.

### Key Concepts:
- **Linked List Representation**: Each linked list node represents a single digit of a number, with the least significant digit at the head of the list. This reverse order simplifies the addition process as it aligns with how we naturally add numbers from right to left.
- **Carry Handling**: When adding two digits along with any existing carry, if the sum is 10 or more, the carry for the next addition is set to 1, and only the unit digit of the sum is used for the current position in the result list.
- **Unequal Lengths**: The two numbers may have different lengths. The solution handles this by continuing the addition process with the longer number once the shorter one is fully traversed, ensuring all digits are accounted for.
- **Final Carry**: After the last addition, if there's a remaining carry (i.e., the final sum is 10 or more), a new node with the carry value (1) is appended to the result list.

### Solution Overview:
1. **Initialization**: A dummy head node is created to simplify the process of adding new nodes to the result list. A variable `carry` is initialized to 0 to keep track of the carry from each digit addition.
2. **Iterative Addition**: The solution iterates through both linked lists simultaneously, adding corresponding digits along with the carry from the previous addition. A new node with the resulting digit is appended to the result list for each addition.
3. **Continuing with Longer List**: If one list is longer, the iteration continues with the remaining digits of the longer list, ensuring the carry is included in each addition.
4. **Handling Remaining Carry**: If there's a carry after the final addition, a new node with the carry value is appended to the result list.
5. **Returning the Result**: The result list is built starting from the node next to the dummy head, as the dummy head was used solely for simplification purposes and does not contain a digit of the sum.

### Efficiency:
- **Time Complexity**: The solution has a linear time complexity, O(max(N,M)), where N and M are the lengths of the two input linked lists. This is because it iterates through each list at most once.
- **Space Complexity**: The space complexity is also linear, O(max(N,M)), due to the new linked list created to store the sum, which in the worst case will have at most max(N,M) + 1 nodes (the extra node is for a possible carry at the end).

This approach is efficient and straightforward, closely mirroring the manual process of adding two numbers while taking advantage of the linked list structure to handle numbers of arbitrary length without conversion to other formats.

*/
