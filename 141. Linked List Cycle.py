# 141. Linked List Cycle.

# Topic: Hash Table, Linked List, Two Pointers.

"""
### Task:
---
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously 
following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is 
connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

#Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

#Example 2:
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

#Example 3:
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.

#Constraints:
The number of the nodes in the list is in the range [0, 104].
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
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
"""
### Solution: -------------------------------------------------------------------------------------------------------

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # If the list is empty or has only one node, return False as no cycle can exist
        if not head or not head.next:
            return False

        # Initialize two pointers - slow and fast
        slow = head  # Slow pointer moves one step at a time
        fast = head.next  # Fast pointer is initially one step ahead of slow

        # Traverse the list until the end is reached or a cycle is detected
        while fast and fast.next:
            # If slow and fast pointers meet, a cycle is detected
            if slow == fast:
                return True

            # Move slow pointer by one step
            slow = slow.next

            # Move fast pointer by two steps
            fast = fast.next.next

        # If end of list is reached without slow and fast meeting, no cycle exists
        return False



### Description: -----------------------------------------------------------------------------------------------------
'''
### Explanation of the Comments:

- The `ListNode` class represents a node in the linked list.
- The `Solution` class contains the method `hasCycle`.
- The `hasCycle` method begins by checking if the linked list is too short to contain a cycle.
- Two pointers, `slow` and `fast`, are initialized. `slow` moves one node at a time, while `fast` moves two nodes.
- The while loop continues as long as `fast` and `fast.next` are not `None`.
- Inside the loop, if `slow` and `fast` meet, it indicates a cycle, and `True` is returned.
- If the loop ends without the pointers meeting, the method returns `False`, indicating no cycle.

To solve the problem of detecting a cycle in a linked list, we can use the two-pointer technique, often referred to as 
the "Floyd's Tortoise and Hare" algorithm. This approach involves using two pointers that move at different speeds, a 
slow pointer (the tortoise) and a fast pointer (the hare). The slow pointer moves one step at a time, while the fast 
pointer moves two steps at a time.

### Algorithm:
1. Initialize two pointers, slow and fast, both pointing to the head of the linked list.
2. Traverse the linked list with these pointers:
   - Move the slow pointer by one step (`slow = slow.next`).
   - Move the fast pointer by two steps (`fast = fast.next.next`).
3. If at any point the fast pointer meets the slow pointer (i.e., `slow == fast`), a cycle is detected, and the function returns `True`.
4. If the fast pointer reaches the end of the list (`fast` is `None` or `fast.next` is `None`), there is no cycle, and the function returns `False`.
5. Continue this process until a cycle is found or the end of the list is reached.

### Implementation:
Here's how the `Solution` class and the `hasCycle` method can be implemented:

### Description of the Solution:
- The function `hasCycle` takes the head of the linked list as its argument.
- If the list is empty or has only one node, it immediately returns `False` as a cycle is not possible.
- Both `slow` and `fast` pointers start at the head, with `fast` initially one step ahead.
- As long as `fast` and `fast.next` are not `None`, the loop continues, moving the `slow` pointer by one step and the `fast` pointer by two steps.
- If at any point `slow` equals `fast`, it means there's a cycle in the list.
- If the end of the list is reached (`fast` or `fast.next` becomes `None`), it means there is no cycle.

This solution satisfies the constraint of using O(1) memory and efficiently detects a cycle in the linked list.
'''