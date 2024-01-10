"""
# 1146. Snapshot Array


# Topic: Array, Hash Table, Binary Search, Design.


# Task:
--------------------
Implement a SnapshotArray that supports the following interface:

- SnapshotArray(int length) initializes an array-like data structure with the given length. Initially, 
  each element equals 0.
- void set(index, val) sets the element at the given index to be equal to val.
- int snap() takes a snapshot of the array and returns the snap_id: the total number of times we 
  called snap() minus 1.
- int get(index, snap_id) returns the value at the given index, at the time we took the snapshot 
  with the given snap_id

Example 1:

Input: ["SnapshotArray","set","snap","set","get"]
[[3],[0,5],[],[0,6],[0,0]]
Output: [null,null,0,null,5]
Explanation: 
SnapshotArray snapshotArr = new SnapshotArray(3); // set the length to be 3
snapshotArr.set(0,5);  // Set array[0] = 5
snapshotArr.snap();  // Take a snapshot, return snap_id = 0
snapshotArr.set(0,6);
snapshotArr.get(0,0);  // Get the value of array[0] with snap_id = 0, return 5

Constraints:
1 <= length <= 5 * 10^4
0 <= index < length
0 <= val <= 10^9
0 <= snap_id < (the total number of times we call snap())
At most 5 * 10^4 calls will be made to set, snap, and get.

Hint 1:
Use a list of lists, adding both the element and the snap_id to each index.



# Testcase:
----------------------
["SnapshotArray","set","snap","set","get"]
[[3],[0,5],[],[0,6],[0,0]]



# Code:
------------------------
class SnapshotArray:

    def __init__(self, length: int):
        

    def set(self, index: int, val: int) -> None:
        

    def snap(self) -> int:
        

    def get(self, index: int, snap_id: int) -> int:
        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)

"""

# Solution:

class SnapshotArray:
    def __init__(self, length: int):
        # Each element of the array is a list of (snap_id, value) tuples.
        self.array = [[(-1, 0)] for _ in range(length)]
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        # If the current snap_id is already present at the index, update the value.
        # Otherwise, append a new (snap_id, value) tuple.
        if self.array[index][-1][0] == self.snap_id:
            self.array[index][-1] = (self.snap_id, val)
        else:
            self.array[index].append((self.snap_id, val))

    def snap(self) -> int:
        # Increment snap_id and return the previous snap_id.
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        # Use binary search to find the most recent value at or before the given snap_id.
        snapshots = self.array[index]
        left, right = 0, len(snapshots) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if snapshots[mid][0] <= snap_id:
                left = mid + 1
            else:
                right = mid - 1
        return snapshots[right][1]


# ----------------------------------------------------------------------
# Description:
'''
We used efficient approach for the get method to reduce the time complexity of retrieving values. 
Instead of iterating backwards through snapshots, we can utilize binary search to find the most 
recent snapshot before or at the given snap_id. This significantly improves the performance for 
the get method.

Explanation:

1. Initialization (__init__): 
   Initializes an array where each element is a list of (snap_id, value) tuples. The initial value 
   for each index is (snap_id=-1, value=0).

2. Set Method (set): Appends a new (snap_id, value) tuple to the list at the specified index if the 
   current snap_id is not present. If the current snap_id is already present, it updates the value 
   for that snap_id.

3. Snap Method (snap): Increments the snap_id and returns the previous snap_id.

4. Get Method (get): Implements binary search on the list of snapshots for the specified index to 
   efficiently find the most recent snapshot at or before the given snap_id.

Complexity Analysis:

Time Complexity:
- For set: O(1) for each call, as we are either updating the last element or appending a new element to 
  the list.
- For get: O(log s) for each call, where s is the number of snapshots for the given index, due to binary 
  search. 

Space Complexity: 
O(n * s), where n is the length of the SnapshotArray and s is the number of snapshots. 
This remains the same as the initial implementation.

This optimized solution offers a significant improvement in the time complexity of the get method, 
especially when the number of snapshots is large.

'''
