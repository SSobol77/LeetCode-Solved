# 83. Remove Duplicates from Sorted List.

# Topic: Linked List

'''
# Task:
----------
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. 
Return the linked list sorted as well.

Example 1:
Input: head = [1,1,2]
Output: [1,2]

Example 2:
Input: head = [1,1,2,3,3]
Output: [1,2,3]

Constraints:
The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.


# Testcase:
---------------
[1,1,2]
[1,1,2,3,3]

# Code:
---------------
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
       
'''
# Solution:
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize 'current' to the head of the linked list
        current = head

        # Traverse the list while 'current' and 'current.next' are not None
        while current and current.next:
            # Check if the current node's value equals the next node's value
            if current.val == current.next.val:
                # Skip the next node by pointing current.next to current.next.next
                current.next = current.next.next
            else:
                # Move to the next node if no duplicate is found
                current = current.next

        # Return the modified list with duplicates removed
        return head

# The Solution class and the deleteDuplicates method are now defined. 
# Below are the test cases to validate the implementation.

# Test cases
sol = Solution()

# Test case 1: Create a linked list [1,1,2]
head1 = ListNode(1, ListNode(1, ListNode(2)))
# Call deleteDuplicates and store the result
result1 = sol.deleteDuplicates(head1)
# Convert the result to a list for easy verification
output1 = []
while result1:
    output1.append(result1.val)
    result1 = result1.next
print(output1)  # Expected output: [1, 2]

# Test case 2: Create a linked list [1,1,2,3,3]
head2 = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))
# Call deleteDuplicates and store the result
result2 = sol.deleteDuplicates(head2)
# Convert the result to a list for easy verification
output2 = []
while result2:
    output2.append(result2.val)
    result2 = result2.next
print(output2)  # Expected output: [1, 2, 3]

# Description:
'''
In this code:

-The ListNode class represents a node in a singly-linked list.
-The Solution class contains the method deleteDuplicates, which removes duplicates from a sorted linked list.
-The deleteDuplicates method iterates through the list, removing duplicates by skipping over them.
-Two test cases are created and processed to verify the implementation. The results are printed as lists for easy reading.

'''
