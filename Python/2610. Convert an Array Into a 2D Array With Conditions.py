# 2610. Convert an Array Into a 2D Array With Conditions.

# Topics: Array, Hash Table.

'''
# Task:
------------

You are given an integer array nums. You need to create a 2D array from nums satisfying the following 
conditions:

    The 2D array should contain only the elements of the array nums.
    Each row in the 2D array contains distinct integers.
    The number of rows in the 2D array should be minimal.

Return the resulting array. If there are multiple answers, return any of them.

Note that the 2D array can have a different number of elements on each row.

Example 1:
Input: nums = [1,3,4,1,2,3,1]
Output: [[1,3,4,2],[1,3],[1]]
Explanation: We can create a 2D array that contains the following rows:
- 1,3,4,2
- 1,3
- 1
All elements of nums were used, and each row of the 2D array contains distinct integers, so it is a valid answer.
It can be shown that we cannot have less than 3 rows in a valid array.

Example 2:
Input: nums = [1,2,3,4]
Output: [[4,3,2,1]]
Explanation: All elements of the array are distinct, so we can keep all of them in the first row of the 2D array.

 Constraints:
    1 <= nums.length <= 200
    1 <= nums[i] <= nums.length

Hint 1:
Process the elements in the array one by one in any order and only create a new row in the matrix when we cannot put it into the existing rows
Hint 2:
We can simply iterate over the existing rows of the matrix to see if we can place each element.


# Testcase:
------------
[1,3,4,1,2,3,1]
[2,1,1]


# Code:
------------
class Solution(object):
    def findMatrix(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
'''
# Solution:
class Solution:
    def findMatrix(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []  # Initialize an empty list to store the 2D array

        for num in nums:  # Iterate through each number in nums
            placed = False  # Flag to check if the number is placed in any row

            # Check each row to see if the number can be placed
            for row in result:
                if num not in row:
                    row.append(num)  # Place the number in the row
                    placed = True
                    break  # Break as we have placed the number

            # If the number is not placed in any row, create a new row with this number
            if not placed:
                result.append([num])

        return result  # Return the resulting 2D array

# Test cases
solution = Solution()
print(solution.findMatrix([1,3,4,1,2,3,1]))  # Example 1
print(solution.findMatrix([2,1,1]))          # Additional test case


# Description

'''
To solve this problem, we will follow these steps:

    1. Initialize an empty list result which will store the 2D array.
    2. Iterate through each element in nums.
    3. For each element, we will check each row in result to see if the element can be placed in that row. 
       An element can be placed in a row if it is not already present in that row.
    4. If the element cannot be placed in any existing row, create a new row with this element.
    5. Continue this process until all elements in nums are placed in result.
    6. Return the result.
    
This code will create the 2D array as per the specified conditions. It's efficient for the given constraints, 
as it iterates over each element in nums only once and performs constant-time checks for each row in the result.

'''
