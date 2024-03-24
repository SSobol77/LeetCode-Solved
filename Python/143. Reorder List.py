# 143. Reorder List.

# Topics: Linked List, Two Pointers, Stack, Recursion.

'''
## Task:
You are given the head of a singly linked-list. The list can be represented as:
L0 → L1 → … → Ln - 1 → Ln

Reorder the list to be on the following form:
L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …

You may not modify the values in the list's nodes. Only nodes themselves may be changed.

Example 1:
Input: head = [1,2,3,4]
Output: [1,4,2,3]

Example 2:
Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]

Constraints:
The number of nodes in the list is in the range [1, 5 * 10^4].
1 <= Node.val <= 1000

## Testcase:
[1,2,3,4]
[1,2,3,4,5]

## Code:
---------
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
       
'''

## Solution:
from typing import Optional  # Import Optional from the typing module

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Base case: if the list is empty or has only one element, no reordering is needed
        if not head or not head.next:
            return

        # Step 1: Find the middle of the list using the slow and fast pointers
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next  # Slow pointer moves one step at a time
            fast = fast.next.next  # Fast pointer moves two steps at a time

        # At the end of the loop, slow pointer is at the middle of the list

        # Step 2: Reverse the second half of the list starting from slow.next
        second = slow.next  # The start of the second half
        prev = None  # Previous pointer to help in reversing
        slow.next = None  # Break the list into two halves
        while second:
            tmp = second.next  # Temporarily store the next node
            second.next = prev  # Reverse the current node's pointer
            prev = second  # Move the prev pointer forward
            second = tmp  # Move to the next node in the list

        # At the end of this loop, 'prev' points to the new head of the reversed second half

        # Step 3: Merge the two halves together
        first, second = head, prev  # 'first' points to the head of the first half, 'second' to the head of the reversed second half
        while second:
            # Temporarily store the next nodes of both halves
            tmp1, tmp2 = first.next, second.next

            # Reorder the nodes by pointing the current nodes to each other
            first.next = second  # Point the current node of the first half to the current node of the second half
            second.next = tmp1  # Point the current node of the second half to the next node of the first half

            # Move the pointers forward for the next iteration
            first, second = tmp1, tmp2


## Description:
'''
To reorder a linked list in the specified manner (L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …), we can break the problem 
down into three main steps:

1. **Find the Middle of the List**: Use the slow and fast pointer technique to find the middle of the list. The slow 
   pointer moves one step at a time, while the fast pointer moves two steps. When the fast pointer reaches the end, 
   the slow pointer will be at the middle.

2. **Reverse the Second Half of the List**: Reverse the list from the middle to the end. This can be done in-place 
   using a simple iterative approach.

3. **Merge the Two Halves**: Alternately merge the nodes from the first half and the reversed second half.


### Explanation:

- **Step 1**: Finding the middle of the list ensures that we can split the list into two roughly equal parts.

- **Step 2**: Reversing the second half inverts the order of the second part of the list, making it easy to reorder the list 
  as required.
  
- **Step 3**: Merging the two halves alternately achieves the desired reordering without modifying the node values, complying 
  with the constraints.

This solution effectively reorders the list in-place with a linear time complexity (O(n)), where n is the number of nodes in the 
list. It only uses a few pointers, so the space complexity is constant (O(1)).

'''
