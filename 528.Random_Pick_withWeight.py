"""
# 528. Random Pick with Weight

# Topic: Array, Math, Binary Search,Prefix Sum, Randomized.

# Task:
---------------
You are given a 0-indexed array of positive integers w where w[i] describes the weight of the i^th index.

You need to implement the function pickIndex(), which randomly picks an index in the range [0, w.length - 1] (inclusive) and returns it. The probability of picking an index i is w[i] / sum(w).

For example, if w = [1, 3], the probability of picking index 0 is 1 / (1 + 3) = 0.25 (i.e., 25%), and the probability of picking index 1 is 3 / (1 + 3) = 0.75 (i.e., 75%).

Example 1:
Input
["Solution","pickIndex"]
[[[1]],[]]
Output
[null,0]

Explanation
Solution solution = new Solution([1]);
solution.pickIndex(); // return 0. The only option is to return 0 since there is only one element in w.

Example 2:
Input
["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
[[[1,3]],[],[],[],[],[]]
Output
[null,1,1,1,1,0]

Explanation
Solution solution = new Solution([1, 3]);
solution.pickIndex(); // return 1. It is returning the second element (index = 1) that has a probability of 3/4.
solution.pickIndex(); // return 1
solution.pickIndex(); // return 1
solution.pickIndex(); // return 1
solution.pickIndex(); // return 0. It is returning the first element (index = 0) that has a probability of 1/4.

Since this is a randomization problem, multiple answers are allowed.
All of the following outputs can be considered correct:
[null,1,1,1,1,0]
[null,1,1,1,1,1]
[null,1,1,1,0,0]
[null,1,1,1,0,1]
[null,1,0,1,0,0]
......
and so on.


Constraints:
1 <= w.length <= 10^4
1 <= w[i] <= 10^5
pickIndex will be called at most 10^4 times.


# Testcase:
------------------------
["Solution","pickIndex"]
[[[1]],[]]
["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
[[[1,3]],[],[],[],[],[]]


# Code:
------------------------
class Solution:

    def __init__(self, w: List[int]):
        

    def pickIndex(self) -> int:
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()

"""
# Solution:
import random
import bisect

class Solution:
    def __init__(self, w: List[int]):
        self.prefixSums = []  # Initialize an array to store prefix sums
        prefixSum = 0
        # Calculate prefix sums from the weights
        for weight in w:
            prefixSum += weight  # Add current weight to the cumulative sum
            self.prefixSums.append(prefixSum)  # Append cumulative sum to the prefix sums array
        self.totalSum = prefixSum  # Store the total sum of weights

    def pickIndex(self) -> int:
        # Generate a random number between 1 and the total sum of weights
        target = random.randint(1, self.totalSum)
        # Use binary search to find the index where the target fits in the prefix sums array
        # The bisect_left function returns the index where the target should be inserted to maintain sorted order
        # This index corresponds to the original index in the weights array
        return bisect.bisect_left(self.prefixSums, target)

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()





#-------------------------------------------------------------------------------------------------
# Description:
'''
To implement the "Random Pick with Weight" problem, we need to design a Solution class that 
can randomly pick an index based on the weights provided in the array w. The probability of 
picking an index is proportional to its weight.

The solution involves two steps:
---------------------------------
    Creating a Prefix Sum Array:
        Create a cumulative sum array (prefixSums) from the weights. Each element in prefixSums 
        represents the sum of weights up to that index. This transforms the weights into a range 
        of sums, where each range corresponds to an index in the original array.

    Implementing pickIndex Method:
        Randomly pick a number between 1 and the total sum of weights.
        Use binary search on the prefix sum array to find the index corresponding to the randomly 
        picked number. The index found will be proportional to the weight of the index in the 
        original array.

        
Explanation:
--------------
-    In the constructor (__init__), we calculate the prefix sum array. This helps in determining 
     the ranges of sums each index corresponds to.
-    In the pickIndex method, we generate a random number between 1 and the total sum of weights. 
     We then use binary search (here, bisect_left) to find the index in the prefix sum array where 
     this random number would fit. The index found in the prefix sum array corresponds to the index 
     in the original weights array, ensuring that indexes with higher weights have a proportionally 
     higher chance of being picked.

This solution efficiently handles the weighted random picking by precomputing the prefix sums and using 
binary search, making the pickIndex operation very efficient.

'''