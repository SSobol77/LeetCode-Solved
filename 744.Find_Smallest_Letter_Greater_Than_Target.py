# 744. Find Smallest Letter Greater Than Target.

# Topic: Array, Binary Search.

'''
# Task:
-----------------
You are given an array of characters letters that is sorted in non-decreasing order, 
and a character target. There are at least two different characters in letters.

Return the smallest character in letters that is lexicographically greater than target. 
If such a character does not exist, return the first character in letters.

Example 1:
Input: letters = ["c","f","j"], target = "a"
Output: "c"
Explanation: The smallest character that is lexicographically greater than 'a' in letters is 'c'.

Example 2:
Input: letters = ["c","f","j"], target = "c"
Output: "f"
Explanation: The smallest character that is lexicographically greater than 'c' in letters is 'f'.

Example 3:
Input: letters = ["x","x","y","y"], target = "z"
Output: "x"
Explanation: There are no characters in letters that is lexicographically greater than 'z' so we 
return letters[0].
 
Constraints:
2 <= letters.length <= 10^4
letters[i] is a lowercase English letter.
letters is sorted in non-decreasing order.
letters contains at least two different characters.
target is a lowercase English letter.

Hint 1:
Try to find whether each of 26 next letters are in the given string array.


# Testcase:
-----------------
["c","f","j"]
"a"
["c","f","j"]
"c"
["x","x","y","y"]
"z"


# Code:
-----------------
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        
'''
# Solution:
from typing import List

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # Initialize left and right pointers for binary search
        left, right = 0, len(letters) - 1

        while left <= right:
            # Find the middle index between left and right
            mid = (left + right) // 2

            # If the letter at mid is less than or equal to the target,
            # shift the left pointer to mid + 1 (to search in the right half)
            if letters[mid] <= target:
                left = mid + 1
            # Otherwise, shift the right pointer to mid - 1 (to search in the left half)
            else:
                right = mid - 1

        # After the loop, left will be the index of the smallest character greater than the target
        # If left is out of bounds, it means all characters in the array are less than or equal to the target
        # In such a case, we return the first element (circular array concept)
        return letters[left % len(letters)]

# Test cases
sol = Solution()
print(sol.nextGreatestLetter(["c", "f", "j"], "a"))  # Output: "c"
print(sol.nextGreatestLetter(["c", "f", "j"], "c"))  # Output: "f"
print(sol.nextGreatestLetter(["x", "x", "y", "y"], "z"))  # Output: "x"


# Description:
'''
To solve this problem, we can use a binary search approach to find the smallest character in 
the array letters that is lexicographically greater than the target. Since the array is sorted,
binary search is an efficient way to perform this search.

Here's the plan for our solution:

1. Initialize Pointers: 
   We'll start with two pointers, left and right, where left points to the start of the array and 
   right points to the end.

2. Binary Search: While left is less than or equal to right, we find the middle index and compare 
   the character at this index with the target. If the character at the middle index is less than or 
   equal to the target, we move the left pointer to mid + 1. Otherwise, we move the right pointer 
   to mid - 1.

3. Finding the Next Greatest Letter: After the loop, if left is within the bounds of the array, the 
   character at left will be the smallest character greater than the target. If left is out of bounds 
   (meaning all characters in the array are less than or equal to the target), we return the first 
   character in the array, as the array is circular.

This code implements a binary search algorithm to efficiently find the smallest character in the sorted 
array letters that is lexicographically greater than the target. The % len(letters) operation at the end 
is a neat trick to handle the case where left exceeds the array bounds, effectively rotating back to the 
start of the array. This handles the scenario where no character in letters is greater than the target, 
fulfilling the circular array condition stated in the problem.

'''
