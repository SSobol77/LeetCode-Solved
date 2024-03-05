// 1750. Minimum Length of String After Deleting Similar Ends.

// Topic: Two Pointers, String.

/*
### Task:
---
Given a string s consisting only of characters 'a', 'b', and 'c'. You are asked to apply the following algorithm on the string any number of times:

1. Pick a non-empty prefix from the string s where all the characters in the prefix are equal.
2. Pick a non-empty suffix from the string s where all the characters in this suffix are equal.
3. The prefix and the suffix should not intersect at any index.
4. The characters from the prefix and suffix must be the same.
5. Delete both the prefix and the suffix.

Return the minimum length of s after performing the above operation any number of times (possibly zero times).

Example 1:
Input: s = "ca"
Output: 2
Explanation: You can't remove any characters, so the string stays as is.

Example 2:
Input: s = "cabaabac"
Output: 0
Explanation: An optimal sequence of operations is:
- Take prefix = "c" and suffix = "c" and remove them, s = "abaaba".
- Take prefix = "a" and suffix = "a" and remove them, s = "baab".
- Take prefix = "b" and suffix = "b" and remove them, s = "aa".
- Take prefix = "a" and suffix = "a" and remove them, s = "".

Example 3:
Input: s = "aabccabba"
Output: 3
Explanation: An optimal sequence of operations is:
- Take prefix = "aa" and suffix = "a" and remove them, s = "bccabb".
- Take prefix = "b" and suffix = "bb" and remove them, s = "cca".
 
Constraints:
1 <= s.length <= 10^5
s only consists of characters 'a', 'b', and 'c'.

Hint 1:
If both ends have distinct characters, no more operations can be made. Otherwise, the only operation is to remove all of the same characters from both ends. We will do this as many times as we can.
Hint 2:
Note that if the length is equal 1 the answer is 1


### Testcase:
---
"ca"
"cabaabac"
"aabccabba"


### Code:
---
class Solution {
public:
    int minimumLength(string s) {
        
    }
};


*/
// Solution: --------------------------------------

class Solution {
public:
    int minimumLength(string s) {
        // Initialize two pointers, one at the start and one at the end of the string
        int left = 0, right = s.length() - 1;

        // Loop until the two pointers meet or cross
        while (left < right && s[left] == s[right]) {
            // Store the current character at the left pointer to identify the sequence
            char currentChar = s[left];
            
            // Move the left and right pointers past the sequences of the current character
            // This loop continues as long as we haven't processed the entire string and
            // either pointer is pointing at the current character.
            while (left <= right && (s[left] == currentChar || s[right] == currentChar)) {
                // If the left pointer points at the current character, move it to the right
                if (s[left] == currentChar) left++;
                // If the right pointer points at the current character, move it to the left
                if (s[right] == currentChar) right--;
            }
        }

        // Calculate the remaining length of the string after removals.
        // The 'max' function ensures that the result is not negative in cases where 'left' exceeds 'right'.
        return max(0, right - left + 1);
    }
};


// Description: ===================================
/*
The provided solution implements an algorithm to reduce the length of a given string by repeatedly removing matching sequences of 
characters from its ends. Here's a detailed description of how the algorithm works:

1. **Initialization**: Two pointers, `left` and `right`, are initialized at the start and end of the string, respectively. These 
pointers are used to scan the string from both ends towards the center.

2. **Main Loop**: The algorithm enters a loop that continues as long as `left` is less than `right` and the characters at these 
pointers are the same. This condition ensures that the algorithm only attempts to remove characters when there are matching sequences 
at both ends of the string.

3. **Character Sequence Removal**: Within the loop, the algorithm identifies the current character (the character at the `left` 
pointer) and then moves both `left` and `right` pointers past any contiguous sequence of this character. This is done by incrementing 
the `left` pointer until it points to a different character or exceeds the `right` pointer, and by decrementing the `right` pointer 
until it points to a different character or falls below the `left` pointer. This step effectively removes the matching sequences from 
both ends of the string.

4. **Length Calculation**: Once the loop ends (either because the pointers have crossed or because the characters at the pointers are 
no longer the same), the algorithm calculates the length of the remaining string. If the pointers have crossed, it means that the entire 
string has been removed, resulting in a length of 0. Otherwise, the length is calculated as the difference between the `right` and `left` 
pointers, plus one (to account for zero-based indexing).

5. **Result**: The algorithm returns the calculated length of the string after all possible removals have been performed. This length 
represents the minimum length of the string after applying the described operation any number of times.

This algorithm is efficient, with a time complexity of \(O(n)\), where \(n\) is the length of the input string, because it involves a 
single pass through the string. The space complexity is \(O(1)\), as the algorithm uses a constant amount of extra space regardless of
the input size.

*/
