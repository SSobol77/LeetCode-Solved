# 455. Assign Cookies.

# Topics: Array, Two Pointers, Greedy, Sorting.

'''
# Task:
--------------
Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie.

Each child i has a greed factor g[i], which is the minimum size of a cookie that the child will be 
content with; and each cookie j has a size s[j]. If s[j] >= g[i], we can assign the cookie j to the 
child i, and the child i will be content. Your goal is to maximize the number of your content children
and output the maximum number.

Example 1:
Input: g = [1,2,3], s = [1,1]
Output: 1
Explanation: You have 3 children and 2 cookies. The greed factors of 3 children are 1, 2, 3. 
And even though you have 2 cookies, since their size is both 1, you could only make the child whose greed 
factor is 1 content.
You need to output 1.

Example 2:
Input: g = [1,2], s = [1,2,3]
Output: 2
Explanation: You have 2 children and 3 cookies. The greed factors of 2 children are 1, 2. 
You have 3 cookies and their sizes are big enough to gratify all of the children, 
You need to output 2.

Constraints:
1 <= g.length <= 3 * 10^4
0 <= s.length <= 3 * 10^4
1 <= g[i], s[j] <= 2^31 - 1

# Testcase:
-------------
[1,2,3]
[1,1]
[1,2]
[1,2,3]

# Code:
--------
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        
        
'''

# Solution:
from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()  # Sort the greed factors of children
        s.sort()  # Sort the sizes of cookies

        child_index, cookie_index = 0, 0
        content_children = 0

        while child_index < len(g) and cookie_index < len(s):
            if s[cookie_index] >= g[child_index]:
                # This cookie can satisfy the child
                content_children += 1
                child_index += 1  # Move to the next child
            cookie_index += 1  # Move to the next cookie

        return content_children

# Test cases
solution = Solution()

# Test case 1
print(solution.findContentChildren([1, 2, 3], [1, 1]))  # Output: 1

# Test case 2
print(solution.findContentChildren([1, 2], [1, 2, 3]))  # Output: 2


# Description:
'''
To solve the "Assign Cookies" problem, we need to match the children with the cookies based on their 
greed factor and the size of the cookies. The goal is to maximize the number of content children. 
We can achieve this by sorting both the children by their greed factor and the cookies by their size. 
Then, we iterate through the cookies and try to satisfy each child in increasing order of their greed 
factor. Here's a step-by-step approach:

1. Sort the array g (greed factors of children) and s (sizes of cookies).
2. Initialize two pointers, one for the children array (g) and one for the cookies array (s).
3. Iterate through the cookies. For each cookie, check if it can satisfy the current child (based on 
   the greed factor).
4. If a cookie satisfies a child, increment the count of content children and move to the next child.
5. Continue this process until all cookies are checked or all children are content.
6. Return the count of content children.

This code should work efficiently for the given constraints. The sorting of both arrays takes O(n log n)
time, and the while loop runs in O(n) time, where n is the length of the longer array. Thus, the overall 
time complexity is O(n log n).

'''
