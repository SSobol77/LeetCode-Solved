# 48. Rotate Image.

# Topic: Array, Math, Matrix.

"""
### Task:
---
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
In computer science, an in-place algorithm is an algorithm that operates directly on the input data structure without requiring extra space proportional 
to the input size. In other words, it modifies the input in place, without creating a separate copy of the data structure. An algorithm which is not 
in-place is sometimes called not-in-place or out-of-place.
In-place can have slightly different meanings. In its strictest form, the algorithm can only have a constant amount of extra space, counting everything 
including function calls and pointers. However, this form is very limited as simply having an index to a length n array requires O(log n) bits. More 
broadly, in-place means that the algorithm does not use extra space for manipulating the input but may require a small though nonconstant extra space 
for its operation. Usually, this space is O(log n), though sometimes anything in o(n) is allowed. Note that space complexity also has varied choices in 
whether or not to count the index lengths as part of the space used. Often, the space complexity is given in terms of the number of indices or pointers 
needed, ignoring their length. In this article, we refer to total space complexity (DSPACE), counting pointer lengths. Therefore, the space requirements 
here have an extra log n factor compared to an analysis that ignores the length of indices and pointers.

An algorithm may or may not count the output as part of its space usage. Since in-place algorithms usually overwrite their input with output, no additional
space is needed. When writing the output to write-only memory or a stream, it may be more appropriate to only consider the working space of the algorithm. 
In theoretical applications such as log-space reductions, it is more typical to always ignore output space (in these cases it is more essential that the 
output is write-only).

Examples in-place algorithm:
Given an array a of n items, suppose we want an array that holds the same elements in reversed order and to dispose of the original. 
One seemingly simple way to do this is to create a new array of equal size, fill it with copies from a in the appropriate order and then delete a.

 function reverse(a[0..n - 1])
     allocate b[0..n - 1]
     for i from 0 to n - 1
         b[n − 1 − i] := a[i]
     return b
Unfortunately, this requires O(n) extra space for having the arrays a and b available simultaneously. Also, allocation and deallocation are often 
slow operations. Since we no longer need a, we can instead overwrite it with its own reversal using this in-place algorithm which will only need 
constant number (2) of integers for the auxiliary variables i and tmp, no matter how large the array is.

 function reverse_in_place(a[0..n-1])
     for i from 0 to floor((n-2)/2)
         tmp := a[i]
         a[i] := a[n − 1 − i]
         a[n − 1 − i] := tmp
As another example, many sorting algorithms rearrange arrays into sorted order in-place, including: bubble sort, comb sort, selection sort, insertion 
sort, heapsort, and Shell sort. These algorithms require only a few pointers, so their space complexity is O(log n).[1]

Quicksort operates in-place on the data to be sorted. However, quicksort requires O(log n) stack space pointers to keep track of the subarrays in its 
divide and conquer strategy. Consequently, quicksort needs O(log2 n) additional space. Although this non-constant space technically takes quicksort 
out of the in-place category, quicksort and other algorithms needing only O(log n) additional pointers are usually considered in-place algorithms.
Most selection algorithms are also in-place, although some considerably rearrange the input array in the process of finding the final, constant-sized
result.
Some text manipulation algorithms such as trim and reverse may be done in-place.

##You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

#Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

#Example 2:
Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

#Constraints:
n == matrix.length == matrix[i].length
1 <= n <= 20
-1000 <= matrix[i][j] <= 1000

### Testcase:
---
[[1,2,3],[4,5,6],[7,8,9]]
[[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]

### Code:
---
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        '''
        Do not return anything, modify matrix in-place instead.
        '''

"""
### Solution: -----------------------------------------------------------------------------------------------
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        
        # Step 1: Transpose the matrix
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # Step 2: Reverse each row
        for i in range(n):
            matrix[i] = matrix[i][::-1]


# Description: ----------------------------------------------------------------------------------------------
'''
To rotate a given n x n 2D matrix by 90 degrees clockwise in place, we can perform the following steps:

1. Transpose the matrix: Swap the elements of the matrix such that the rows become columns and vice versa. This operation effectively 
   rotates the matrix by 90 degrees counterclockwise.

2. Reverse each row: After transposing the matrix, reverse each row to get the final result, which is a 90-degree clockwise rotation 
   of the original matrix.

This solution directly modifies the input 2D matrix in place, as required by the problem statement. It first transposes the matrix and 
then reverses each row to achieve the 90-degree clockwise rotation.

**Time Complexity:** 
The time complexity of this solution is O(n^2), where n is the number of rows (or columns) in the matrix. This is because we visit each 
element of the matrix exactly once during the transpose operation and once again during the row reversal operation.

'''
