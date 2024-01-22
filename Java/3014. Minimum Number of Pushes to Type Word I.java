// 3014. Minimum Number of Pushes to Type Word I.

/*
### Task:

You are given a string word containing distinct lowercase English letters.

Telephone keypads have keys mapped with distinct collections of lowercase English letters, which can
be used to form words by pushing them. For example, the key 2 is mapped with ["a","b","c"], we need
to push the key one time to type "a", two times to type "b", and three times to type "c" .

It is allowed to remap the keys numbered 2 to 9 to distinct collections of letters. The keys can be
remapped to any amount of letters, but each letter must be mapped to exactly one key. You need to find
the minimum number of times the keys will be pushed to type the string word.

Return the minimum number of pushes needed to type word after remapping the keys.

An example mapping of letters to keys on a telephone keypad is given below. Note that 1, *, #, and 0 do
not map to any letters.


Example 1:

Input: word = "abcde"
Output: 5
Explanation: The remapped keypad given in the image provides the minimum cost.
"a" -> one push on key 2
"b" -> one push on key 3
"c" -> one push on key 4
"d" -> one push on key 5
"e" -> one push on key 6
Total cost is 1 + 1 + 1 + 1 + 1 = 5.
It can be shown that no other mapping can provide a lower cost.

Example 2:

Input: word = "xycdefghij"
Output: 12
Explanation: The remapped keypad given in the image provides the minimum cost.
"x" -> one push on key 2
"y" -> two pushes on key 2
"c" -> one push on key 3
"d" -> two pushes on key 3
"e" -> one push on key 4
"f" -> one push on key 5
"g" -> one push on key 6
"h" -> one push on key 7
"i" -> one push on key 8
"j" -> one push on key 9
Total cost is 1 + 2 + 1 + 2 + 1 + 1 + 1 + 1 + 1 + 1 = 12.
It can be shown that no other mapping can provide a lower cost.

Constraints:
1 <= word.length <= 26
word consists of lowercase English letters.
All letters in word are distinct.

Hint 1:
We have 8 keys in total. We can type 8 characters with one push each, 8 different characters with two
pushes each, and so on.
Hint 2:
The optimal way is to map letters to keys evenly.

### Testcase:
---
"abcde"
"xycdefghij"

### Code:
---
class Solution {
    public int minimumPushes(String word) {

    }
}
*/

// Solution:

public class Solution {
    public int minimumPushes(String word) {
        int length = word.length();
        int pushes = 0;

        // Distribute characters across keys
        for (int i = 0; i < length; i++) {
            // Find the number of keys needed to reach the current character
            int keysNeeded = (i / 8) + 1;
            // Add to the total number of pushes
            pushes += keysNeeded;
        }

        return pushes;
    }

    // Test cases
    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.minimumPushes("abcde"));      // Should output 5
        System.out.println(sol.minimumPushes("xycdefghij")); // Should output 12
    }
}


// Description:
/*
To develop a strategy for solving this problem in Java, we will follow these steps:

1. **Understand the Problem**: We need to remap a telephone keypad's keys (2 to 9) with distinct lowercase English letters
     to minimize the number of key presses required to type a given word. Each letter in the word is distinct and must be
     mapped to exactly one key.

2. **Calculate Key Distribution**: Since we have 8 keys and each key can be mapped to a different number of letters, our
     goal is to distribute the letters of the word as evenly as possible across these keys. This distribution will minimize
     the total number of key presses. For example, if there are 16 letters, we would ideally map 2 letters to each key.

3. **Implement the Logic in Java**:
   - Create a Java class `Solution` with a method `minimumPushes(String word)`.
   - In this method, calculate the length of the word.
   - Initialize a variable to keep track of the total number of pushes.
   - Iterate through each character of the word.
     - For each character, calculate the number of key presses required. This can be done by dividing the character's
       position in the word by 8 (the number of keys) and adding 1, since array indices start at 0 but we need at least
       one push for each letter.
   - Sum these values to get the total number of pushes.
   - Return the total number of pushes.

4. **Code Efficiency**:
   - Ensure that the loop iterates only once through the word.
   - Avoid using any unnecessary data structures or complex operations, as the problem can be solved with simple arithmetic.

5. **Testing**:
   - Test the method with the provided examples to ensure accuracy.
   - Consider edge cases, such as a word with a length of 1 or 26 (the minimum and maximum possible lengths).

By following this strategy, the Java implementation should efficiently solve the problem while maintaining readability
and performance.

In this implementation, we first calculate the length of the word. Then, in a loop, we iterate over each character of
the word. The number of key presses required for each character is calculated based on its position in the sequence.
We sum these values to get the total number of pushes, which is then returned. The main method contains test cases to
demonstrate the functionality of the minimumPushes method.

*/
