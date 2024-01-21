"""
# 278. First Bad Version

# Topic: Binary Search, Interactive.


# Task:
--------------
You are a product manager and currently leading a team to develop a new product. Unfortunately, the 
latest version of your product fails the quality check. Since each version is developed based on the 
previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes 
all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a 
function to find the first bad version. You should minimize the number of calls to the API.
 

Example 1:
Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.

Example 2:
Input: n = 1, bad = 1
Output: 1
 
Constraints:
1 <= bad <= n <= 2^31 - 1


# Testcase:
---------------
5
4
1
1


# Code:
---------------
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        

"""

# Solution:
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # Initialize the search range
        left, right = 1, n

        # Use binary search to find the first bad version
        while left < right:
            mid = left + (right - left) // 2

            if isBadVersion(mid):
                # If the current version is bad, the first bad version is at mid or before
                right = mid
            else:
                # If the current version is not bad, the first bad version is after mid
                left = mid + 1

        # Left will be the first bad version
        return left

# Description:
'''
To solve the "First Bad Version" problem, we will apply a binary search algorithm. The goal 
is to minimize the number of API calls to isBadVersion(version). By using binary search, we 
can efficiently narrow down the range of versions to check.

Explanation:

    Initialization of left and right: Sets up the range of versions to check, starting from 1 to n.
    While loop (binary search): Continues searching as long as left is less than right.
    Calculation of mid: Finds the middle version between left and right.
    isBadVersion(mid) API call: Uses the API to check if the version mid is bad.
        If mid is a bad version, the first bad version must be at mid or earlier, so we set right to mid.
        If mid is not a bad version, the first bad version must be after mid, so we set left to mid + 1.
    Return statement: Once the loop exits, left points to the first bad version.

Complexity Analysis:

    Time Complexity: O(log n), as the binary search halves the search space in each iteration.
    Space Complexity: O(1), since a constant amount of space is used.

This approach efficiently finds the first bad version while minimizing the number of API calls.

'''