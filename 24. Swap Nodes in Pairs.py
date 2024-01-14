# 24. Swap Nodes in Pairs.

# Topic: Linked List, Recursion.

"""
### Task:
---
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values 
in the list's nodes (i.e., only nodes themselves may be changed.)

#Example 1:
Input: head = [1,2,3,4]
Output: [2,1,4,3]

#Example 2:
Input: head = []
Output: []

#Example 3:
Input: head = [1]
Output: [1]

#Constraints:
The number of nodes in the list is in the range [0, 100].
0 <= Node.val <= 100


### Testcase:
---
[1,2,3,4]
[]
[1]


### Code:
---
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
"""

### Solution: -----------------------------------------------------------------------------------------

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Swaps every two adjacent nodes in a linked list.

        Args:
        head (Optional[ListNode]): The head of the linked list.

        Returns:
        Optional[ListNode]: The head of the modified linked list after swapping pairs.
        """
        # Base case: if the list is empty or has only one node
        if not head or not head.next:
            return head

        # Nodes to be swapped
        first_node = head
        second_node = head.next

        # Swapping
        first_node.next = self.swapPairs(second_node.next)
        second_node.next = first_node

        # New head after swapping
        return second_node


### Description: --------------------------------------------------------------------------------------
'''
To solve this problem, we can use a recursive approach to swap every two adjacent nodes in the linked list. 
The base cases are when the list is empty (null) or when there is only one node left, in which case there's no pair to swap.

### Algorithm:
1. **Base Case Check:** 
   - If the head is null (empty list) or if there is only one node (head.next is null), return the head.

2. **Swapping Nodes:** 
   - Store the second node as it will become the new head after the swap.
   - Recursively call the function for the rest of the list starting from the third node.
   - Change the next of the second node to the first node.
   - Change the next of the first node to the head returned by the recursive call (this is the head of the swapped sublist).

3. **Return the New Head:** 
   - Return the second node which is the new head of the swapped list.



### Description:
- **Recursive Approach:** The function is called recursively for every two nodes.
- **Swapping Logic:** The pointers are modified to swap the nodes without changing their values.
- **Base Case Handling:** The function returns the same head if there's only one or no nodes left, ensuring that the list's 
    end is handled properly.

This solution effectively

swaps pairs of nodes in the linked list using recursion. It's efficient and maintains the original node structure without modifying 
the values inside the nodes. This method is well-suited for linked lists where direct access to nodes is not possible, and we need 
to traverse the list sequentially. The recursive approach simplifies the logic, especially when dealing with linked lists, by breaking 
down the problem into smaller, manageable sub-problems.

'''
