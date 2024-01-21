# 142. Linked List Cycle II.

# Topic: Hash Table, Linked List, Two Pointers.

"""
### Task:
---
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.

Do not modify the linked list.

#Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.

#Example 2:
Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.

#Example 3:
Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.

#Constraints:
The number of the nodes in the list is in the range [0, 10^4].
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
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        

"""
### Solution: --------------------------------------------------------------------------------------------------

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Step 1: Initialize two pointers, slow and fast, both starting at the head of the linked list
        slow, fast = head, head
        
        # Use Floyd's Tortoise and Hare algorithm to detect the presence of a cycle
        while fast and fast.next:
            # Move slow pointer one step at a time
            slow = slow.next
            # Move fast pointer two steps at a time
            fast = fast.next.next
            
            # If there's a cycle, slow and fast will meet at some point within the cycle
            if slow == fast:
                break
        else:
            # No cycle found, return None
            return None
        
        # Step 2: Find the node where the cycle begins
        # Reset the slow pointer to the head of the linked list, and move both pointers at the same pace
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        
        # Return the node where the cycle begins
        return slow


### Description: -----------------------------------------------------------------------------------------------
'''
**Problem Description:**

You are given the head of a singly-linked list. Your task is to determine whether there is a cycle in the linked list. If a cycle exists, 
find and return the node where the cycle begins. If there is no cycle, return `None`.

In this problem, a cycle in a linked list is defined as a situation where a node can be reached again by continuously following the `next` 
pointers within the list. The `head` of the linked list is the starting point, and the `next` pointer of the last node in the list may point 
to a previous node, creating a loop. The problem provides an integer `pos` to denote the index of the node where the tail's `next` pointer 
is connected to, with a `0`-based indexing system. If there is no cycle, `pos` is set to `-1`.

**Solution Approach:**

The problem can be efficiently solved using the Floyd's Tortoise and Hare algorithm, also known as the cycle detection algorithm. This algorithm 
involves two pointers: one slow (tortoise) and one fast (hare). The algorithm works as follows:

1. Initialize both the slow and fast pointers to the `head` of the linked list.

2. Move the slow pointer one step at a time and the fast pointer two steps at a time.

3. If there is a cycle in the linked list, the fast pointer will eventually catch up to the slow pointer, and they will meet at some node within 
   the cycle. This is the key detection step.

4. Once the meeting point is found, reset one of the pointers (e.g., slow) to the `head` of the list and keep the other pointer (e.g., fast) at 
   the meeting point. Move both pointers one step at a time.

5. When the slow and fast pointers meet again, the node at which they meet is the starting point of the cycle.

By applying this algorithm, we can efficiently detect the presence of a cycle and find the node where the cycle begins, if one exists, while using 
constant space (O(1)).

**Time Complexity:**

The time complexity of this algorithm is O(n), where n is the number of nodes in the linked list, as both pointers traverse the list once. This makes 
the algorithm very efficient for large linked lists.

'''
