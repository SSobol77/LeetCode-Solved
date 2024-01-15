# 1704. Determine if String Halves Are Alike

# Topic: String, Counting.

"""
### Task:
---
You are given a string s of even length. Split this string into two halves of equal lengths, and let a be the first half and b be the second half.

Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). Notice that s contains uppercase and lowercase letters.

Return true if a and b are alike. Otherwise, return false.

#Example 1:
Input: s = "book"
Output: true
Explanation: a = "bo" and b = "ok". a has 1 vowel and b has 1 vowel. Therefore, they are alike.

#Example 2:
Input: s = "textbook"
Output: false
Explanation: a = "text" and b = "book". a has 1 vowel whereas b has 2. Therefore, they are not alike.
Notice that the vowel o is counted twice.

#Constraints:
2 <= s.length <= 1000
s.length is even.
s consists of uppercase and lowercase letters.

#Hint 1:
Create a function that checks if a character is a vowel, either uppercase or lowercase.

### Code:
---
class Solution:
    def halvesAreAlike(self, s: str) -> bool:

"""
### Solution:

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        # Helper function to check if a character is a vowel
        def is_vowel(char: str) -> bool:
            return char in "aeiouAEIOU"
        
        # Split the string into two equal halves
        half_length = len(s) // 2
        a, b = s[:half_length], s[half_length:]
        
        # Initialize count variables
        count_a = count_b = 0
        
        # Count vowels in the first half (a)
        for char in a:
            if is_vowel(char):
                count_a += 1
        
        # Count vowels in the second half (b)
        for char in b:
            if is_vowel(char):
                count_b += 1
        
        # Compare vowel counts in both halves
        return count_a == count_b


### Description:
'''
To solve this problem, you can follow these steps within the `halvesAreAlike` method:

1. Create a function to check if a character is a vowel, either uppercase or lowercase.
2. Split the input string `s` into two equal halves: `a` and `b`.
3. Initialize two variables `count_a` and `count_b` to keep track of the number of vowels in `a` and `b`, respectively.
4. Loop through each character in `a` and `b`, and for each character, check if it is a vowel using the previously 
   defined function. Increment the respective count variables if the character is a vowel.
5. After looping through both halves, compare `count_a` and `count_b`. If they are equal, return `True`, indicating 
   that the two halves are alike in terms of vowel counts. Otherwise, return `False`.


This code splits the input string into two halves and counts the vowels in each half, then compares the counts 
to determine if they are alike.

'''
