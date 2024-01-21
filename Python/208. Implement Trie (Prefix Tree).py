# 208. Implement Trie (Prefix Tree).            -Medium-

# Topic:Hash Table, String, Design, Trie.

"""
### Task:
---
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve 
keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

- Trie() Initializes the trie object.
- void insert(String word) Inserts the string word into the trie.
- boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
- boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, 
  and false otherwise.
 
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
class Trie:

    def __init__(self):
        

    def insert(self, word: str) -> None:
        

    def search(self, word: str) -> bool:
        

    def startsWith(self, prefix: str) -> bool:
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

"""
### Solution: ------------------------------------

class TrieNode:
    def __init__(self):
        # Each node stores its children in a dictionary.
        # Keys are characters, and values are TrieNode objects.
        self.children = {}
        # Flag to indicate if a word ends at this node.
        self.isEndOfWord = False

class Trie:
    def __init__(self):
        # The root node of the Trie, which is an empty node initially.
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        # Start from the root node.
        node = self.root
        for char in word:
            # For each character in the word, find the corresponding child node.
            if char not in node.children:
                # If the child node doesn't exist, create a new TrieNode.
                node.children[char] = TrieNode()
            # Move to the child node.
            node = node.children[char]
        # After the last character, mark this node as the end of a word.
        node.isEndOfWord = True

    def search(self, word: str) -> bool:
        # Start from the root node.
        node = self.root
        for char in word:
            # For each character in the word, find the corresponding child node.
            if char not in node.children:
                # If a character is not found, the word does not exist in the Trie.
                return False
            # Move to the child node.
            node = node.children[char]
        # Return true if the current node is marked as the end of the word.
        return node.isEndOfWord

    def startsWith(self, prefix: str) -> bool:
        # Start from the root node.
        node = self.root
        for char in prefix:
            # For each character in the prefix, find the corresponding child node.
            if char not in node.children:
                # If a character is not found, no words start with this prefix.
                return False
            # Move to the child node.
            node = node.children[char

]
        # If the prefix is traversed successfully, return true.
        # It's not necessary for the node to be the end of a word; we only care about the prefix.
        return True
    

### Description: =================================

'''
### Comments Explanation:
- **TrieNode Class**: A helper class representing each node in the Trie. Each node has a `children` dictionary, mapping characters to their corresponding child nodes, and a boolean `isEndOfWord` to indicate if a node is the end of a word.
- **Trie Class Initialization**: In the `__init__` method of the `Trie` class, a root node is created. This root node is essentially an empty node to start building the Trie.
- **Insert Method**: This method iterates through each character of the input word. For each character, it checks if the corresponding child node exists in the current node's `children`. If not, it creates a new `TrieNode`. It then moves to this child node and continues. Finally, it marks the node corresponding to the last character as the end of a word.
- **Search Method**: Similar to `insert`, but instead of creating new nodes, it checks if each character of the word exists in the Trie. If any character is missing, it returns `False`. If all characters are found and the final node is marked as the end of a word, it returns `True`.
- **StartsWith Method**: This method checks if a prefix exists in the Trie. It is similar to `search`, but it only needs to check if the nodes corresponding to each character in the prefix exist. It does not need to check if the final node is marked as the end of a word.

These comments provide clear explanations of each part of the Trie implementation, detailing the functionality and purpose of each method and the `TrieNode` class, which together facilitate efficient string insertion, search, and prefix matching.

Implementing a Trie (or Prefix Tree) is a classic problem that tests understanding of tree-like data structures and their applications in operations like search and prefix matching. Let's dive into the solution.

### Problem Analysis:
A Trie is a specialized tree used in searching, most often with strings. The key tasks are:
- **Insertion**: Add a word to the Trie.
- **Search**: Check if a word is present in the Trie.
- **Prefix Matching**: Check if any word in the Trie starts with a given prefix.

### Approach:
1. **Trie Node Structure**:
   - Each node should contain a map (or array) pointing to its child nodes and a boolean to mark the end of a word.

2. **Insertion**:
   - Start from the root and for each character in the word, go to the corresponding child node.
   - If the child node doesn’t exist, create a new node.
   - Mark the end of the word in the last node.

3. **Search**:
   - Similar to insertion, but check if each character of the word is present in Trie.
   - If any character is missing, return false.
   - If all characters are found and the last node is marked as the end of a word, return true.

4. **Starts With (Prefix Matching)**:
   - Similar to search, but it's only necessary to check if the prefix is present, not whether it marks the end of a word.


### Explanation:
- **TrieNode Class**: Represents a node in the Trie. Each node has a map (`children`) to represent its children and a flag (`isEndOfWord`) to indicate if it's the end

 of a word.
- **Trie Class Initialization**: Initializes the Trie with a root node.
- **Insert Method**: Iterates through each character of the word. For each character, if the corresponding child node does not exist, it creates a new one. Finally, it marks the last node as the end of a word.
- **Search Method**: Similar to insert, it traverses the Trie for each character in the word. If any character node is missing, it returns false. It also checks if the last node is marked as the end of a word.
- **StartsWith Method**: Traverses the Trie for each character in the prefix. If any character node is missing, it returns false. Unlike search, it doesn't need to check if the last node is the end of a word, as it's only concerned with the prefix.

### Time Complexity:
- **Insert**: O(m), where m is the length of the word.
- **Search**: O(m), for a word of length m.
- **StartsWith**: O(p), for a prefix of length p.

### Test Case:
For the test case `["Trie", "insert", "search", "search", "startsWith", "insert", "search"]` and `[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]`:
- Create a Trie.
- Insert "apple".
- Search "apple" -> returns `True`.
- Search "app" -> returns `False` (as "app" is not a complete word in the Trie).
- Check startsWith "app" -> returns `True`.
- Insert "app".
- Search "app" -> returns `True`.

This Trie implementation efficiently handles the operations of insertion, search, and prefix matching in a dataset of strings, making it suitable for applications like autocomplete and spellcheckers.

'''
