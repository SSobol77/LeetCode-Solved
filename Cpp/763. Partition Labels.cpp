// 763. Partition Labels.


// Topic: Hash Table, Two Pointers, String, Greedy.


/*
### Task:
---
You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.
Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.
Return a list of integers representing the size of these parts.

Example 1:
Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.

Example 2:
Input: s = "eccbbbbdec"
Output: [10]
 
Constraints:
1 <= s.length <= 500
s consists of lowercase English letters.

Hint 1:
Try to greedily choose the smallest partition that includes the first letter. If you have something like "abaccbdeffed", 
then you might need to add b. You can use an map like "last['b'] = 5" to help you expand the width of your partition.


### Testcase:
---
"ababcbacadefegdehijhklij"
"eccbbbbdec"

### Code:
---
class Solution {
public:
    vector<int> partitionLabels(string s) {
        
    }
};


*/
// Solution: --------------------------------------

class Solution {
public:
    vector<int> partitionLabels(string s) {
        // Array to store the last occurrence of each character.
        // Since the string consists of lowercase English letters, we need an array of size 26.
        vector<int> last(26, 0);
        
        // First pass: Fill the 'last' array with the last occurrence of each character in the string.
        for (int i = 0; i < s.length(); ++i) {
            last[s[i] - 'a'] = i; // Subtract 'a' to convert char to an index (0-25).
        }

        vector<int> partitions; // This will store the sizes of the partitions.
        int start = 0; // Start index of the current partition.
        int end = 0; // End index of the current partition.

        // Second pass: Determine the partitions.
        for (int i = 0; i < s.length(); ++i) {
            // Update the end of the current partition to be the furthest last occurrence of the current character.
            end = max(end, last[s[i] - 'a']);

            // If the current index is the end of the partition,
            // it means all characters within this partition do not appear beyond this point.
            if (i == end) {
                // Add the size of the current partition to the result list.
                // The size is 'end - start + 1' because both start and end are inclusive.
                partitions.push_back(end - start + 1);

                // Move the start to the next character, marking the beginning of a new partition.
                start = i + 1;
            }
        }

        // Return the list of partition sizes.
        return partitions;
    }
};


// Description: ===================================
/*
To solve the "Partition Labels" problem, we can use a greedy approach along with a hash table (or an array since the input consists 
of lowercase English letters only) to keep track of the last occurrence of each character in the string. The idea is to iterate through 
the string, and for each character, we extend the current partition to include the last occurrence of that character. Once we reach 
the end of the current partition, we record its size and start a new partition.

Here's a step-by-step approach:

1. Create a hash table (or an array of size 26 for lowercase English letters) to store the last index of each character in the string.

2. Iterate through the string to fill this hash table with the last occurrence of each character.

3. Initialize two pointers, `start` and `end`, to keep track of the start and end of the current partition. Initially, both are set to 0.

4. Iterate through the string again. For each character at index `i`:
   - Update `end` to be the maximum of `end` and the last occurrence of the current character (from the hash table). This ensures the 
     current partition includes all occurrences of the current character.
   - If `i` equals `end`, it means we've reached the end of a partition where all characters included in the partition appear only 
     within this partition. Record the size of the partition (`end - start + 1`), add it to the result list, and update `start` to 
     `i + 1` to begin a new partition.

5. Return the list of partition sizes.

This solution iterates through the string twice, making the time complexity O(N), where N is the length of the string. 
The space complexity is O(1) since the size of the hash table (or array) is constant (26 for lowercase English letters).

*/
