// 208. Implement Trie (Prefix Tree).           -medium-

// Topic: Hash Table, String, Design, Trie.


/*
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
struct Trie {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl Trie {

    fn new() -> Self {
        
    }
    
    fn insert(&self, word: String) {
        
    }
    
    fn search(&self, word: String) -> bool {
        
    }
    
    fn starts_with(&self, prefix: String) -> bool {
        
    }
}

/**
 * Your Trie object will be instantiated and called as such:
 * let obj = Trie::new();
 * obj.insert(word);
 * let ret_2: bool = obj.search(word);
 * let ret_3: bool = obj.starts_with(prefix);
 */
*/

// Solution: ------------------------------------


// Constant representing the size of the alphabet (26 English lowercase letters).
const ALPHABET_SIZE: usize = 26;

// Definition of a TrieNode struct.
struct TrieNode {
    // Each node has `ALPHABET_SIZE` children, stored in an array.
    // `Option<Box<TrieNode>>` is used for each child, where `None` indicates no child node.
    children: [Option<Box<TrieNode>>; ALPHABET_SIZE],

    // Flag to mark the end of a word.
    is_end_of_word: bool,
}

impl TrieNode {
    // Constructor for a new TrieNode.
    fn new() -> Self {
        TrieNode {
            // Initialize the children array with `None`, meaning no children initially.
            children: Default::default(),
            is_end_of_word: false,
        }
    }

    // Helper function to map a character to its corresponding index in the children array.
    // Converts a lowercase English letter to a zero-based index.
    fn index(c: char) -> usize {
        (c as usize) - ('a' as usize)
    }
}

// Definition of the Trie struct.
struct Trie {
    // The root node of the Trie.
    root: TrieNode,
}

impl Trie {
    // Constructor for a new Trie.
    fn new() -> Self {
        Trie {
            root: TrieNode::new(),
        }
    }

    // Method to insert a word into the Trie.
    fn insert(&mut self, word: String) {
        let mut node = &mut self.root;
        for c in word.chars() {
            // Determine the index for the character.
            let idx = TrieNode::index(c);
            // Access the child node at the index, creating a new node if it doesn't exist.
            node = node.children[idx].get_or_insert_with(|| Box::new(TrieNode::new()));
        }
        // Mark the end of the word.
        node.is_end_of_word = true;
    }

    // Method to check if a word exists in the Trie.
    fn search(&self, word: String) -> bool {
        let mut node = &self.root;
        for c in word.chars() {
            // Determine the index for the character.
            let idx = TrieNode::index(c);
            // Check if the child node exists; if

 not, return false.
            match node.children[idx].as_ref() {
                Some(n) => node = n,
                None => return false,
            }
        }
        // Return true if the end of the word has been reached, false otherwise.
        node.is_end_of_word
    }

    // Method to check if any word in the Trie starts with the given prefix.
    fn starts_with(&self, prefix: String) -> bool {
        let mut node = &self.root;
        for c in prefix.chars() {
            // Determine the index for the character.
            let idx = TrieNode::index(c);
            // Check if the child node exists; if not, return false.
            match node.children[idx].as_ref() {
                Some(n) => node = n,
                None => return false,
            }
        }
        // If the loop completes without returning false, a prefix match exists.
        true
    }
}



// Description: =================================
/*
### Commentary:

- The `TrieNode` struct represents each node in the Trie. It contains an array of child nodes, with one entry for each letter in the alphabet, and a boolean to indicate whether it represents the end of a word.

- The `Trie` struct represents the entire Trie. It has a root `TrieNode` from which all words are branched out.

- The `insert` method iterates through each character in the input word, creating new nodes as necessary, and marks the end of the word.

- The `search` method checks for the existence of a word in the Trie, traversing node by node according to the word's characters.

- The `starts_with` method verifies if any word in the Trie starts with a given prefix, similar to the `search` method but only checks for the presence of the prefix, not the complete word.

These methods collectively allow the Trie to efficiently store and query strings, particularly useful for tasks like autocomplete and spell checking in large datasets of strings.

### Description of the Trie Data Structure Implementation in Rust

The implementation of the Trie (Prefix Tree) data structure in Rust involves creating a specialized tree-like structure optimized for efficient storage and retrieval of strings. This data structure is particularly useful in applications like autocomplete systems, spell checkers, and other scenarios where quick lookup of words or prefixes is required.



#### Core Components:

1. **TrieNode Structure:**
   - Each node (`TrieNode`) in the Trie represents a single character of a word.
   - It contains an array of child nodes, each corresponding to one of the 26 lowercase English letters

. This array is implemented as `[Option<Box<TrieNode>>; ALPHABET_SIZE]`, where `ALPHABET_SIZE` is 26 for the English alphabet.
   - The `Option<Box<TrieNode>>` type allows each element in the array to either hold a `TrieNode` (boxed, i.e., heap-allocated) or `None`, indicating the absence of a child node for the corresponding letter.
   - A boolean flag `is_end_of_word` indicates whether the node marks the completion of a valid word in the Trie.

2. **Trie Structure:**
   - The Trie itself is represented by the `Trie` struct, which primarily

contains a root `TrieNode`. This root node acts as the entry point to the Trie and does not correspond to any character.
   - The Trie provides a framework for implementing various methods that operate on the TrieNode structure to insert words, search for words, and check for the presence of prefixes.

#### Key Methods:

1. **Insertion (`insert`):**
   - Words are inserted into the Trie character by character.
   - Starting from the root, the method navigates through or creates child nodes for each character in the word.
   - Once the end of the word is reached, the `is_end_of_word` flag is set to `true` on the final node, marking the completion of a word.

2. **Search (`search`):**
   - The search operation checks whether a complete word exists in the Trie.
   - It traverses the Trie from the root, following the path of characters in the word.
   - If the path exists and ends with `is_end_of_word` set to `true`, the word is present in the Trie.

3. **Prefix Checking (`starts_with`):**
   - This operation checks if there is any word in the Trie that starts with a given prefix.
   - Similar to `search`, it traverses the Trie according to the characters in the prefix.
   - The method returns `true` if the path for the entire prefix exists, regardless of the `is_end_of_word` flag.

#### Performance and Use Cases:

- **Efficiency:** The Trie structure is highly efficient for scenarios involving a large number of string lookups. 
   It optimizes both the storage and retrieval of strings, particularly when dealing with large datasets of words.
- **Use Cases:** Commonly used in situations where quick prefix searches are frequent, such as in autocomplete systems, 
   spell checkers, or in implementing dictionaries.

#### Conclusion:

This Rust implementation of the Trie data structure demonstrates an efficient approach to handling strings in a way that 
optimizes for quick insertions and search operations. It leverages Rust's memory safety and efficient data structures, 
like `HashMap`, to provide a robust and performance-oriented solution.


*/
