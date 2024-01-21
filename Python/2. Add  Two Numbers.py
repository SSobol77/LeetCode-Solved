# 2. Add  Two Numbers.

# Topic:

"""
### Task:
---
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, 
and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

#Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

#Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

#Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

#Constraints:
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
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

"""
### Solution:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(0)  # Create a dummy head for the result linked list
        current = dummy_head       # Initialize a pointer to the current node
        carry = 0                 # Initialize the carry
        
        while l1 or l2 or carry:
            # Get the values of the current nodes in l1 and l2 (if they exist)
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate the sum of values from l1, l2, and the carry
            total_sum = val1 + val2 + carry
            
            # Calculate the new carry for the next iteration
            carry = total_sum // 10
            
            # Create a new node with the remainder of total_sum (digit)
            current.next = ListNode(total_sum % 10)
            current = current.next  # Move the current pointer
            
            # Move l1 and l2 pointers if they exist
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        return dummy_head.next  # Return the result linked list starting from the next node of the dummy head


### Description:
'''
To add two numbers represented as linked lists, you can traverse both linked lists simultaneously, adding the corresponding 
digits and handling carry as you go.

This code iterates through both linked lists l1 and l2 simultaneously, adding the corresponding digits along with any carry 
from the previous step. The result is stored in a new linked list represented by dummy_head, and the final result is returned 
starting from the next node of the dummy_head.

The algorithm works in O(max(m, n)) time, where m and n are the lengths of l1 and l2, respectively, because it traverses both 
linked lists only once.

'''
