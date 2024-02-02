# 1291. Sequential Digits.


# Topic: Enumeration

"""
### Task:
---
An integer has sequential digits if and only if each digit in the number is one more than the previous digit.

Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.


Example 1:
Input: low = 100, high = 300
Output: [123,234]

Example 2:
Input: low = 1000, high = 13000
Output: [1234,2345,3456,4567,5678,6789,12345]
 
Constraints:
10 <= low <= high <= 10^9

Hint 1:
Generate all numbers with sequential digits and check if they are in the given range.
Hint 2:
Fix the starting digit then do a recursion that tries to append all valid digits.


### Testcase:
---
100
300
1000
13000


### Code:
---
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        
    
"""
### Solution: --------------------------------------

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        seq_digits = []  # Initialize an empty list to store the sequential digit numbers.

        # Determine the length of 'low' and 'high' to understand the range of number lengths we need to consider.
        low_len = len(str(low))
        high_len = len(str(high))

        # Loop through each possible length of sequential digit numbers within the range of 'low_len' to 'high_len'.
        for length in range(low_len, high_len + 1):
            # Start the first digit of the number from 1 to 9.
            for start in range(1, 10):
                num = 0  # Initialize 'num' to build the sequential digit number.
                # Generate a sequential digit number of 'length' digits starting with 'start'.
                for i in range(length):
                    digit = start + i  # Calculate the next digit in the sequence.
                    if digit > 9:  # If the next digit exceeds 9, break as we can't have a digit more than 9.
                        break
                    num = num * 10 + digit  # Append the digit to 'num' to form the sequential number.

                # If the generated number is within the range [low, high], add it to the list.
                if low <= num <= high:
                    seq_digits.append(num)

                # If 'num' has reached or exceeded 'high' or if the next digit would be more than 9, stop the loop.
                if num >= high or digit > 9:
                    break

        return seq_digits  # Return the list of sequential digit numbers within the range.




### Description: ===================================
'''
To solve the issue of finding numbers with sequential digits within a specific range \([low, high]\), 
we need a direct and efficient method. The concept of sequential digits means each digit in a number is 
followed by its immediate successor, making a series like 123 or 456. 

### Algorithm for Generating Sequential Digit Numbers:

1. **Understanding Sequential Digits**:
   Sequential digits in a number imply a consecutive increment in each digit. Numbers such as 123, 456, and 789 
   are examples of such patterns where each digit is one more than the preceding one.

2. **Efficient Generation of Sequential Digits**:
   The process begins by determining the length of the lowest and highest numbers in the range, using these lengths 
   to control the generation of sequential digit numbers. This ensures that numbers are constructed with appropriate 
   lengths right from the start, thereby maintaining an inherent order and efficiency.

3. **Iterative Number Construction**:
   For each possible length within the determined range, numbers are constructed by starting from each digit (1 to 9) 
   and sequentially adding subsequent digits. The process is carefully controlled to prevent exceeding the digit limit 
   (9) and to ensure that numbers beyond the upper limit (`high`) are not unnecessarily generated.

4. **Range Filtering and Immediate Validation**:
   As numbers are generated, they are immediately checked to ensure they fall within the specified range \([low, high]\). 
   This real-time validation efficiently filters out ineligible numbers, streamlining the process.

5. **Direct Inclusion in the Result Set**:
   Valid numbers that meet the criteria are directly added to the result list, eliminating the need for post-generation 
   sorting. This approach not only simplifies the process but also ensures that the output is ready for immediate use.


### Key Advantages of the Revised Approach:

- **Efficiency**: By tailoring the generation process to the specific lengths of the lower and upper bounds, the algorithm 
    becomes more efficient, avoiding the generation of numbers outside the desired range.

- **Inherent Sorting**: The algorithm inherently maintains an ascending order, negating the need for an explicit sorting step 
    and thus enhancing performance.

- **Direct Filtering**: Immediate validation of each generated number against the given range ensures that only eligible 
    numbers are included, further optimizing the process.

    
This refined approach offers a more streamlined and efficient solution to identifying sequential digit numbers within a 
specified range, ensuring that the output is both accurate and optimally generated.

'''
