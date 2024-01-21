# 23. Merge k Sorted Lists.

# Topics: Linked List, Divide and Conquer, Heap (Priority Queue), Merge Sort.


'''
# Task:
----------------------------------
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Example 2:
Input: lists = []
Output: []

Example 3:
Input: lists = [[]]
Output: []

Constraints:
k == lists.length
0 <= k <= 10^4
0 <= lists[i].length <= 500
-104 <= lists[i][j] <= 10^4
lists[i] is sorted in ascending order.
The sum of lists[i].length will not exceed 10^4.


# Testcase
-------------
Case 1
[[1,4,5],[1,3,4],[2,6]]
Case 2
[]
Case 3
[[]]

# Code:
--------------------------------------
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
  
'''

# Solution:

class ListNode:
    # Definition for singly-linked list nodes
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists):
        import heapq  # Importing heapq for heap operations

        # Initialize a min heap
        min_heap = []
        for list_node in lists:
            while list_node:
                # Pushing each value from each linked list into the min heap
                heapq.heappush(min_heap, list_node.val)
                list_node = list_node.next  # Move to next node

        # Create a dummy node to serve as the start of the merged list
        dummy = ListNode()
        current = dummy
        while min_heap:
            # Pop the smallest value from the heap and add it to the merged list
            val = heapq.heappop(min_heap)
            current.next = ListNode(val)
            current = current.next  # Move to next node

        return dummy.next  # Return the merged list starting from dummy's next node

# Helper function to create a linked list from a list of values
def create_linked_list(values):
    dummy = ListNode()
    current = dummy
    for val in values:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

# Test cases
sol = Solution()

# Case 1: Merging lists [1,4,5], [1,3,4], and [2,6]
lists1 = [create_linked_list([1, 4, 5]), create_linked_list([1, 3, 4]), create_linked_list([2, 6])]

# Case 2: Merging an empty list of lists
lists2 = []

# Case 3: Merging a list of an empty list
lists3 = [create_linked_list([])]

# Function to convert a linked list to a Python list for easy verification
def linked_list_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

# Results
result1 = linked_list_to_list(sol.mergeKLists(lists1))
result2 = linked_list_to_list(sol.mergeKLists(lists2))
result3 = linked_list_to_list(sol.mergeKLists(lists3))

result1, result2, result3


# Description:
#---------------------------------------------------------------------
'''
Description of the Solution:

* Heap for Efficient Merging: The solution uses a min heap to store and sort all the nodes from the k linked 
  lists. By leveraging the properties of a heap, we can always get the smallest element efficiently, which
  is crucial for merging sorted lists.

* ListNode Class: A simple class for linked list nodes is defined, which has a val attribute for the value 
  and a next attribute pointing to the next node.

* MergeKLists Method: This is the core method that merges the k sorted linked lists.
    - It first iterates through each list and inserts all its elements into a min heap.
    - Then, it removes elements from the heap one by one (which comes out in sorted order due to the 
      heap's properties) and constructs the merged linked list.

* Helper Functions:
   - create_linked_list is used to convert a Python list to a linked list, which is useful for creating 
     test cases.
   - linked_list_to_list converts a linked list back into a Python list for easier result verification.

* Test Cases: The solution is tested with three cases: merging non-empty lists, an empty list of lists, and
  a list containing an empty list. The results are converted to Python lists for easy verification.

This approach is efficient for merging k sorted lists, especially when k is large, as it minimizes the 
number of comparisons needed to find the next smallest item to add to the merged list.

'''
