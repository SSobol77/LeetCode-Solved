# 380. Insert Delete GetRandom O(1).            -Medium-

# Topic: Array, Hash Table, Math, Design, Randomized.

"""
### Task:
---
Implement the RandomizedSet class:

RandomizedSet() Initializes the RandomizedSet object.
bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
You must implement the functions of the class such that each function works in average O(1) time complexity.

#Example 1:
Input
["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]
Output
[null, true, false, true, 2, true, false, 2]

Explanation
RandomizedSet randomizedSet = new RandomizedSet();
randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2].
randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.
randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now contains [2].
randomizedSet.insert(2); // 2 was already in the set, so return false.
randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom() will always return 2.
 
#Constraints:
-2^31 <= val <= 2^31 - 1
At most 2 * 10^5 calls will be made to insert, remove, and getRandom.
There will be at least one element in the data structure when getRandom is called.


### Testcase:
---
["RandomizedSet","insert","remove","insert","getRandom","remove","insert","getRandom"]
[[],[1],[2],[2],[],[1],[2],[]]


### Code:
---
class RandomizedSet:

    def __init__(self):
        

    def insert(self, val: int) -> bool:
        

    def remove(self, val: int) -> bool:
        

    def getRandom(self) -> int:
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

"""
### Solution: ------------------------------------------------------------------------------

import random

class RandomizedSet:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.numMap = {}  # Maps value to its index in the nums array
        self.nums = []    # Holds the actual values

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.numMap:
            return False
        self.numMap[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.numMap:
            return False
        # Move the last element to the place idx of the element to delete
        last_element, idx = self.nums[-1], self.numMap[val]
        self.nums[idx], self.numMap[last_element] = last_element, idx
        # Remove the last element
        self.nums.pop()
        del self.numMap[val]
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.nums)

# Testcases
randomizedSet = RandomizedSet()
print(randomizedSet.insert(1))  # True
print(randomizedSet.remove(2))  # False
print(randomizedSet.insert(2))  # True
print(randomizedSet.getRandom()) # 1 or 2
print(randomizedSet.remove(1))  # True
print(randomizedSet.insert(2))  # False
print(randomizedSet.getRandom()) # 2

### Description: ============================================================
'''
The `RandomizedSet` class has been successfully implemented in Python. This class supports `insert`, `remove`, and `getRandom` operations, 
all in average O(1) time complexity. Here's a summary of the implementation:

- **`__init__`**: Initializes two data structures, a list `nums` to store the elements, and a dictionary `numMap` to map each value to its index in `nums`.

- **`insert`**: Adds an element to the set if it is not already present. It appends the element to the `nums` list and updates the `numMap`. 
                Returns `True` if the element was not present, `False` otherwise.

- **`remove`**: Removes an element from the set if it is present. To maintain O(1) complexity, it swaps the element with the last element 
                in the `nums` list and then removes the last element. Updates `numMap` accordingly. Returns `True` if the element was 
                present, `False` otherwise.

- **`getRandom`**: Returns a random element from the set. It uses `random.choice` to pick a random element from the `nums` list.

Here are the results of the test cases based on the example:

- Insert 1: Returns `True` as 1 was inserted successfully.
- Remove 2: Returns `False` as 2 does not exist in the set.
- Insert 2: Returns `True` as 2 was inserted successfully.
- getRandom: Returns either 1 or 2 randomly.
- Remove 1: Returns `True` as 1 was successfully removed.
- Insert 2: Returns `False` as 2 was already in the set.
- getRandom: Returns 2 as it is the only number in the set.

This implementation meets the specified requirements and constraints.

'''
