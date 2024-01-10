# 433. Minimum Genetic Mutation

# Topic: Hash Table, String, Breadth-First Search.

'''
# Task:
-------
A gene string can be represented by an 8-character long string, with choices from 'A', 'C', 'G', and 'T'.

Suppose we need to investigate a mutation from a gene string startGene to a gene string endGene where one mutation is
defined as one single character changed in the gene string.

For example, "AACCGGTT" --> "AACCGGTA" is one mutation.
There is also a gene bank bank that records all the valid gene mutations. A gene must be in bank to make it a valid 
gene string.

Given the two gene strings startGene and endGene and the gene bank bank, return the minimum number of mutations needed 
to mutate from startGene to endGene. If there is no such a mutation, return -1.

Note that the starting point is assumed to be valid, so it might not be included in the bank.

Example 1:
Input: startGene = "AACCGGTT", endGene = "AACCGGTA", bank = ["AACCGGTA"]
Output: 1

Example 2:
Input: startGene = "AACCGGTT", endGene = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
Output: 2

Constraints:
0 <= bank.length <= 10
startGene.length == endGene.length == bank[i].length == 8
startGene, endGene, and bank[i] consist of only the characters ['A', 'C', 'G', 'T'].


# Testcase:
-----------
"AACCGGTT"
"AACCGGTA"
["AACCGGTA"]
"AACCGGTT"
"AAACGGTA"
["AACCGGTA","AACCGCTA","AAACGGTA"]


# Code:
-------
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
     

'''
# Solution:
from typing import List
from collections import deque

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        # Return -1 if endGene is not in the bank
        if endGene not in bank:
            return -1

        # Convert bank list to a set for efficient access
        bank = set(bank)
        # Initialize BFS queue with startGene and mutation count
        queue = deque([(startGene, 0)])
        # Set of valid characters in a gene
        valid_chars = {'A', 'C', 'G', 'T'}

        while queue:
            current_gene, mutations = queue.popleft()
            # Check if the current gene is the target gene
            if current_gene == endGene:
                return mutations

            # Generate all possible one-character mutations
            for i in range(len(current_gene)):
                for char in valid_chars:
                    mutated_gene = current_gene[:i] + char + current_gene[i+1:]
                    # Check if the mutation is valid and in the bank
                    if mutated_gene in bank:
                        # Remove from bank to avoid revisiting
                        bank.remove(mutated_gene)
                        # Add mutated gene to the queue
                        queue.append((mutated_gene, mutations + 1))

        # Return -1 if mutation to endGene is not possible
        return -1

# Testing the solution
sol = Solution()
print(sol.minMutation("AACCGGTT", "AACCGGTA", ["AACCGGTA"]))  # Expected output: 1
print(sol.minMutation("AACCGGTT", "AAACGGTA", ["AACCGGTA","AACCGCTA","AAACGGTA"]))  # Expected output: 2


#Description:
'''
Description of the "Minimum Genetic Mutation" Solution
The Python solution provided addresses the "Minimum Genetic Mutation" problem, which is conceptually similar to the 
"Word Ladder" problem. The task is to find the minimum number of mutations required to transform a start gene sequence 
into an end gene sequence using a given set of valid mutations (bank). A mutation is defined as a change in one 
character in the gene string.

Key Components of the Solution:
BFS Algorithm: The solution employs the Breadth-First Search (BFS) algorithm to explore the possible mutations level 
by level, ensuring the minimum number of mutations is found.

Data Structures:

A queue (deque) is used to store the gene sequences and their corresponding mutation count.
A set (bank) is used for efficient lookup and to avoid revisiting the same gene sequence.
Mutation Generation: For each gene sequence, the algorithm generates all possible valid mutations by changing one 
character at a time.

Early Termination: If the end gene sequence is not in the bank, the function returns -1 immediately, as mutation 
to the end gene is impossible.

Goal Check: If a mutation matches the end gene sequence, the current mutation count is returned.

Avoiding Revisits: Once a mutation is used, it is removed from the bank to prevent revisiting.

Efficiency of the Solution:
Time Complexity: O(N * M), where N is the number of genes in the bank and M is the length of the gene sequence. 
Each gene is visited and for each gene, all possible mutations are generated.
Space Complexity: O(N), primarily for the storage of the bank and the queue.
This solution is efficient for finding the minimum number of mutations required to reach the end gene sequence, 
ensuring that all possible paths are explored without unnecessary repetitions.

'''
