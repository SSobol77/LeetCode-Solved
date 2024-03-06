// 41. First Missing Positive.      - HARD -

// Topic: Array, Hash Table.

/*
### Task:
---
Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.

You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

Example 1:
Input: nums = [1,2,0]
Output: 3
Explanation: The numbers in the range [1,2] are all in the array.

Example 2:
Input: nums = [3,4,-1,1]
Output: 2
Explanation: 1 is in the array but 2 is missing.

Example 3:
Input: nums = [7,8,9,11,12]
Output: 1
Explanation: The smallest positive integer 1 is missing.

Constraints:
1 <= nums.length <= 10^5
-2^31 <= nums[i] <= 2^31 - 1

Hint 1:
Think about how you would solve the problem in non-constant space. Can you apply that logic to the existing space?
Hint 2:
We don't care about duplicates or non-positive integers
Hint 3:
Remember that O(2n) = O(n)


### Testcase:
---
[1,2,0]
[3,4,-1,1]
[7,8,9,11,12]


### Code:
---
class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        
    }
};


*/
// Solution: --------------------------------------

#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        int n = nums.size();  // Store the size of the array for convenience.

        // Step 1: Modify the array by setting all non-positive and out-of-range numbers to n+1.
        // This ensures that all irrelevant numbers are set to a common value beyond the range of interest.
        for (int& num : nums) {
            if (num <= 0 || num > n) num = n + 1;
        }

        // Step 2: Use the array itself to mark the presence of numbers.
        // Iterate through the array, and for each positive integer x within the range [1, n],
        // mark the presence of x by flipping the sign of the element at index x-1 to negative.
        for (int i = 0; i < n; ++i) {
            int num = abs(nums[i]);  // Get the absolute value in case it's already been marked negative.
            if (num <= n) {
                // Mark as seen by making the element at index num-1 negative.
                // Use abs() to handle cases where the element is already negative.
                nums[num - 1] = -abs(nums[num - 1]);
            }
        }

        // Step 3: Scan the array for the first missing positive number.
        // The first positive element's index + 1 gives us the smallest missing positive integer.
        for (int i = 0; i < n; ++i) {
            if (nums[i] > 0) {
                return i + 1;  // Return the index + 1 as the missing positive number.
            }
        }

        // If all positions in the array are marked (i.e., all positive integers up to n are present),
        // then the missing positive integer is n+1.
        return n + 1;
    }
};




// Description: ===================================
/*
The "First Missing Positive" problem requires finding the smallest positive integer that does not appear in an array. The challenge lies in doing this efficiently, with an O(n) time complexity and O(1) space complexity. This problem can be approached by leveraging the array itself to record the presence of positive integers, effectively using it as a hash table.

The key insight is that the first missing positive integer must be within the range `[1, n+1]`, where `n` is the size of the array. This is because, in the worst-case scenario, the array contains all the first `n` positive integers, and the answer would be `n+1`.

Here is a step-by-step guide to solve this problem:

1. **Partition the array**: Segregate positive integers from non-positive integers, keeping all positive numbers at the beginning of the array. This step is not necessary but makes the next steps more straightforward.
2. **Mark the presence of integers**: Iterate through the array, and for each positive integer `x` within the range `[1, n]`, mark the presence of `x` by flipping the sign of the element at index `x-1` to negative. The sign flip is a way to record that the number `x` exists in the array without using additional space.
3. **Scan for the first missing positive**: Iterate through the modified array, and the index of the first positive number (if any) indicates the smallest missing positive integer. If all numbers are negative, the first missing positive is `n+1`.

### Description:

This solution utilizes the input array itself to keep track of which positive integers are present, effectively using it as a makeshift hash table. By marking the presence of an integer `x` by making the element at index `x-1` negative, we avoid using additional space. The first pass through the array is to adjust all non-positive and out-of-range values to a common value (`n+1`), which simplifies the marking process. The second pass marks the presence of numbers, and the final pass finds the smallest positive integer that hasn't been marked (i.e., its corresponding position is still positive). This solution meets the problem's requirements by running in O(n) time and using O(1) auxiliary space.

*/
