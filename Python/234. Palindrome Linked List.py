# 234. Palindrome Linked List.
 
# Topics: Linked List, Two Pointers, Stack, Recursion.

'''
### Task:
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

# Testcase:
[1,2,2,1]
[1,2]

## Code:
---
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
  

'''

# Solution:
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Edge case: A single node or empty list is always a palindrome
        if not head or not head.next:
            return True
        
        # Step 1: Find the middle of the linked list using the two-pointer technique
        slow, fast = head, head  # Initialize slow and fast pointers
        while fast and fast.next:
            slow = slow.next  # Slow pointer moves one step
            fast = fast.next.next  # Fast pointer moves two steps
        
        # At this point, 'slow' is at the midpoint of the list
        
        # Step 2: Reverse the second half of the list starting from 'slow'
        prev = None  # Previous node, used to reverse the list
        while slow:
            tmp = slow.next  # Temporary storage for the next node
            slow.next = prev  # Reverse the 'next' pointer
            prev = slow  # Move 'prev' to the current node
            slow = tmp  # Proceed to the next node in the original list
        
        # 'prev' now points to the head of the reversed second half
        
        # Step 3: Compare the first half and the reversed second half node-by-node
        left, right = head, prev  # 'left' will traverse the first half, 'right' the second
        while right:  # Only need to traverse the second half (which might be shorter)
            if left.val != right.val:
                return False  # Mismatch found, not a palindrome
            left = left.next  # Move to the next node in the first half
            right = right.next  # Move to the next node in the second half
        
        # If we reach this point, all corresponding nodes matched, so it's a palindrome
        return True


# Description:
'''
To solve the problem of determining whether a singly linked list is a palindrome, we need to compare the first 
half of the list with the reversed second half. However, since we're working with a linked list, we don't have 
direct access to the middle of the list without traversing it. Therefore, the challenge lies in finding the middle 
of the list, reversing the second half, and then comparing it with the first half, all while adhering to the 
constraint of doing it in O(n) time and O(1) space.

Here's a step-by-step approach:

1. **Find the middle of the linked list**: We can achieve this by using the two-pointer technique. We'll have a 
slow pointer and a fast pointer, both starting at the head of the list. The slow pointer moves one step at a time, 
while the fast pointer moves two steps at a time. When the fast pointer reaches the end of the list, the slow pointer 
will be at the middle.

2. **Reverse the second half of the list**: Once we have the middle of the list, we reverse the second half. This can 
be done in-place by changing the next pointers of the nodes.

3. **Compare the two halves**: Finally, we compare the values of the nodes in the first half with the values of the 
nodes in the reversed second half. If all corresponding nodes are equal, the list is a palindrome.

4. **Restore the list (optional)**: If required, we can reverse the second half again to restore the list to its original 
state before returning the result.

This solution meets the requirement of O(n) time complexity, as each node is visited a constant number of times. It also 
meets the O(1) space complexity requirement since we are only using a fixed amount of extra space for pointers.

'''
