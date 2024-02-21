// 201. Bitwise AND of Numbers Range.


// Topic: Bit Manipulation


/*
### Task:
---
Given two integers left and right that represent the range [left, right], return the bitwise AND of 
all numbers in this range, inclusive.

Example 1:
Input: left = 5, right = 7
Output: 4

Example 2:
Input: left = 0, right = 0
Output: 0

Example 3:
Input: left = 1, right = 2147483647
Output: 0

Constraints:
0 <= left <= right <= 2^31 - 1

### Testcase:
---
5
7
0
0
1
2147483647


### Code:
---
class Solution {
public:
    int rangeBitwiseAnd(int left, int right) {
        
    }
};

*/
// Solution: --------------------------------------

class Solution {
public:
    int rangeBitwiseAnd(int left, int right) {
        int shift = 0;
        // Find the common prefix
        while (left < right) {
            left >>= 1;
            right >>= 1;
            shift++;
        }
        // Left shift the common prefix
        return left << shift;
    }
};

// Description: ===================================
/*
To solve this problem efficiently, we need to find the common prefix of the binary representations of `left` and `right`. 
This common prefix represents the bits that are common in all the numbers within the given range. Once we find this common 
prefix, we can create the final result by left-shifting it to the right until `left` and `right` become equal.

This solution iteratively right-shifts both `left` and `right` until they are equal, keeping track of the number of shifts 
in the variable `shift`. Then, it left-shifts `left` by `shift` bits to create the final result.

This solution has a time complexity of O(log(N)), where N is the maximum possible value of `left` or `right`, and a space 
complexity of O(1).

*/
