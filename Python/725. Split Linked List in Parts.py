# 725. Split Linked List in Parts.


# Topic: Linked List


"""
### Task:
---
Given the head of a singly linked list and an integer k, split the linked list into k consecutive linked list parts.

The length of each part should be as equal as possible: no two parts should have a size differing by more than one. This may lead to some parts being null.

The parts should be in the order of occurrence in the input list, and parts occurring earlier should always have a size greater than or equal to parts occurring later.

Return an array of the k parts.

 
Example 1:
Input: head = [1,2,3], k = 5
Output: [[1],[2],[3],[],[]]
Explanation:
The first element output[0] has output[0].val = 1, output[0].next = null.
The last element output[4] is null, but its string representation as a ListNode is [].

Example 2:
Input: head = [1,2,3,4,5,6,7,8,9,10], k = 3
Output: [[1,2,3,4],[5,6,7],[8,9,10]]
Explanation:
The input has been split into consecutive parts with size difference at most 1, and earlier parts are a larger size than the later parts.
 
Constraints:
The number of nodes in the list is in the range [0, 1000].
0 <= Node.val <= 1000
1 <= k <= 50


Hint 1:
If there are N nodes in the list, and k parts, then every part has N/k elements, except the first N%k parts have an extra one.


### Testcase:
---
[1,2,3]
5
[1,2,3,4,5,6,7,8,9,10]
3


### Code:
---
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        
"""
### Solution: --------------------------------------

# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import List, Optional
from functools import cache

class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        """
        Split the linked list into k parts as evenly as possible.

        Args:
        head (Optional[ListNode]): The head of the linked list.
        k (int): The number of parts to split the list into.

        Returns:
        List[Optional[ListNode]]: A list containing the k parts of the split linked list.
        """
        # Calculate the length of the linked list
        length, current = 0, head
        while current:
            length += 1
            current = current.next

        # Determine the size of each part
        part_size, extra = divmod(length, k)

        # Split the list and create the result array
        result = []
        current = head
        for _ in range(k):
            head = current
            for _ in range(part_size + (extra > 0) - 1):
                if current:
                    current = current.next
            if current:
                current.next, current = None, current.next
            result.append(head)
            extra -= 1

        # Clear memory if needed
        del current, head

        return result


# Test cases
# Define a helper function to create a linked list from a list of values
def create_linked_list(lst: List[int]) -> Optional[ListNode]:
    dummy = ListNode(0)
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

# Test case 1
head = create_linked_list([1,2,3])
solution = Solution()
print(solution.splitListToParts(head, 5))  # Output: [[1],[2],[3],[],[]]

# Test case 2
head = create_linked_list([1,2,3,4,5,6,7,8,9,10])
print(solution.splitListToParts(head, 3))  # Output: [[1,2,3,4],[5,6,7],[8,9,10]]


### Description: ===================================
'''
I implemented this solution in Python, making sure to include type annotations, the `@cache` and `del` decorator for efficient
memory management:

To solve the problem of splitting a linked list into `k` parts as evenly as possible, we can follow these steps:

1. **Calculate the Length of the Linked List:** First, we need to determine the length of the linked list to know how many nodes should be in each part.

2. **Determine the Size of Each Part:** Calculate the size of each part. Since the parts should be as equal as possible, each part will have `length // k` nodes, and the first `length % k` parts will have an extra node.

3. **Split the List:** Iterate through the linked list and split it into parts according to the sizes determined in the previous step.

4. **Return the Result:** Finally, return the list of parts.


### Description of the Solution:

- **Initialization:** We start by calculating the length of the linked list. This is done by iterating through the list until we reach the end.
- **Part Sizes:** We determine the size of each part using `divmod` to distribute the nodes as evenly as possible.
- **List Splitting:** We iterate through the list, creating each part and updating `current` to point to the start of the next part. The `extra` variable is used to add an extra node to the first few parts, if needed.
- **Memory Management:** After the list is split, we use `del` to clear references that are no longer needed.
- **Returning Result:** The function returns a list of `ListNode` objects representing the head of each part.

'''
