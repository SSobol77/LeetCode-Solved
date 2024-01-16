// # 380. Insert Delete GetRandom O(1).            -Medium-

// Topic: Array, Hash Table, Math, Design, Randomized.

/*
### Task:
---
Implement the RandomizedSet class:

RandomizedSet() Initializes the RandomizedSet object.
bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
You must implement the functions of the class such that each function works in average O(1) time complexity.

#Example 1:
Input
["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]
Output
[null, true, false, true, 2, true, false, 2]

Explanation
RandomizedSet randomizedSet = new RandomizedSet();
randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2].
randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.
randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now contains [2].
randomizedSet.insert(2); // 2 was already in the set, so return false.
randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom() will always return 2.
 
#Constraints:
-2^31 <= val <= 2^31 - 1
At most 2 * 10^5 calls will be made to insert, remove, and getRandom.
There will be at least one element in the data structure when getRandom is called.


### Testcase:
---
["RandomizedSet","insert","remove","insert","getRandom","remove","insert","getRandom"]
[[],[1],[2],[2],[],[1],[2],[]]


### Code:
---

struct RandomizedSet {

}

/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl RandomizedSet {

    fn new() -> Self {
        
    }
    
    fn insert(&self, val: i32) -> bool {
        
    }
    
    fn remove(&self, val: i32) -> bool {
        
    }
    
    fn get_random(&self) -> i32 {
        
    }
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * let obj = RandomizedSet::new();
 * let ret_1: bool = obj.insert(val);
 * let ret_2: bool = obj.remove(val);
 * let ret_3: i32 = obj.get_random();
 */

*/
// Solution: ------------------------------------------------------------------------------

use rand::{thread_rng, Rng};  // Importing necessary items from the rand crate
use std::collections::HashMap; // Importing HashMap from the standard library

// A structure representing the RandomizedSet
struct RandomizedSet {
    map: HashMap<i32, usize>, // HashMap to store the value and its index in the vector
    vec: Vec<i32>,            // Vector to store the actual values
}

impl RandomizedSet {
    // Constructor for the RandomizedSet
    fn new() -> Self {
        RandomizedSet {
            map: HashMap::new(), // Initialize an empty HashMap
            vec: Vec::new(),     // Initialize an empty Vector
        }
    }

    // Inserts a value into the set. Returns true if the value was not present, false otherwise
    fn insert(&mut self, val: i32) -> bool {
        // Check if the value is already in the map
        if self.map.contains_key(&val) {
            false // Value already exists, return false
        } else {
            self.vec.push(val);        // Add the value to the vector
            let idx = self.vec.len() - 1; // Calculate the index of the newly added value
            self.map.insert(val, idx);    // Map the value to its index
            true  // Value inserted successfully, return true
        }
    }

    // Removes a value from the set. Returns true if the value was present, false otherwise
    fn remove(&mut self, val: i32) -> bool {
        match self.map.remove(&val) {
            Some(idx) => {
                let last_val = self.vec.pop().unwrap(); // Remove the last value from the vector
                if idx < self.vec.len() {  // Check if the removed element is not the last one
                    self.vec[idx] = last_val;  // Move the last element to the removed element's position
                    self.map.insert(last_val, idx); // Update the map with the new index for the moved element
                }
                true  // Value removed successfully, return true
            }
            None => false, // Value not found in the set, return false
        }
    }

    // Returns a random element from the set
    fn get_random(&self) -> i32 {
        let mut rng = thread_rng(); // Create a random number generator
        let idx = rng.gen_range(0, self.vec.len()); // Generate a random index
        self.vec[idx] // Return the value at the random index
    }
}


// Description: =======================================================================================
/*
Description of the solution for the `RandomizedSet` implementation in Rust:

### Overview
The `RandomizedSet` class is designed to support the insertion, removal, and retrieval of random elements with average time complexity O(1). This is achieved by combining a `HashMap` and a `Vec`.

### Data Structures
- **HashMap (`map`)**: This `HashMap` maps each value (`i32`) to its index (`usize`) in the `Vec`. It's used for quick lookup to check if a value already exists in the set and to find its index for removal.
- **Vector (`vec`)**: The `Vec` stores the actual values of the set. It enables us to access elements at specific indices quickly, which is essential for the `get_random` function.

### Methods

1. **`new`**
   - **Purpose**: Creates a new `RandomizedSet` instance with an empty `HashMap` and `Vec`.
   - **Complexity**: O(1), as it only involves initializing empty data structures.

2. **`insert`**
   - **Purpose**: Inserts a new value into the set.
   - **Parameters**: `val` (i32) - The value to insert.
   - **Return**: `bool` - `true` if the value was added, `false` if it was already present.
   - **Logic**: 
     - Check if the value is already in the map.
     - If not, add the value to the `Vec` and map the value to its index in the `HashMap`.
   - **Complexity**: O(1) on average, due to the constant-time operation of `HashMap` and `Vec`.

3. **`remove`**
   - **Purpose**: Removes a value from the set.
   - **Parameters**: `val` (i32) - The value to remove.
   - **Return**: `bool` - `true` if the value was removed, `false` if it was not found.
   - **Logic**:
     - Remove the value-index mapping from the `HashMap`.
     - If the value is in the set, swap it with the last element in the `Vec` and then remove it to maintain the integrity of the index mapping.
   - **Complexity**: O(1) on average, as `HashMap` and `Vec` operations are generally constant time.

4. **`get_random`**
   - **Purpose**: Returns a random element from the set.
   - **Return

**: `i32` - A random value from the set.
   - **Logic**:
     - Generate a random index within the range of the `Vec`'s length.
     - Return the value at this random index from the `Vec`.
   - **Complexity**: O(1), as accessing an element by index in a `Vec` and generating a random number are constant time operations.

### Implementation Details

- **Insertion**: When a new value is inserted, it's added to the end of the `Vec`, and its index is stored in the `HashMap`. This ensures that future lookups, insertions, or deletions of this value can be done in O(1) time.
  
- **Removal**: To remove a value, the algorithm finds its index from the `HashMap` and then swaps this value with the last element in the `Vec`. This swapping is crucial because it allows the `Vec` to maintain contiguous storage and enables the removal of the last element in O(1) time. After the swap, the `HashMap` is updated to reflect the new index of the element that was swapped.

- **Random Selection**: The `get_random` function generates a random index and retrieves the value at this index from the `Vec`. The use of the `Vec` ensures that each element has an equal probability of being chosen.

### Performance Considerations

- **HashMap**: Provides O(1) average time complexity for insertions, deletions, and lookups.
- **Vector**: Ensures constant time

access to elements, which is particularly important for the `get_random` operation.

### Trade-offs

- **Memory Usage**: The use of a `HashMap` alongside a `Vec` means that the data structure consumes more memory than a simple list or set. This is the trade-off for achieving O(1) time complexity for insertions, deletions, and retrieving a random element.
- **Random Number Generation**: The `get_random` method relies on the `rand` crate for random number generation. The performance of this method can vary slightly based on the efficiency of the random number generator used.

### Usage Scenario

This implementation is particularly useful in scenarios where a data structure needs to support very fast insertions, deletions, and retrieval of random elements. Typical use cases might include load balancing, random sampling, or in certain types of caching mechanisms.

### Conclusion

The `RandomizedSet` in Rust, using a combination of a `HashMap` and a `Vec`, provides an efficient solution for managing a collection of items with the ability to insert, remove, and retrieve random elements in constant average time. The implementation balances the need for speed with increased memory usage, making it a practical choice for performance-critical applications that require such operations.
*/