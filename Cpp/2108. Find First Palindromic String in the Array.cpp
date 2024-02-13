// 2108. Find First Palindromic String in the Array.


// Topic: Array, Two Pointers, String.


/*
### Task:
---
Given an array of strings words, return the first palindromic string in the array. 
If there is no such string, return an empty string "".

A string is palindromic if it reads the same forward and backward.

Example 1:
Input: words = ["abc","car","ada","racecar","cool"]
Output: "ada"
Explanation: The first string that is palindromic is "ada".
Note that "racecar" is also palindromic, but it is not the first.

Example 2:
Input: words = ["notapalindrome","racecar"]
Output: "racecar"
Explanation: The first and only string that is palindromic is "racecar".

Example 3:
Input: words = ["def","ghi"]
Output: ""
Explanation: There are no palindromic strings, so the empty string is returned.
 
Constraints:
1 <= words.length <= 100
1 <= words[i].length <= 100
words[i] consists only of lowercase English letters.

Hint 1:
Iterate through the elements in order. As soon as the current element is a palindrome, return it.
Hint 2:
To check if an element is a palindrome, can you reverse the string?


### Testcase:
---
["abc","car","ada","racecar","cool"]
["notapalindrome","racecar"]
["def","ghi"]


### Code:
---
class Solution {
public:
    string firstPalindrome(vector<string>& words) {
        
    }
};


*/
// Solution: --------------------------------------

#include <vector>
#include <string>
using namespace std;

class Solution {
public:
    string firstPalindrome(vector<string>& words) {
        // Iterate through each word in the array
        for (const string& word : words) {
            if (isPalindrome(word)) {
                // If the word is a palindrome, return it
                return word;
            }
        }
        // If no palindromic string is found, return an empty string
        return "";
    }

private:
    // Helper function to check if a string is a palindrome
    bool isPalindrome(const string& s) {
        int left = 0; // Start pointer
        int right = s.length() - 1; // End pointer

        // Check characters from both ends moving towards the center
        while (left < right) {
            if (s[left] != s[right]) {
                // If characters at the pointers do not match, it's not a palindrome
                return false;
            }
            left++;  // Move the start pointer towards the center
            right--; // Move the end pointer towards the center
        }

        // If all characters match, it's a palindrome
        return true;
    }
};

// Description: ===================================
/*
To solve the problem described, we need to iterate through each string in the given array and check if it is a palindrome.
A palindrome is a string that reads the same forward and backward. We can achieve this by comparing characters from the 
beginning and the end of the string, moving towards the center. If we find a palindromic string, we return it immediately. 
If we iterate through the entire array without finding a palindrome, we return an empty string.

### Description:

- The `firstPalindrome` function iterates through each word in the given `words` array.
- For each word, it calls the `isPalindrome` helper function to check if the word is a palindrome.
- The `isPalindrome` function uses two pointers, `left` and `right`, to compare characters from both ends of the string. 
  If at any point the characters at these pointers do not match, the function returns `false`, indicating that the string is 
  not a palindrome. If all characters match, the function returns `true`.
- If a palindromic string is found, `firstPalindrome` returns it immediately. If no palindromic string is found after checking 
  all words, it returns an empty string.

*/
