# 21. Merge Two Sorted Lists

# Topic: Linked List, Recursion.

"""
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


# Code:
---
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
"""
### Solution:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Base case: If one of the lists is empty, return the other list
        if not list1:
            return list2
        if not list2:
            return list1
        
        # Compare the values of the current nodes in both lists
        if list1.val < list2.val:
            # If list1's value is smaller, set list1's next to the merged result of list1's next and list2
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            # If list2's value is smaller or equal, set list2's next to the merged result of list1 and list2's next
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2

### Description:
'''
This code defines a recursive function mergeTwoLists that takes two linked lists list1 and list2 as input and returns 
the merged sorted linked list. The function handles the base cases where one of the lists is empty.

In the recursive step, the function compares the values of the current nodes in both lists. If the value in list1 is 
smaller, it recursively calls mergeTwoLists on the next node of list1 and list2. If the value in list2 is smaller or 
equal, it recursively calls mergeTwoLists on list1 and the next node of list2. This way, it merges the two lists while 
maintaining the sorted order.

The algorithm works in O(m + n) time, where m and n are the lengths of list1 and list2, respectively, because it 
traverses both lists once.

'''
