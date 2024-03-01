// 2864. Maximum Odd Binary Number.


// Topic: Mathm, String, Greedy.


/*
### Task:
---

Topics
Companies
Hint
You are given a binary string s that contains at least one '1'.

You have to rearrange the bits in such a way that the resulting binary number is the maximum odd binary number that can be created from this combination.

Return a string representing the maximum odd binary number that can be created from the given combination.

Note that the resulting string can have leading zeros.

Example 1:
Input: s = "010"
Output: "001"
Explanation: Because there is just one '1', it must be in the last position. So the answer is "001".

Example 2:
Input: s = "0101"
Output: "1001"
Explanation: One of the '1's must be in the last position. The maximum number that can be made with the remaining digits is "100". So the answer is "1001".

Constraints:
1 <= s.length <= 100
s consists only of '0' and '1'.
s contains at least one '1'.

Hint 1:
The binary representation of an odd number contains '1' in the least significant place.

### Testcase:
---
"010"
"0101"


### Code:
---
class Solution {
public:
    string maximumOddBinaryNumber(string s) {
        
    }
};

*/
// Solution: --------------------------------------

class Solution {
public:
    string maximumOddBinaryNumber(string s) {
        // Count the number of '1's in the input string
        int onesCount = 0;
        for(char c : s) {
            if(c == '1') {
                onesCount++;
            }
        }

        // If there is only one '1', the result is '0's followed by a single '1'
        if(onesCount == 1) {
            return string(s.length() - 1, '0') + "1";
        }

        // Construct the maximum odd binary number
        string result;
        // Add '1's to the beginning, leaving one '1' for the end
        for(int i = 0; i < onesCount - 1; ++i) {
            result += "1";
        }
        // Fill the middle with '0's (total length - onesCount + 1, for the '1' at the end)
        result += string(s.length() - onesCount, '0');
        // Ensure the last digit is '1' to make it odd
        result += "1";

        return result;
    }
};



// Description: ===================================
/*
To solve the problem, we need to focus on the fact that an odd binary number must end with a '1'. Our goal is to maximize 
the value of the binary number while ensuring it remains odd. This can be achieved by placing the highest value bits (i.e., '1's) 
as far left as possible, except for one '1' that must be at the end to ensure the number is odd.

Here's a step-by-step strategy to construct the maximum odd binary number:
1. Count the number of '1's in the given binary string.
2. If there is only one '1', the maximum odd binary number would be to place this '1' at the end, filling the rest with '0's.
3. If there are more than one '1's, place all but one '1' at the beginning of the new binary string, followed by '0's (if any), 
   and ensure the last digit is '1'.

This solution first counts the number of '1's in the input string. If there's only one '1', the result is straightforward: 
all '0's followed by a '1'. For more than one '1', it constructs a new string with all '1's (except one) at the beginning, 
fills any gap with '0's, and places a '1' at the end to ensure the number is odd. This approach ensures the constructed 
binary number is the maximum odd binary number possible with the given '1's and '0's.

*/
