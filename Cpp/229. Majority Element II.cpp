// 229. Majority Element II.


// Topic: Array, Hash Table, Sorting, Counting.


/*
### Task:
---
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Example 1:
Input: nums = [3,2,3]
Output: [3]

Example 2:
Input: nums = [1]
Output: [1]

Example 3:
Input: nums = [1,2]
Output: [1,2]

Constraints:
1 <= nums.length <= 5 * 10^4
-10^9 <= nums[i] <= 10^9

Follow up: Could you solve the problem in linear time and in O(1) space?

Hint 1:
Think about the possible number of elements that can appear more than ⌊ n/3 ⌋ times in the array.
Hint 2:
It can be at most two. Why?
Hint 3:
Consider using Boyer-Moore Voting Algorithm, which is efficient for finding elements that appear more than a certain threshold.

### Testcase:
---
[3,2,3]
[1]
[1,2]


### Code:
---
class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
        
    }
};


*/
// Solution: --------------------------------------

class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
        // Initialize two potential candidates for majority element and their counts
        int count1 = 0, count2 = 0, candidate1 = 0, candidate2 = 1; 

        // First Pass: Identify potential majority candidates
        for (int num : nums) {
            // If the current element is the same as candidate1, increment count1
            if (num == candidate1) {
                count1++;
            }
            // Else if the current element is the same as candidate2, increment count2
            else if (num == candidate2) {
                count2++;
            }
            // If count1 is 0, nominate current element as candidate1
            else if (count1 == 0) {
                candidate1 = num;
                count1 = 1;
            }
            // If count2 is 0, nominate current element as candidate2
            else if (count2 == 0) {
                candidate2 = num;
                count2 = 1;
            }
            // If current element is different from both candidates, decrement both counts
            else {
                count1--;
                count2--;
            }
        }

        // Reset counts for validation
        count1 = count2 = 0;
        
        // Second Pass: Validate the candidates by counting their actual occurrences
        for (int num : nums) {
            if (num == candidate1) count1++;
            else if (num == candidate2) count2++;
        }

        // Prepare the result vector
        vector<int> result;
        int n = nums.size();
        
        // If candidate1's count is more than n/3, add it to the result vector
        if (count1 > n / 3) result.push_back(candidate1);
        
        // If candidate2's count is more than n/3, add it to the result vector
        if (count2 > n / 3) result.push_back(candidate2);
        
        return result; // Return the final result vector
    }
};



// Description: ===================================
/*
To find all elements in the array `nums` that appear more than ⌊ n/3 ⌋ times, we can use the Boyer-Moore Voting Algorithm with a 
modification to handle the possibility of up to two majority elements (since no more than two elements can appear more than ⌊ n/3 ⌋ 
times in the array).

### Modified Boyer-Moore Voting Algorithm:

1. **Initialization**: Start with two candidate elements (candidate1 and candidate2) and their counts (count1 and count2).

2. **First Pass (Voting Phase)**: Iterate through the array, updating the candidates and counts according to the following rules:
   - If the current element is equal to one of the candidates, increment its count.
   - Else if one of the counts is 0, replace the candidate with the current element and set the count to 1.
   - Otherwise, decrement both counts.

3. **Second Pass (Validation Phase)**: Reset both counts to 0 and iterate through the array again to confirm that the candidates 
     appear more than ⌊ n/3 ⌋ times.

4. **Result Compilation**: Add the candidates that meet the criteria to the result vector.

### Description:

This algorithm leverages the insight that there can be at most two elements in the array that appear more than ⌊ n/3 ⌋ times. 
The first pass (Voting Phase) identifies two candidates that could potentially be the majority elements. The second pass 
(Validation Phase) verifies whether these candidates actually appear more than ⌊ n/3 ⌋ times. This approach is efficient, with O(n) 
time complexity and O(1) space complexity, thus meeting the challenge of solving the problem in linear time and constant space.

*/
