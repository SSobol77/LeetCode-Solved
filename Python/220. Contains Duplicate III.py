# 220. Contains Duplicate III.          - HARD -

# Topic: Array, Sliding Window, Sorting, Bucket Sort, Ordered Set.

"""
### Task:
---
You are given an integer array nums and two integers indexDiff and valueDiff.

Find a pair of indices (i, j) such that:

    i != j,
    abs(i - j) <= indexDiff.
    abs(nums[i] - nums[j]) <= valueDiff, and

Return true if such pair exists or false otherwise.

Example 1:
Input: nums = [1,2,3,1], indexDiff = 3, valueDiff = 0
Output: true
Explanation: We can choose (i, j) = (0, 3).
We satisfy the three conditions:
i != j --> 0 != 3
abs(i - j) <= indexDiff --> abs(0 - 3) <= 3
abs(nums[i] - nums[j]) <= valueDiff --> abs(1 - 1) <= 0

Example 2:
Input: nums = [1,5,9,1,5,9], indexDiff = 2, valueDiff = 3
Output: false
Explanation: After trying all the possible pairs (i, j), we cannot satisfy the three conditions, so we return false.
 
Constraints:
2 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
1 <= indexDiff <= nums.length
0 <= valueDiff <= 10^9

Hint 1:
Time complexity O(n logk) - This will give an indication that sorting is involved for k elements.
Hint 2:
Use already existing state to evaluate next state - Like, a set of k sorted numbers are only needed to be tracked. When we are processing the next number in array, then we can utilize the existing sorted state and it is not necessary to sort next overlapping set of k numbers again.


### Testcase:
---
[1,2,3,1]
3
0
[1,5,9,1,5,9]
2
3


### Code:
---
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:

"""
### Solution: --------------------------------------------------------------------------------------

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        if valueDiff < 0: return False  # Negative valueDiff means no solution exists
        bucket = {}
        w = valueDiff + 1  # Bucket width

        for i, num in enumerate(nums):
            bucket_id = num // w
            # Check if the bucket already contains a nearby almost duplicate
            if bucket_id in bucket:
                return True

            # Check neighbors
            if bucket_id - 1 in bucket and abs(num - bucket[bucket_id - 1]) < w:
                return True
            if bucket_id + 1 in bucket and abs(num - bucket[bucket_id + 1]) < w:
                return True

            # Add to bucket
            bucket[bucket_id] = num

            # Remove old value if outside the indexDiff window
            if i >= indexDiff:
                del bucket[nums[i - indexDiff] // w]

        return False


# Test cases
sol = Solution()
print(sol.containsNearbyAlmostDuplicate([1,2,3,1], 3, 0))  # Output: true
print(sol.containsNearbyAlmostDuplicate([1,5,9,1,5,9], 2, 3))  # Output: false



### Description: ============================================================================================
'''
The "Contains Duplicate III" problem is a more complex variant of the previous "Contains Duplicate" problems. 
This time, we need to find if there are any pairs `(i, j)` in the array such that `i != j`, `abs(i - j) <= indexDiff`, 
and `abs(nums[i] - nums[j]) <= valueDiff`. 

Given the constraints and the hints, a good approach to this problem is to use a sliding window combined with a sorted 
data structure. One efficient way to implement this is using a balanced binary search tree (like a TreeSet in Java), 
but Python does not have a built-in TreeSet. However, we can use a SortedList from the `sortedcontainers` module, which 
maintains the elements in sorted order and provides logarithmic time operations, or we can simulate this behavior using buckets.

### Approach Using Buckets
We can bucketize the numbers so that numbers in the same bucket or adjacent buckets are guaranteed to be within `valueDiff`. 
The size of each bucket will be `valueDiff + 1`. Then, we use a sliding window of size `indexDiff` to check for the condition.


### Explanation:
- **Bucketization**: Each number is assigned to a bucket based on its value. Buckets have a width of `valueDiff + 1`. This ensures 
    that numbers in the same or neighboring buckets are within `valueDiff`.
- **Sliding Window**: We maintain a sliding window of size `indexDiff`. As we traverse the array, we check if there is any almost 
    duplicate in the current or neighboring buckets.
- **Early Exit**: If `valueDiff` is negative, we return `False` immediately, as it's impossible to satisfy the condition.
- **Removing Old Elements**: To maintain the window size, we remove the element that falls out of the `indexDiff` range from its bucket.

This solution efficiently checks for almost duplicate values within a specified index and value difference, ensuring compliance 
with the given constraints.

'''

