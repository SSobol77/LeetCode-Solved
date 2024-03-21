# 206. Reverse Linked List.

# Topics: Linked List, Recursion.

'''
## Task:
--------
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []

Constraints:
The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000

Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?


## Testcase:
------------
[1,2,3,4,5]
[1,2]
[]

## Code:
--------
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
           
'''

# Solution: ---------------------------------------------------------------------------------------------------------

### Solution 1: Iterative Approach with Comments
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None  # Initialize previous node as None
        curr = head  # Start with the head as the current node
        while curr:  # Iterate until the end of the list
            next = curr.next  # Save the next node
            curr.next = prev  # Reverse current node's pointer
            prev = curr  # Move prev to the current node
            curr = next  # Move to the next node in the original list
        # At the end, prev will be the new head of the reversed list
        return prev


### Solution 2: Recursive Approach with Comments

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case: if list is empty or has a single node, return head
        if not head or not head.next:
            return head

        # Recursively reverse the rest of the list from the second node
        reversed_list = self.reverseList(head.next)

        # Reverse the link between the current node and the next node
        head.next.next = head
        # Set the current node's next pointer to None to avoid cycles
        head.next = None

        # Return the head of the reversed list
        return reversed_list


# Description: ================================================================================================
'''
To solve the problem of reversing a singly linked list, we can approach it in two ways: iteratively and recursively. 
Here, I'll provide solutions for both methods.

### Iterative Approach
In the iterative approach, we use a loop to reverse the links between nodes. We'll have three pointers: `prev`, `curr`, 
and `next`. Initially, `prev` is set to `None` and `curr` is set to the head of the list. In each iteration, we'll reverse 
the link between the current node and the next node, and then move the pointers one step forward.


### Recursive Approach
In the recursive approach, we dive to the end of the list and then start reversing the links as we backtrack. The base case 
occurs when we reach the end of the list (`head` is `None` or `head.next` is `None`). On backtracking, we set the `next` 
node's `next` pointer to the current node, effectively reversing the link, and then set the current node's `next` pointer 
to `None` to avoid cycles.

In the recursive solution, `reversed_list` holds the head of the reversed list, which is the last node we reach before hitting 
the base case. As we backtrack, we reverse the links and set the `next` pointer of the last node (which becomes the head of the 
reversed list) to `None` to complete the reversal.

'''

### Tests code:

# To test the iterative and recursive solutions for reversing a singly linked list, we can create a small testing framework. 
# This framework will include a function to build a linked list from a Python list, a function to convert a linked list back 
# to a Python list (for easy comparison), and finally, test cases to verify the correctness of both solutions.

# the test framework:
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseListIterative(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev

    def reverseListRecursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        reversed_list = self.reverseListRecursive(head.next)
        head.next.next = head
        head.next = None
        return reversed_list

def build_list(elements):
    """Build a linked list from a Python list and return the head."""
    head = current = None
    for element in elements:
        if not head:
            head = current = ListNode(element)
        else:
            current.next = ListNode(element)
            current = current.next
    return head

def to_list(head):
    """Convert a linked list back to a Python list."""
    elements = []
    while head:
        elements.append(head.val)
        head = head.next
    return elements

def test_solution():
    tests = [
        ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
        ([1, 2], [2, 1]),
        ([], []),
    ]
    solution = Solution()
    for input_list, expected_output in tests:
        head = build_list(input_list)
        
        # Test iterative solution
        reversed_head_iterative = solution.reverseListIterative(head)
        result_iterative = to_list(reversed_head_iterative)
        assert result_iterative == expected_output, f"Iterative failed for {input_list}. Expected {expected_output}, got {result_iterative}"

        # Since the list has been reversed, rebuild it for the recursive test
        head = build_list(input_list)

        # Test recursive solution
        reversed_head_recursive = solution.reverseListRecursive(head)
        result_recursive = to_list(reversed_head_recursive)
        assert result_recursive == expected_output, f"Recursive failed for {input_list}. Expected {expected_output}, got {result_recursive}"

    print("All tests passed!")

test_solution()

'''
This test framework defines a few utility functions:
    
- `build_list(elements)` takes a Python list and constructs a linked list.
- `to_list(head)` converts a linked list back into a Python list for easy comparison.
- `test_solution()` runs predefined test cases, including edge cases like an empty list, to ensure both iterative and 
   recursive solutions work as expected.

After running `test_solution()`, it will either print "All tests passed!" if all tests succeed, or it will raise an assertion 
error indicating which test case failed and why. This helps in quickly identifying and fixing any issues in the implementation.

'''
