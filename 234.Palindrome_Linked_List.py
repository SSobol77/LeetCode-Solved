"""
# 234. Palindrome Linked List.


# Topic: Linked List, Two Pointers, Stack, Recursion.


# Task:
------------
Given the head of a singly linked list, return true if it is a palindrome
or false otherwise.

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
-------------
[1,2,2,1]
[1,2]


# Code:
--------------
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

"""
# Solution:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Helper function to reverse a linked list
        def reverseList(head):
            prev = None
            current = head
            # Iterating through the list to reverse it
            while current:
                next_temp = current.next  # Store the next node
                current.next = prev       # Reverse the current node's pointer
                prev = current            # Move prev to the current node
                current = next_temp       # Move to the next node in the original list
            return prev  # At the end, 'prev' will be the new head of the reversed list

        # Find the middle of the linked list using fast and slow pointers
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next          # Slow pointer moves one step
            fast = fast.next.next     # Fast pointer moves two steps

        # By the end of the loop, slow pointer reaches the middle of the list

        # Reverse the second half of the list starting from the middle
        slow = reverseList(slow)
        # Set 'fast' back to the beginning of the list
        fast = head

        # Compare the two halves
        while slow:
            # If values are different, then it's not a palindrome
            if slow.val != fast.val:
                return False
            slow = slow.next  # Move to the next node in the second half
            fast = fast.next  # Move to the next node in the first half

        # If all the values matched, return True indicating it's a palindrome
        return True



# Description:
'''
To solve the problem of determining if a linked list is a palindrome, the goal is to check if 
the list reads the same backward as forward. The challenge here is to do it in O(n) time and O(1) space. 
This rules out approaches that use extra space like converting the list to an array or using a stack.

Here's a step-by-step approach to solve this problem within the constraints:
-----------------------------------------------------------------------------

1. Find the Middle of the Linked List: 
   First, we need to find the middle of the list. We can do this using the fast and slow pointer technique. 
   The slow pointer moves one step at a time, while the fast pointer moves two steps. When the fast pointer 
   reaches the end of the list, the slow pointer will be at the middle.

2. Reverse the Second Half of the List: 
   Next, we reverse the second half of the list. We start reversing the list from the middle to the end.

3. Compare the Two Halves: 
   Finally, we compare the first half with the reversed second half. If they are identical, then the list 
   is a palindrome.

4. Restore the List (Optional): 
   If it's required to keep the original list unchanged, we would need to reverse the second half again to
   restore the list to its original order. However, this step is not necessary for just determining if the 
   list is a palindrome.

Detailed Explanation:
------------------------
1. Reverse List Function (Lines 5-13): This function reverses the linked list. It iterates through the list, 
   reversing the direction of each node's pointer.

2. Finding the Middle (Lines 16-19): The slow and fast pointers start at the head. The fast pointer moves two 
   steps for every one step the slow pointer moves. When the fast pointer reaches the end of the list, the slow 
   pointer will be at the middle.

3. Reversing Second Half (Line 21): The list is split into two halves at the middle. The second half is reversed 
   using the reverseList function.

4. Comparing Halves (Lines 23-28): The first half, starting from head, and the reversed second half, starting 
   from slow, are compared. If any corresponding nodes have different values, the function returns False.

5. Return Result (Line 30): If the entire list is traversed without finding any mismatch, the function returns 
   True, confirming the list is a palindrome.

'''