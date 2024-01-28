// 3020. Find the Maximum Number of Elements in Subset.

// 

/*
#Task:
You are given an array of positive integers nums.
You need to select a subset  of nums which satisfies the following condition:

You can place the selected elements in a 0-indexed array such that it follows the pattern: [x, x^2, x^4, ..., x^k/2, x^k, x^k/2, ..., x^4, x^2, x] 
(Note that k can be be any non-negative power of 2). For example, [2, 4, 16, 4, 2] and [3, 9, 3] follow the pattern while [2, 4, 8, 4, 2] does not.

Return the maximum number of elements in a subset that satisfies these conditions.

Example 1:
Input: nums = [5,4,1,2,2]
Output: 3
Explanation: We can select the subset {4,2,2}, which can be placed in the array as [2,4,2] which follows the pattern and 22 == 4. Hence the answer is 3.

Example 2:
Input: nums = [1,3,2,4]
Output: 1
Explanation: We can select the subset {1}, which can be placed in the array as [1] which follows the pattern. Hence the answer is 1. Note that we could have also selected the subsets {2}, {4}, or {3}, there may be multiple subsets which provide the same answer. 

Constraints:
2 <= nums.length <= 10^5
1 <= nums[i] <= 10^9

Hint 1:
We can select an odd number of 1’s.
Hint 2:
Put all the values into a HashSet. We can start from each x > 1 as the smallest chosen value and we can find the longest subset by checking the new values (which are the square of the previous value) in the set by brute force.
Hint 3:
Note when x > 1, x2, x4, x8, … increases very fast, the longest subset with smallest value x cannot be very long. (The length is O(log(log(109))).
Hint 4:
Hence we can directly check all lengths less than 10 for all values of x.


# Testcase:
[5,4,1,2,2]
[1,3,2,4]


# Code:
class Solution {
public:
    int maximumLength(vector<int>& nums) {
        
    }
};

*/

// Solution:  ----------------------------------------------------------------------------------

#include <vector>
#include <unordered_map>
#include <cmath>
#include <algorithm>

class Solution {
public:
    int maximumLength(std::vector<int>& nums) {
        // Using a map to count the occurrences of each number
        std::unordered_map<long long, int> frequencyMap;
        for (int num : nums) {
            frequencyMap[num]++;
        }

        // If all elements are the same, the longest subset can only be 1
        if (frequencyMap.size() == 1) return 1;

        int maxLength = 1; // Initialize the maximum subset length
        int currentLength; // Variable to store the current subset length

        // Iterate through each unique number in the array
        for (auto& pair : frequencyMap) {
            long long base = std::sqrt(pair.first); // Find the square root of the current number
            currentLength = 1; // Reset the current subset length

            // Loop to find if there's a chain of square roots leading to another number in the set
            while (base >= 2) {
                if (frequencyMap.find(base) != frequencyMap.end()) {
                    // Only consider the chain if there are at least 2 occurrences of the base
                    if (frequencyMap[base] >= 2) {
                        currentLength += 2; // Increment the current subset length by 2
                    } else {
                        break; // Break the loop if the chain is broken
                    }
                    base = std::sqrt(base); // Update the base to its square root for the next iteration
                } else {
                    break; // Break the loop if the next base is not found
                }
            }

            maxLength = std::max(maxLength, currentLength); // Update the maximum subset length if necessary
        }

        // Special handling for the number 1
        int onesCount = frequencyMap.find(1) != frequencyMap.end() ? frequencyMap[1] : 0;
        if (onesCount > maxLength) {
            // If the count of 1's is odd, it's the maximum subset length
            // If it's even, subtract 1 to make it odd (since the pattern requires symmetry)
            return onesCount % 2 == 0 ? onesCount - 1 : onesCount;
        }

        return maxLength; // Return the maximum length of the subset found
    }
};


// Description:
/*
The provided solution addresses the problem of finding the maximum number of elements in a subset of a given array of positive integers, where the subset must follow a specific pattern. This pattern is such that the elements can be arranged as `[x, x^2, x^4, ..., x^k/2, x^k, x^k/2, ..., x^4, x^2, x]`, where `k` is a non-negative power of 2. The algorithm operates in several key steps:

1. **Frequency Map Creation**: The algorithm starts by iterating through the input array `nums` and populating an `unordered_map` named `frequencyMap`, where each key is a unique element from `nums`, and the corresponding value is the frequency of that element within the array.

2. **Initial Check for Uniform Array**: The algorithm checks if the size of the `frequencyMap` is 1, which would indicate that all elements in the input array are the same. In such a case, the maximum subset size can only be 1, and the function returns this value immediately.

3. **Initialization**: The variable `maxLength` is initialized to 1 to account for the minimum subset size, and `currentLength` is used to track the size of the current subset being evaluated.

4. **Iterating Through Unique Elements**: The algorithm iterates through each unique element in `frequencyMap`. For each element, it calculates its square roots iteratively, checking at each step if the square root exists in the `frequencyMap`. This process is akin to traversing backward through the desired pattern, starting from `x^k` down to `x`.

5. **Updating Subset Size**: If a square root of the current element is found in the map, and there are at least 2 occurrences of this square root (to account for its presence on both sides of the pattern), the `currentLength` is incremented by 2. This process continues until the square root is less than 2 or no longer found in the map.

6. **Maximum Length Update**: After evaluating each unique element, the algorithm updates `maxLength` if `currentLength` exceeds the current value of `maxLength`.

7. **Special Handling for Ones**: After iterating through all unique elements, the algorithm checks the count of `1`s in the array. If the count of `1`s is greater than `maxLength`, the algorithm returns the count of `1`s as the maximum subset length. If the count is even, it decrements it by 1 to maintain symmetry in the subset pattern.

8. **Returning Result**: Finally, the algorithm returns `maxLength`, which represents the maximum number of elements that can form a subset following the specified pattern.

This algorithm effectively utilizes the mathematical property of square roots to construct the desired subset pattern in reverse, ensuring that the selected subset adheres to the problem's constraints.

*/