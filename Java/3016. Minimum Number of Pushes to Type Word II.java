// 3016. Minimum Number of Pushes to Type Word II.


/*
### Task:
---
You are given a string word containing lowercase English letters.

Telephone keypads have keys mapped with distinct collections of lowercase English letters, which can be used to form words by pushing them. For example, the key 2 is mapped with ["a","b","c"], we need to push the key one time to type "a", two times to type "b", and three times to type "c" .

It is allowed to remap the keys numbered 2 to 9 to distinct collections of letters. The keys can be remapped to any amount of letters, but each letter must be mapped to exactly one key. You need to find the minimum number of times the keys will be pushed to type the string word.

Return the minimum number of pushes needed to type word after remapping the keys.

An example mapping of letters to keys on a telephone keypad is given below. Note that 1, *, #, and 0 do not map to any letters.

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
Input: word = "xyzxyzxyzxyz"
Output: 12
Explanation: The remapped keypad given in the image provides the minimum cost.
"x" -> one push on key 2
"y" -> one push on key 3
"z" -> one push on key 4
Total cost is 1 * 4 + 1 * 4 + 1 * 4 = 12
It can be shown that no other mapping can provide a lower cost.
Note that the key 9 is not mapped to any letter: it is not necessary to map letters to every key, but to map all the letters.

Example 3:
Input: word = "aabbccddeeffgghhiiiiii"
Output: 24
Explanation: The remapped keypad given in the image provides the minimum cost.
"a" -> one push on key 2
"b" -> one push on key 3
"c" -> one push on key 4
"d" -> one push on key 5
"e" -> one push on key 6
"f" -> one push on key 7
"g" -> one push on key 8
"h" -> two pushes on key 9
"i" -> one push on key 9
Total cost is 1 * 2 + 1 * 2 + 1 * 2 + 1 * 2 + 1 * 2 + 1 * 2 + 1 * 2 + 2 * 2 + 6 * 1 = 24.
It can be shown that no other mapping can provide a lower cost.

Constraints:
1 <= word.length <= 10^5
word consists of lowercase English letters.


### Testcase:
---
"abcde"
"xyzxyzxyzxyz"
"aabbccddeeffgghhiiiiii"

### Code:
---
class Solution {
    public int minimumPushes(String word) {

    }
}

*/
// Solution: -------------------------------------------

import java.util.*;

class Solution {
    public int minimumPushes(String word) {
        // Map to store the frequency of each letter
        Map<Character, Integer> freqMap = new HashMap<>();

        // Count the frequency of each letter in the word
        for (char c : word.toCharArray()) {
            freqMap.put(c, freqMap.getOrDefault(c, 0) + 1);
        }

        // Create a list from the map and sort it by frequency in descending order
        List<Map.Entry<Character, Integer>> list = new ArrayList<>(freqMap.entrySet());
        list.sort((a, b) -> b.getValue().compareTo(a.getValue()));

        // Initialize total pushes
        int totalPushes = 0;
        int keys = 8;  // Total keys available (2 to 9)

        // Assign letters to keys and calculate pushes
        for (int i = 0; i < list.size(); i++) {
            // Determine the position of the letter on its key
            int pushes = (i / keys) + 1;
            // Add the total number of pushes for this letter
            totalPushes += list.get(i).getValue() * pushes;
        }

        return totalPushes;
    }

    // Test cases
    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.minimumPushes("abcde"));              // Output: 5
        System.out.println(sol.minimumPushes("xyzxyzxyzxyz"));       // Output: 12
        System.out.println(sol.minimumPushes("aabbccddeeffgghhiiiiii"));  // Output: 24
    }
}


// Description: ========================================
/*
The strategy employed in this Java solution for the "Minimum Number of Pushes to Type Word II" problem can be described as follows:

1. **Frequency Counting**: First, count the frequency of each letter in the word. This is important because letters that appear more frequently should be placed on keys that require fewer pushes.

2. **Sorting by Frequency**: Sort the letters in descending order of frequency. The goal is to assign the most frequent letters to keys that will require the least number of pushes.

3. **Optimal Key Assignment**: Assign letters to keys in a way that minimizes the total number of key pushes. This is done by placing the most frequent letters in the first position of the keys, then the next set of frequent letters in the second position, and so on.

4. **Calculating Total Pushes**: The total number of key pushes is calculated by iterating through the sorted list of letters and determining the number of pushes needed for each letter based on its position.

5. **Consideration for Available Keys**: There are 8 keys available (keys numbered 2 to 9), and each key can be mapped to multiple letters. The position of the letter on a key determines the number of pushes required to type it.

In this code:
- A `HashMap` is used to count the frequency of each letter in the word.
- The map is converted into a list of entries, which is then sorted by frequency in descending order.
- The list is iterated over, and the number of pushes for each letter is calculated based on its position in the sorted list and the total number of available keys.
- The `main` method demonstrates the functionality of the `minimumPushes` method with test cases.

*/
