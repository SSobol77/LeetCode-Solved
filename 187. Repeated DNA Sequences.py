# 187. Repeated DNA Sequences.

# Topic: Hash Table, String, Bit Manipulation, Sliding Window, Rolling Hash, Hash Function.

'''
# Task
-------------------
The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.

    For example, "ACGAATTCCG" is a DNA sequence.

When studying DNA, it is useful to identify repeated sequences within the DNA.

Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) 
that occur more than once in a DNA molecule. You may return the answer in any order.

Example 1:
Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC","CCCCCAAAAA"]

Example 2:
Input: s = "AAAAAAAAAAAAA"
Output: ["AAAAAAAAAA"]

Constraints:
1 <= s.length <= 10^5
s[i] is either 'A', 'C', 'G', or 'T'.


# Testcase:
--------------------
"AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
"AAAAAAAAAAAAA"


# Code:
-----------
class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        

'''
# Solution:
class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        # Dictionary to keep track of all sequences and their counts
        sequence_count = {}
        repeated_sequences = set()

        # Iterate through the string
        for i in range(len(s) - 9):
            sequence = s[i:i+10]
            if sequence in sequence_count:
                # If sequence is already seen, add it to the set of repeated sequences
                repeated_sequences.add(sequence)
            else:
                # Otherwise, add it to the dictionary
                sequence_count[sequence] = 1

        return list(repeated_sequences)

# Test cases
sol = Solution()
test1 = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
test2 = "AAAAAAAAAAAAA"

output1 = sol.findRepeatedDnaSequences(test1)
output2 = sol.findRepeatedDnaSequences(test2)

output1, output2

# Description:
'''
The solution correctly identifies all 10-letter-long sequences (substrings) that occur more
than once in a DNA molecule:

1. For the input "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT", the output is ["CCCCCAAAAA", "AAAAACCCCC"]. 
   These are the sequences that are repeated in the given DNA string.

2. For the input "AAAAAAAAAAAAA", the output is ["AAAAAAAAAA"]. This is the repeated 10-letter 
   sequence in the DNA string

'''
