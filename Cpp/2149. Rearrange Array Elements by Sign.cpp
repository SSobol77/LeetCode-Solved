// 2149. Rearrange Array Elements by Sign.


// Topic: Array, Two Pointers, Simulation.


/*
### Task:
---
You are given a 0-indexed integer array nums of even length consisting of an equal number of positive and negative integers.

You should rearrange the elements of nums such that the modified array follows the given conditions:

Every consecutive pair of integers have opposite signs.
For all integers with the same sign, the order in which they were present in nums is preserved.
The rearranged array begins with a positive integer.
Return the modified array after rearranging the elements to satisfy the aforementioned conditions.

Example 1:
Input: nums = [3,1,-2,-5,2,-4]
Output: [3,-2,1,-5,2,-4]
Explanation:
The positive integers in nums are [3,1,2]. The negative integers are [-2,-5,-4].
The only possible way to rearrange them such that they satisfy all conditions is [3,-2,1,-5,2,-4].
Other ways such as [1,-2,2,-5,3,-4], [3,1,2,-2,-5,-4], [-2,3,-5,1,-4,2] are incorrect because they do not satisfy one or more conditions.  

Example 2:
Input: nums = [-1,1]
Output: [1,-1]
Explanation:
1 is the only positive integer and -1 the only negative integer in nums.
So nums is rearranged to [1,-1].

Constraints:
2 <= nums.length <= 2 * 10^5
nums.length is even
1 <= |nums[i]| <= 10^5
nums consists of equal number of positive and negative integers.
 
It is not required to do the modifications in-place.

Hint 1:
Divide the array into two parts- one comprising of only positive integers and the other of negative integers.
Hint 2:
Merge the two parts to get the resultant array.

### Testcase:
---
[3,1,-2,-5,2,-4]
[-1,1]


### Code:
---
class Solution {
public:
    vector<int> rearrangeArray(vector<int>& nums) {
        
    }
};


*/
// Solution: --------------------------------------

class Solution {
public:
    vector<int> rearrangeArray(vector<int>& nums) {
        // Vectors to hold separated positive and negative numbers
        vector<int> pos, neg;

        // Loop through the nums array to separate positive and negative numbers
        for (int num : nums) {
            if (num > 0) {
                // If the number is positive, add it to the pos vector
                pos.push_back(num);
            } else {
                // If the number is negative, add it to the neg vector
                neg.push_back(num);
            }
        }

        // Vector to hold the final rearranged array
        vector<int> result;

        // Loop through the separated positive and negative numbers
        for (int i = 0; i < pos.size(); ++i) { // Assuming pos and neg have equal lengths
            // Add one positive and one negative number in turn to the result vector
            result.push_back(pos[i]); // Add positive number
            result.push_back(neg[i]); // Add negative number immediately after
        }

        // Return the rearranged array that satisfies all conditions
        return result;
    }
};


// Description: ===================================
/*

This solution follows the hints provided. It first separates the positive and negative integers from the `nums` array 
into two different vectors, `pos` for positive integers and `neg` for negative integers. Then, it merges these two vectors 
into a `result` vector by alternating between positive and negative integers, ensuring that every consecutive pair of 
integers have opposite signs and preserving the original order of integers with the same sign. This approach satisfies all 
the given conditions for rearranging the array.

### Comments:

- The `pos` and `neg` vectors are used to separate positive and negative numbers from the input `nums` array.
- The loop through `nums` checks each number's sign and adds it to the appropriate vector (`pos` for positive, `neg` for negative).
- The `result` vector is used to store the final rearranged array.
- In the final loop, positive and negative numbers are added alternately to the `result` vector from the `pos` and `neg` vectors, 
  ensuring that every consecutive pair of integers have opposite signs and maintaining the original order of integers with the same sign.

*/