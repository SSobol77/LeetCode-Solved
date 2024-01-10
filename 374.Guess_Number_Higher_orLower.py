"""
# 374. Guess Number Higher or Lower.

# Topic: Binary Search, Interactive.


# Task:
----------------
We are playing the Guess Game. The game is as follows:
I pick a number from 1 to n. You have to guess which number I picked.
Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API int guess(int num), which returns three possible results:

   -1: Your guess is higher than the number I picked (i.e. num > pick).
    1: Your guess is lower than the number I picked (i.e. num < pick).
    0: your guess is equal to the number I picked (i.e. num == pick).

Return the number that I picked.

Example 1:
Input: n = 10, pick = 6
Output: 6

Example 2:
Input: n = 1, pick = 1
Output: 1

Example 3:
Input: n = 2, pick = 1
Output: 1

Constraints:
1 <= n <= 2^31 - 1
1 <= pick <= n

# Testcase:
----------------
10
6
1
1
2
1



# Code:
------------------
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
  




"""

# Solution:
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        # Initialize the range of numbers to search
        low, high = 1, n
        
        # Use binary search to narrow down the number
        while low <= high:
            # Find the middle number in the current range
            mid = low + (high - low) // 2
            
            # Use the API to guide whether to search higher or lower
            res = guess(mid)
            if res == 0:
                # Found the number, return it
                return mid
            elif res == -1:
                # The guessed number is higher, search lower half
                high = mid - 1
            else:
                # The guessed number is lower, search upper half
                low = mid + 1
                
        # If the number is not found, this line should not be reached
        return -1


# Description:
'''
To solve the "Guess Number Higher or Lower" problem, we can use a binary search approach. 
The idea is to narrow down the range of numbers to guess based on whether the current guess 
is higher or lower than the picked number. This is a classic application of binary search 
where we use the provided API guess(num) to guide our search.

Explanation:

    Initialization of low and high: Sets up the range of numbers to search.
    While loop (binary search): Continues searching as long as low is less than or equal to high.
    Calculation of mid: Finds the middle number between low and high.
    guess(mid) API call: Uses the provided API to check if the guessed number is higher, lower, 
    or equal to the picked number.
        If res == 0, the correct number is found, and it's returned.
        If res == -1, the guessed number is higher, and the search range is updated to the lower half.
        If res == 1, the guessed number is lower, and the search range is updated to the upper half.

Complexity Analysis:

    Time Complexity: O(log n), as binary search cuts the search space in half each time.
    Space Complexity: O(1), as the solution uses a constant amount of space.

'''

