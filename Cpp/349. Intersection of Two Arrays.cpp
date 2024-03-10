// 349. Intersection of Two Arrays.

// Topic: Array, Hash Table, Two Pointers, Binary Search, Sorting.

/*
### Task:
---
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.

Constraints:
1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000


### Testcase:
---
[1,2,2,1]
[2,2]
[4,9,5]
[9,4,9,8,4]


### Code:
---
class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        
    }
};


*/
// Solution: --------------------------------------

#include <vector>
#include <unordered_set>
using namespace std;

class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        // Create a set from nums1 to remove duplicates and allow efficient look-up
        unordered_set<int> nums1Set(nums1.begin(), nums1.end());

        // Set to store the intersection elements, ensuring each element is unique
        unordered_set<int> resultSet;
        
        // Iterate over each element in nums2
        for (int num : nums2) {
            // Check if the current element is present in nums1Set (i.e., in both arrays)
            if (nums1Set.find(num) != nums1Set.end()) {
                // If so, add it to the resultSet to ensure only unique elements are added
                resultSet.insert(num);
            }
        }
        
        // Convert the resultSet (which contains unique intersection elements) to a vector
        vector<int> result(resultSet.begin(), resultSet.end());

        // Return the vector containing the intersection of nums1 and nums2
        return result;
    }
};




// Description: ===================================
/*
To solve the task of finding the intersection of two arrays, we can leverage the efficiency of a hash table to track the 
unique elements present in both arrays. The algorithm involves inserting all elements of the first array into a set to 
eliminate duplicates, then iterating through the second array to check for the presence of its elements in the set. If 
an element from the second array is found in the set, it is part of the intersection and is added to the result set (to 
ensure uniqueness). Finally, we convert the result set to a vector to adhere to the required return type. This approach 
offers a time complexity of O(n + m) where n and m are the lengths of the two arrays, assuming average-case constant time 
operations in the hash set.

### Description:
- `unordered_set<int> nums1Set(nums1.begin(), nums1.end());`: Initializes an unordered_set with elements from `nums1`, 
   automatically removing any duplicates.
- `unordered_set<int> resultSet;`: A set to keep track of the intersection elements, ensuring they are unique.
- The for loop iterates through `nums2`, and for each element, it checks if the element exists in `nums1Set`. If it does, 
  the element is added to `resultSet`.
- Finally, `resultSet` is converted to a vector and returned as the result.

This implementation provides a straightforward and efficient way to find the intersection of two arrays with unique elements, 
conforming to the given constraints.

*/
