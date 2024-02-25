// 2709. Greatest Common Divisor Traversal.     - HARD -


// Topic: Array, Math, Union Find, Number Theory.


/*
### Task:
---
You are given a 0-indexed integer array nums, and you are allowed to traverse between its indices. You can traverse between index i and index j, i != j, if and only if gcd(nums[i], nums[j]) > 1, where gcd is the greatest common divisor.

Your task is to determine if for every pair of indices i and j in nums, where i < j, there exists a sequence of traversals that can take us from i to j.

Return true if it is possible to traverse between all such pairs of indices, or false otherwise.

Example 1:
Input: nums = [2,3,6]
Output: true
Explanation: In this example, there are 3 possible pairs of indices: (0, 1), (0, 2), and (1, 2).
To go from index 0 to index 1, we can use the sequence of traversals 0 -> 2 -> 1, where we move from index 0 to index 2 because gcd(nums[0], nums[2]) = gcd(2, 6) = 2 > 1, and then move from index 2 to index 1 because gcd(nums[2], nums[1]) = gcd(6, 3) = 3 > 1.
To go from index 0 to index 2, we can just go directly because gcd(nums[0], nums[2]) = gcd(2, 6) = 2 > 1. Likewise, to go from index 1 to index 2, we can just go directly because gcd(nums[1], nums[2]) = gcd(3, 6) = 3 > 1.

Example 2:
Input: nums = [3,9,5]
Output: false
Explanation: No sequence of traversals can take us from index 0 to index 2 in this example. So, we return false.

Example 3:
Input: nums = [4,3,12,8]
Output: true
Explanation: There are 6 possible pairs of indices to traverse between: (0, 1), (0, 2), (0, 3), (1, 2), (1, 3), and (2, 3). A valid sequence of traversals exists for each pair, so we return true.

Constraints:
1 <= nums.length <= 10^5
1 <= nums[i] <= 10^5

Hint 1:
Create a (prime) factor-numbers list for all the indices.
Hint 2:
Add an edge between the neighbors of the (prime) factor-numbers list. The order of the numbers doesn’t matter. We only need edges between 2 neighbors instead of edges for all pairs.
Hint 3:
The problem is now similar to checking if all the numbers (nodes of the graph) are in the same connected component.
Hint 4:
Any algorithm (i.e., BFS, DFS, or Union-Find Set) should work to find or check connected components

### Testcase:
---
[2,3,6]
[3,9,5]
[4,3,12,8]


### Code:
---
class Solution {
public:
    bool canTraverseAllPairs(vector<int>& nums) {
        
    }
};

*/

// Solution: --------------------------------------

#include <vector>
#include <unordered_map>
#include <unordered_set>
using namespace std;

class Solution {
public:
    // Function to find the prime factors of a given number 'n'.
    // Returns a set containing all prime factors of 'n'.
    unordered_set<int> findPrimeFactors(int n) {
        unordered_set<int> factors;
        // Check divisibility by 2 and add to factors
        if (n % 2 == 0) {
            factors.insert(2);
            while (n % 2 == 0) n /= 2;  // Divide 'n' by 2 until it's odd
        }
        // Check for odd factors starting from 3 to sqrt(n)
        for (int i = 3; i * i <= n; i += 2) {
            if (n % i == 0) {
                factors.insert(i);
                while (n % i == 0) n /= i;  // Divide 'n' by 'i' until it's not divisible
            }
        }
        // If 'n' is a prime number greater than 2, add it to factors
        if (n > 2) factors.insert(n);
        return factors;
    }

    // Function for Union-Find's 'find' operation with path compression.
    // Finds and returns the root of the set to which element 'i' belongs.
    int find(vector<int>& parent, int i) {
        if (parent[i] != i)
            parent[i] = find(parent, parent[i]);  // Recursively find the root and compress path
        return parent[i];
    }

