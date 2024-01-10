"""
# 763. Partition Labels.

# Topic: Hash Table, Two Pointers, String, Greedy.

# Task:
---------
You are given a string s. We want to partition the string into as many parts as possible so that 
each letter appears in at most one part.

Note that the partition is done so that after concatenating all the parts in order, the resultant 
string should be s.

Return a list of integers representing the size of these parts.

Example 1:
Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.

Example 2:
Input: s = "eccbbbbdec"
Output: [10]

Constraints:
1 <= s.length <= 500
s consists of lowercase English letters.

Hint 1:
Try to greedily choose the smallest partition that includes the first letter. If you have something like "abaccbdeffed", 
then you might need to add b. You can use an map like "last['b'] = 5" to help you expand the width of your partition.



# Testcase:
------------
"ababcbacadefegdehijhklij"
"eccbbbbdec"

# Code:
-------------
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        

"""
# Solution:
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # Dictionary to store the last occurrence of each character
        last_occurrence = {char: idx for idx, char in enumerate(s)}

        # Variables to keep track of the start and end of the current partition
        start, end = 0, 0

        # List to store the size of each partition
        partition_sizes = []

        # Iterate through the string
        for idx, char in enumerate(s):
            # Update the end of the current partition
            end = max(end, last_occurrence[char])

            # If the current index is the end of the partition
            if idx == end:
                # Add the size of the current partition to the list
                partition_sizes.append(end - start + 1)
                # Update the start for the next partition
                start = idx + 1

        return partition_sizes




# Description:
'''
To solve the "Partition Labels" problem, a greedy approach can be used. The main idea is to iterate through the string s 
and keep track of the last occurrence of each character. This helps in determining the end of a partition, as a partition 
should contain all occurrences of the characters it includes.

Here's the step-by-step approach:

1.Store Last Occurrences: First, iterate through the string s and store the last index of each character in a hash table 
  (e.g., a dictionary in Python).

2.Iterate to Create Partitions: Then, iterate through the string again and for each character:
  - Update the end of the current partition to be the maximum of the current end and the last occurrence of the character.
  - If the current index reaches the end of the partition, it means we have found a partition. Record its size, and start
    a new partition.

3. Return Partition Sizes: Store the sizes of the partitions in a list and return it.

In this solution:

* We first create a dictionary last_occurrence to store the last index of each character in s.
* We then iterate over s, updating the end of the current partition whenever we encounter a character whose last occurrence 
  is farther than the current end.
* When we reach the end of a partition, we add its size to partition_sizes and update the start for the next partition.
* This approach ensures that each partition contains all occurrences of the characters it includes and no more, thus meeting 
  the problem's requirement.


'''
