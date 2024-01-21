# 93. Restore IP Addresses

# Topic: String, Backtracking.

'''
# Task
--------
A valid IP address consists of exactly four integers separated by single dots. Each integer is between 0 and 255 (inclusive)
and cannot have leading zeros.

For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses, but "0.011.255.245", "192.168.1.312" and "192.168@1.1" 
are invalid IP addresses.
Given a string s containing only digits, return all possible valid IP addresses that can be formed by inserting dots 
into s. You are not allowed to reorder or remove any digits in s. You may return the valid IP addresses in any order.

Example 1:
Input: s = "25525511135"
Output: ["255.255.11.135","255.255.111.35"]

Example 2:
Input: s = "0000"
Output: ["0.0.0.0"]

Example 3:
Input: s = "101023"
Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]

Constraints:
1 <= s.length <= 20
s consists of digits only.


# Testcase:
-------------
"25525511135"
"0000"
"101023"


# Code:
---------------
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
     
'''
# Solution:
from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        # Check if the length of the string is not suitable for an IP address
        n = len(s)
        if n < 4 or n > 12:
            return []

        result = []

        # The first loop selects the end of the first segment (1 to 3 digits)
        for i in range(1, min(4, n - 2)):
            # The second loop selects the end of the second segment
            for j in range(i + 1, min(i + 4, n - 1)):
                # The third loop selects the end of the third segment
                for k in range(j + 1, min(j + 4, n)):
                    # Split the string into four parts based on the selected indices
                    s1, s2, s3, s4 = s[:i], s[i:j], s[j:k], s[k:]

                    # Check if all four segments are valid
                    if all(self.is_valid(segment) for segment in [s1, s2, s3, s4]):
                        # If valid, add the constructed IP to the result list
                        result.append(f"{s1}.{s2}.{s3}.{s4}")
        return result

    def is_valid(self, segment: str) -> bool:
        # Check if the segment is a valid IP address part:
        # 1. Length should be 1 to 3 characters
        # 2. Should not start with '0' unless it is '0'
        # 3. Should not be greater than 255
        return 0 < len(segment) <= 3 and (segment[0] != '0' or len(segment) == 1) and int(segment) <= 255

# Test cases
sol = Solution()
print(sol.restoreIpAddresses("25525511135"))  # ["255.255.11.135", "255.255.111.35"]
print(sol.restoreIpAddresses("0000"))         # ["0.0.0.0"]
print(sol.restoreIpAddresses("101023"))       # ["1.0.10.23", "1.0.102.3", "10.1.0.23", "10.10.2.3", "101.0.2.3"]

# Description:
'''
This code defines a Solution class with a method restoreIpAddresses to find all possible valid IP addresses that can be
formed from a given string. It uses three nested loops to generate all possible splits of the string into four parts, 
ensuring that each part is a valid segment of an IP address. The is_valid method is used to check the validity of each
segment. If all segments are valid, the segments are concatenated into an IP address and added to the result list. 
The solution is optimized for performance by reducing string operations and avoiding unnecessary recursive calls.

'''
