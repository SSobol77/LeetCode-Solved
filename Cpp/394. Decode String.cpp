// 394. Decode String.


// Topic: String, Stack, Recursion.

/*
### Task:
---
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. 
Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. 
Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. 
For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 10^5.

Example 1:
Input: s = "3[a]2[bc]"
Output: "aaabcbc"

Example 2:
Input: s = "3[a2[c]]"
Output: "accaccacc"

Example 3:
Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"

Constraints:
1 <= s.length <= 30
s consists of lowercase English letters, digits, and square brackets '[]'.
s is guaranteed to be a valid input.
All the integers in s are in the range [1, 300].

### Testcase:
---
"3[a]2[bc]"
"3[a2[c]]"
"2[abc]3[cd]ef"


### Code:
---
class Solution {
public:
    string decodeString(string s) {
        
    }
};

*/
// Solution: --------------------------------------

class Solution {
public:
    string decodeString(string s) {
        stack<string> chars;  // Stack to store characters and decoded strings
        stack<int> nums;      // Stack to store repeat numbers
        string result;
        int num = 0;

        for (char c : s) {
            if (isdigit(c)) {
                num = num * 10 + (c - '0');  // Parse the entire number
            } else if (isalpha(c)) {
                chars.push(string(1, c));  // Push the current character as a string
            } else if (c == '[') {
                nums.push(num);  // Push the number onto the nums stack
                num = 0;         // Reset num for the next number
                chars.push("["); // Use '[' as a marker
            } else if (c == ']') {
                string decoded = "";
                while (!chars.empty() && chars.top() != "[") {
                    decoded = chars.top() + decoded;  // Reverse the decoded string
                    chars.pop();
                }
                chars.pop();  // Pop the '[' marker

                int count = nums.top();  // Get the repeat count
                nums.pop();

                string temp;
                while (count--)  // Repeat the decoded string count times
                    temp += decoded;
                
                chars.push(temp);  // Push the repeated string back onto the chars stack
            }
        }

        // Pop everything from the chars stack, reverse it, and concatenate
        while (!chars.empty()) {
            result = chars.top() + result;
            chars.pop();
        }

        return result;
    }
};


// Description: ===================================
/*
To decode a string according to the given encoding rule `k[encoded_string]`, we can use a stack to keep track of the characters 
and numbers. Since the problem guarantees valid input, we don't need to worry about edge cases like unmatched brackets or invalid 
characters. We'll iterate through the string, and whenever we encounter a digit, we'll parse the entire number (since numbers can 
be more than one digit). When we see an opening bracket, we know that an encoded string is starting, and when we encounter a closing 
bracket, we must pop the stack until the opening bracket to decode the current encoded string.

Here's a step-by-step guide to the algorithm:

1. Initialize an empty stack.
2. Iterate through each character of the input string.
3. If the current character is a digit, parse the entire number and push it onto the stack.
4. If the current character is a letter, push it onto the stack.
5. If the current character is an opening bracket `[`, just proceed to the next character as it signifies the start of an encoded string.
6. If the current character is a closing bracket `]`, start popping from the stack and keep track of the characters until you hit a digit. 
   These characters form the encoded string that needs to be repeated.
7. Once you reach a digit, repeat the popped encoded string that many times and push it back onto the stack as a single string.
8. After the iteration is complete, the stack will contain parts of the decoded string in reverse order. Pop everything from the stack, 
   reverse it, and concatenate to form the decoded string.



### Description:

This code defines a `decodeString` method that takes an encoded string `s` as input and returns its decoded string. It uses two stacks: 
`chars` for characters and decoded strings, and `nums` for repeat numbers. The method iterates through each character of the input string, 
handling digits, letters, opening brackets `[`, and closing brackets `]` according to the described algorithm. Once the iteration is 
complete, it constructs the decoded string from the stack contents, ensuring the decoded string's correct order. This approach efficiently 
decodes the string by leveraging stacks to manage the nested encoded strings and their repeat counts.

*/
