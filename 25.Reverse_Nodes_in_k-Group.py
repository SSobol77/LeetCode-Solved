"""
# 25. Reverse Nodes in k-Group.

# Topic: Linked List, Recursion.


# Task:
------------
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes 
is not a multiple of k then left-out nodes, in the end, should remain as it is.

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


# Testcase:
-------------
[1,2,3,4,5]
2
[1,2,3,4,5]
3


# Code:
------------
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

"""
# Solution:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Check if there are at least k nodes to reverse
        current = head
        count = 0
        while current and count < k:
            current = current.next
            count += 1
        # If fewer than k nodes, return the head as it is
        if count < k:
            return head

        # Reverse the first k nodes of the list
        prev, current = None, head
        for _ in range(k):
            temp = current.next  # Store the next node
            current.next = prev  # Reverse the link
            prev = current       # Move prev one step ahead
            current = temp       # Move current one step ahead

        # Recursively reverse the remaining list after the first k nodes
        # Then connect the last node of reversed k nodes to the returned head of the recursively reversed list
        head.next = self.reverseKGroup(current, k)

        # Return the new head of the reversed k nodes
        return prev



# Description:
'''
To solve the "Reverse Nodes in k-Group" problem, we will use recursion. The basic idea is to reverse every 
group of k nodes in the linked list. If there are fewer than k nodes remaining, we leave them as they are.

Here's a step-by-step approach:
--------------------------------------
1. Check if There are At Least k Nodes Left: Before reversing, we need to check if there are at least k nodes left in the list. 
   If not, we return the head as is.

2. Reverse k Nodes: Reverse the first k nodes of the list. This will be done using a standard reverse for a linked list.

3. Recursion: After reversing k nodes, we will have a new head for this part of the list. The remaining part of the list will 
   still be unprocessed. We will recursively call the same function for the remaining list.

4. Connect Reversed Parts: After the recursive call returns, we need to connect the reversed part with the rest of the list.

5. O(1) Space Complexity: To achieve O(1) extra space, we avoid using any additional data structures and use pointers to 
   manipulate the list in place.


In this code:
--------------------------
- We first traverse k nodes to check if there are enough nodes to reverse.
- If we have fewer than k nodes, we return the head without any changes.
- We reverse k nodes using a standard iterative approach for reversing a linked list.
- We then recursively call reverseKGroup for the list after the first k nodes.
- Finally, we connect the reversed part with the head of the recursively reversed part and return 
  the new head of the reversed list. This ensures that the list is reversed in groups of k nodes, 
  maintaining the integrity of the original l

'''
