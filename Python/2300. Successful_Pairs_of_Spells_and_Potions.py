"""
# 2300. Successful Pairs of Spells and Potions.


# Topic: Array, Two Pointers, Binary Search, Sorting.



# Task:
------------
You are given two positive integer arrays spells and potions, of length n and m respectively,
where spells[i] represents the strength of the i^th spell and potions[j] represents the strength 
of the j^th potion.

You are also given an integer success. A spell and potion pair is considered successful if the 
product of their strengths is at least success.

Return an integer array pairs of length n where pairs[i] is the number of potions that will form a 
successful pair with the i^th spell.

 

Example 1:

Input: spells = [5,1,3], potions = [1,2,3,4,5], success = 7
Output: [4,0,3]
Explanation:
- 0^th spell: 5 * [1,2,3,4,5] = [5,10,15,20,25]. 4 pairs are successful.
- 1^st spell: 1 * [1,2,3,4,5] = [1,2,3,4,5]. 0 pairs are successful.
- 2^nd spell: 3 * [1,2,3,4,5] = [3,6,9,12,15]. 3 pairs are successful.
Thus, [4,0,3] is returned.

Example 2:
Input: spells = [3,1,2], potions = [8,5,8], success = 16
Output: [2,0,2]
Explanation:
- 0^th spell: 3 * [8,5,8] = [24,15,24]. 2 pairs are successful.
- 1^st spell: 1 * [8,5,8] = [8,5,8]. 0 pairs are successful. 
- 2^nd spell: 2 * [8,5,8] = [16,10,16]. 2 pairs are successful. 
Thus, [2,0,2] is returned.

Constraints:
n == spells.length
m == potions.length
1 <= n, m <= 10^5
1 <= spells[i], potions[i] <= 10^5
1 <= success <= 10^10

Hint 1:
Notice that if a spell and potion pair is successful, then the spell and all stronger potions will be successful too.
Hint 2:
Thus, for each spell, we need to find the potion with the least strength that will form a successful pair.
Hint 3:
We can efficiently do this by sorting the potions based on strength and using binary search.


# Testcase:
--------------
[5,1,3]
[1,2,3,4,5]
7
[3,1,2]
[8,5,8]
16


# Code:
------------
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
   
"""
# Solution:
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        # Sort the potions array for binary search
        potions.sort()
        n = len(potions)
        result = []

        # Iterate through each spell
        for spell in spells:
            # Binary search to find the first potion that makes a successful pair
            left, right = 0, n
            while left < right:
                mid = (left + right) // 2
                # If the product of the spell and the potion at mid is at least success
                if spell * potions[mid] >= success:
                    right = mid  # Move the right pointer to narrow down the search
                else:
                    left = mid + 1  # Otherwise, move the left pointer

            # The number of successful pairs is determined by the number of potions
            # from the found potion to the end of the array
            result.append(n - left)

        return result


# Description:
'''
To solve the "Successful Pairs of Spells and Potions" problem, we need to count the number of 
potion-spell combinations that meet or exceed a certain success threshold. The key is to realize 
that if a certain potion is successful with a spell, all stronger potions will also be successful. 
This allows us to use binary search to efficiently find the least strong potion that forms a successful 
pair for each spell, given that the potions are sorted.

Here's the step-by-step approach:
-----------------------------------
1    Sort the Potions: Sort the potions array in ascending order.

2    Iterate over Spells and Apply Binary Search:
        For each spell in spells, use binary search on the potions array to find the first potion that, when multiplied with the spell, meets or exceeds the success value.

3    Count Successful Pairs:
        The number of successful pairs for each spell is the number of potions from the found potion to the end of the potions array.

4    Return the Result Array.


Testing the Solution:
---------------------------------------------------
    Test Case 1: spells = [5,1,3], potions = [1,2,3,4,5], success = 7
        The number of successful pairs for each spell are [4,0,3].

    Test Case 2: spells = [3,1,2], potions = [8,5,8], success = 16
        The number of successful pairs for each spell are [2,0,2].


        
This code uses binary search to efficiently find the first potion in the sorted potions array that, 
when multiplied with each spell, meets or exceeds the success threshold. For each spell, it calculates 
the number of successful pairs by determining how many potions from the identified position to the end
of the potions array can form a successful pair with that spell. This approach provides an optimal 
solution, especially suitable for large datasets.       

This solution efficiently calculates the number of successful pairs for each spell by using a sorted 
array and binary search, ensuring optimal performance for large datasets.

'''