    // Function for Union-Find's 'union' operation.
    // Merges the sets containing elements 'x' and 'y'.
    void unionSets(vector<int>& parent, int x, int y) {
        int rootX = find(parent, x);  // Find root of 'x'
        int rootY = find(parent, y);  // Find root of 'y'
        if (rootX != rootY)
            parent[rootY] = rootX;  // Merge sets by making root of 'y' point to root of 'x'
    }

    // Main function to check if all pairs of indices in 'nums' are traversable.
    // Returns true if traversal is possible for all pairs, false otherwise.
    bool canTraverseAllPairs(vector<int>& nums) {
        int n = nums.size();
        vector<int> parent(n);  // Union-Find parent array
        for (int i = 0; i < n; ++i) parent[i] = i;  // Initialize each element as its own parent

        // Map to associate each prime factor with its first occurrence index in 'nums'
        unordered_map<int, int> primeToIndex;

        // Iterate over 'nums' to build the graph using Union-Find
        for (int i = 0; i < n; ++i) {
            unordered_set<int> primes = findPrimeFactors(nums[i]);  // Get prime factors of 'nums[i]'

            // For each prime factor, union current index 'i' with the index of its first occurrence
            for (int prime : primes) {
                if (primeToIndex.find(prime) != primeToIndex.end()) {
                    unionSets(parent, i, primeToIndex[prime]);
                } else {
                    primeToIndex[prime] = i;  // Mark the first occurrence of this prime factor
                }
            }
        }

        // Check if all elements in 'nums' belong to the same connected component
        int root = find(parent, 0);  // Find the root of the first element
        for (int i = 1; i < n; ++i) {
            if (find(parent, i) != root) return false;  // If any element has a different root, return false
        }

        return true;  // All elements are connected, return true
    }
};


// Description: ===================================
/*
The solution presented addresses the problem of determining whether it is possible to traverse between all pairs of indices in a given integer array, based on the condition that the greatest common divisor (GCD) of the values at those indices is greater than 1. This problem is framed within the context of an array, mathematics, Union Find data structure, and number theory. The approach effectively transforms the problem into a graph connectivity issue, where nodes represent array indices, and edges exist between nodes if the GCD of their corresponding values is greater than 1.

### Key Components of the Solution:

- **Prime Factorization**: The solution employs prime factorization to identify common factors between numbers. This step is crucial because two numbers can traverse to each other if they share at least one prime factor (other than 1), implying their GCD is greater than 1.

- **Graph Representation**: The problem is mapped onto a graph model where each index in the array represents a node. Edges between nodes are established based on shared prime factors, indicating possible traversal paths due to the GCD condition.

- **Union Find Data Structure**: To efficiently manage and query connectivity between nodes (indices), the Union Find data structure is utilized. It helps in grouping indices into sets, where each set represents a connected component in the graph. Two indices belong to the same set if there is a sequence of traversals possible between them.

- **Traversal Sequence**: The essence of the problem is to verify that for any two indices, there exists a sequence of moves from one to the other, leveraging the edges defined by the GCD condition. This is equivalent to checking if all indices belong to the same connected component in the graph representation.

### Solution Workflow:

1. **Initialization**: An array to represent the Union Find structure is initialized, where each index initially points to itself, indicating separate sets.

2. **Building Connections**: For each number in the input array, its prime factors are determined. An edge (Union operation in the Union Find structure) is created between indices if their numbers share a prime factor, effectively merging their sets.

3. **Connectivity Check**: After establishing all possible connections, the solution checks if all indices belong to the same set (connected component) in the Union Find structure. This is done by comparing the root of each index to a reference root (e.g., the root of the first index).

4. **Result**: If all indices are found to be in the same set, it indicates that a traversal sequence exists between every pair of indices, and the function returns `true`. Otherwise, it returns `false`.

### Conclusion:

This solution elegantly transforms the problem into a graph connectivity issue, solving it efficiently using prime factorization to identify connections and the Union Find data structure to manage and query these connections. It provides a systematic approach to verify the possibility of traversal between all pairs of indices under the given GCD condition, making it a fascinating application of number theory and data structure concepts in algorithm design.

*/
