// 208. Implement Trie (Prefix Tree).


// Topic: Hash Table, String, Design, Trie.


/*
### Task:
---
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

    - Trie() Initializes the trie object.
    - void insert(String word) Inserts the string word into the trie.
    - boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
    - boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
    
Example 1:
Input
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output
[null, null, true, false, true, null, true]
Explanation
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True
 
Constraints:
1 <= word.length, prefix.length <= 2000
word and prefix consist only of lowercase English letters.
At most 3 * 10^4 calls in total will be made to insert, search, and startsWith.

### Testcase:
---
["Trie","insert","search","search","startsWith","insert","search"]
[[],["apple"],["apple"],["app"],["app"],["app"],["app"]]


### Code:
---
class Trie {
public:
    Trie() {
        
    }
    
    void insert(string word) {
        
    }
    
    bool search(string word) {
        
    }
    
    bool startsWith(string prefix) {
        
    }
};

//**
// * Your Trie object will be instantiated and called as such:
// * Trie* obj = new Trie();
// * obj->insert(word);
// * bool param_2 = obj->search(word);
// * bool param_3 = obj->startsWith(prefix);
// *

*/


// Solution: -----------------------------------------------------------------------------------------------

#include <vector>
#include <string>
using namespace std;

// Define the TrieNode structure.
class TrieNode {
public:
    TrieNode* children[26]; // Array to store pointers to child nodes for each letter of the alphabet.
    bool isEndOfWord; // Boolean flag to indicate if the node represents the end of a word.

    TrieNode() {
        isEndOfWord = false; // Initially, no node is the end of a word.
        for (int i = 0; i < 26; ++i) {
            children[i] = nullptr; // Initialize all child pointers to nullptr.
        }
    }
};

class Trie {
private:
    TrieNode* root; // Root node of the Trie.

public:
    Trie() {
        root = new TrieNode(); // Initialize the Trie with a new root node.
    }

    // Function to insert a word into the Trie.
    void insert(string word) {
        TrieNode* node = root; // Start from the root node.
        for (char c : word) { // Iterate over each character in the word.
            int index = c - 'a'; // Calculate the index corresponding to the character.
            if (!node->children[index]) { // If the child node doesn't exist, create it.
                node->children[index] = new TrieNode();
            }
            node = node->children[index]; // Move to the child node.
        }
        node->isEndOfWord = true; // Mark the last node as the end of the word.
    }

    // Function to search for a word in the Trie.
    bool search(string word) {
        TrieNode* node = root; // Start from the root node.
        for (char c : word) { // Iterate over each character in the word.
            int index = c - 'a'; // Calculate the index corresponding to the character.
            if (!node->children[index]) { // If the child node doesn't exist, the word is not in the Trie.
                return false;
            }
            node = node->children[index]; // Move to the child node.
        }
        return node->isEndOfWord; // Return true if the last node is marked as the end of the word.
    }

    // Function to check if there is any word in the Trie that starts with the given prefix.
    bool startsWith(string prefix) {
        TrieNode* node = root; // Start from the root node.
        for (char c : prefix) { // Iterate over each character in the prefix.
            int index = c - 'a'; // Calculate the index corresponding to the character.
            if (!node->children[index]) { // If the child node doesn't exist, the prefix is not in the Trie.
                return false;
            }
            node = node->children[index]; // Move to the child node.
        }
        return true;  // The prefix exists in the Trie.
    }
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */



// Description: =================================================================================================================
/*
To implement a Trie (Prefix Tree), we need to define the Trie node structure and the Trie class itself. Each Trie node will contain a fixed-size array or hash map to store child nodes corresponding to different characters and a boolean flag to indicate the end of a word.

Here's a step-by-step guide to implement the Trie class:

1. **Define the TrieNode structure**: This includes an array/hash map for child nodes and a boolean flag to indicate the end of a word.
2. **Initialize the Trie**: The constructor initializes the root node.
3. **Insert a word**: Start from the root and traverse the Trie, creating new nodes for characters that do not exist. Mark the end of the word in the last node.
4. **Search for a word**: Traverse the Trie according to the characters in the word. If you can reach the end of the word and the node's end-of-word flag is true, the word exists in the Trie.
5. **Check for a prefix**: Similar to search, but return true if you can simply traverse the Trie according to the prefix's characters, regardless of the end-of-word flag.

### Description:

This solution defines a `TrieNode` class, which represents each node in the Trie, containing an array of child nodes for each lowercase English letter and a boolean flag to indicate the end of a word. The `Trie` class has methods to `insert` a word into the Trie, `search` for a word, and check if a prefix `startsWith` a previously inserted word. The `insert` method iterates over each character in the word, navigating through or creating necessary child nodes and marking the end of the word. The `search` method checks for the existence of each character in the word within the Trie, returning `true` if the end of the word is reached and the respective node is marked as an end-of-word node. The `startsWith` method is similar to `search` but only checks for the presence of a prefix, without considering the end-of-word flag.

*/
