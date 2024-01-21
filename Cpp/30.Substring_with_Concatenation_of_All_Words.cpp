// 30. Substring with Concatenation of All Words

/*
### Task:
----------
You are given a string s and an array of strings words. All the strings of words are of the same length.

A concatenated substring in s is a substring that contains all the strings of any permutation of words concatenated.

 - For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are all 
   concatenated strings. "acdbef" is not a concatenated substring because it is not the concatenation of any permutation of words.

Return the starting indices of all the concatenated substrings in s. You can return the answer in any order.

#Example 1:
Input: s = "barfoothefoobarman", words = ["foo","bar"]
Output: [0,9]
Explanation: Since words.length == 2 and words[i].length == 3, the concatenated substring has to be of length 6.
The substring starting at 0 is "barfoo". It is the concatenation of ["bar","foo"] which is a permutation of words.
The substring starting at 9 is "foobar". It is the concatenation of ["foo","bar"] which is a permutation of words.
The output order does not matter. Returning [9,0] is fine too.

#Example 2:
Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
Output: []
Explanation: Since words.length == 4 and words[i].length == 4, the concatenated substring has to be of length 16.
There is no substring of length 16 in s that is equal to the concatenation of any permutation of words.
We return an empty array.

#Example 3:
Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
Output: [6,9,12]
Explanation: Since words.length == 3 and words[i].length == 3, the concatenated substring has to be of length 9.
The substring starting at 6 is "foobarthe". It is the concatenation of ["foo","bar","the"] which is a permutation of words.
The substring starting at 9 is "barthefoo". It is the concatenation of ["bar","the","foo"] which is a permutation of words.
The substring starting at 12 is "thefoobar". It is the concatenation of ["the","foo","bar"] which is a permutation of words.

#Constraints:

    1 <= s.length <= 10^4
    1 <= words.length <= 5000
    1 <= words[i].length <= 30
    s and words[i] consist of lowercase English letters.




### Code:
----------
class Solution {
public:
    vector<int> findSubstring(string s, vector<string>& words) {
        
    }
};
*/

// Solution
class Solution {
public:
    vector<int> findSubstring(string s, vector<string>& words) {
        vector<int> result;
        int wordLen = words[0].length();  // Length of each word in the words array
        int totalWords = words.size();    // Total number of words in the words array
        int concatLen = wordLen * totalWords;  // Length of the concatenated substring
        
        unordered_map<string, int> wordCounts;  // Hash map to store the counts of words
        
        // Count the occurrences of each word in the words array
        for (const string& word : words) {
            wordCounts[word]++;
        }
        
        // Iterate through all possible starting positions for each word in a single word's length cycle
        for (int i = 0; i < wordLen; i++) {
            int left = i;  // Left pointer of the sliding window
            int right = i; // Right pointer of the sliding window
            unordered_map<string, int> currentCounts; // Hash map to store counts of words in the current substring
            int count = 0; // Total count of words found in the current substring
            
            while (right + wordLen <= s.length()) {
                string word = s.substr(right, wordLen); // Get the current word from the substring
                right += wordLen; // Move the right pointer
                
                if (wordCounts.find(word) != wordCounts.end()) {
                    currentCounts[word]++; // Increment the count of the current word
                    count++; // Increment the total count of words
                    
                    // Check if there are excess occurrences of the current word
                    while (currentCounts[word] > wordCounts[word]) {
                        string leftWord = s.substr(left, wordLen); // Get the word at the left end
                        left += wordLen; // Move the left pointer
                        currentCounts[leftWord]--; // Decrement its count
                        count--; // Decrement the total count of words
                    }
                    
                    // If the total count of words matches the total number of words in the words array
                    if (count == totalWords) {
                        result.push_back(left); // Add the starting index of the substring to the result
                    }
                } else {
                    currentCounts.clear(); // Reset the counts if a non-word is encountered
                    count = 0;
                    left = right; // Move both pointers to the right
                }
            }
        }
        
        return result;
    }
};



// Description:
/*
This code uses a sliding window approach to iterate through the string s, considering different starting positions 
for each word in words. It keeps track of the counts of words using hash maps and checks if the current substring 
of s forms a concatenated substring of any permutation of words. If so, it adds the starting index of the substring 
to the result vector.

The time complexity of this solution is O(N * M), where N is the length of the string s, and M is the length of a 
single word in words.

*/
