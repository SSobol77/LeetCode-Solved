"""
# 981. Time Based Key-Value Store

# Topic: Hash Table, String, Binary Search, Design.

# Task:
-----------------
Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

Implement the TimeMap class:

    TimeMap() Initializes the object of the data structure.
    void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
    String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".

 

Example 1:

Input
["TimeMap", "set", "get", "get", "set", "get", "get"]
[[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
Output
[null, null, "bar", "bar", null, "bar2", "bar2"]

Explanation
TimeMap timeMap = new TimeMap();
timeMap.set("foo", "bar", 1);  // store the key "foo" and value "bar" along with timestamp = 1.
timeMap.get("foo", 1);         // return "bar"
timeMap.get("foo", 3);         // return "bar", since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".
timeMap.set("foo", "bar2", 4); // store the key "foo" and value "bar2" along with timestamp = 4.
timeMap.get("foo", 4);         // return "bar2"
timeMap.get("foo", 5);         // return "bar2"

Constraints:
1 <= key.length, value.length <= 100
key and value consist of lowercase English letters and digits.
1 <= timestamp <= 10^7
All the timestamps timestamp of set are strictly increasing.
At most 2 * 10^5 calls will be made to set and get.



# Testcase:
-----------------
["TimeMap","set","get","get","set","get","get"]
[[],["foo","bar",1],["foo",1],["foo",3],["foo","bar2",4],["foo",4],["foo",5]]


# Code:
-----------------
class TimeMap:

    def __init__(self):
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        

    def get(self, key: str, timestamp: int) -> str:
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)


"""
# Solution:

class TimeMap:
    def __init__(self):
        # Initialize a dictionary to store the key-value pairs.
        # Each key maps to a list of (timestamp, value) tuples.
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # If the key is not already in the store, initialize an empty list for it.
        if key not in self.store:
            self.store[key] = []
        # Append the (timestamp, value) pair to the list corresponding to the key.
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        # If the key is not present in the store, return an empty string.
        if key not in self.store:
            return ""

        # Retrieve the list of (timestamp, value) pairs for the key.
        values = self.store[key]
        # Initialize binary search bounds.
        left, right = 0, len(values) - 1

        # Perform binary search to find the right value for the given timestamp.
        # We want to find the largest timestamp that is less than or equal to the given timestamp.
        while left <= right:
            mid = left + (right - left) // 2
            if values[mid][0] <= timestamp:
                left = mid + 1
            else:
                right = mid - 1

        # If a valid timestamp is found, return the corresponding value.
        # If 'right' is -1, it means no suitable timestamp was found, so return an empty string.
        return values[right][1] if right >= 0 else ""



#-----------------------------------------------------------------------------------------------
# Description:
'''
To design a time-based key-value store for the given task, we can use a dictionary to map keys to 
lists of (timestamp, value) pairs. The set method will append new pairs to the list corresponding 
to a key, and the get method will use binary search to find the appropriate value for a given 
timestamp.

Explanation:

- Initialization (__init__): Initialize an empty dictionary store to hold the key-value pairs.

- Set Method (set): For each key, we maintain a list of (timestamp, value) pairs. When a new value is set 
  for a key, we append the (timestamp, value) pair to the list for that key.

- Get Method (get): To retrieve the value for a given key and timestamp, we perform binary search on the 
  list of (timestamp, value) pairs associated with the key. The goal is to find the largest timestamp that 
  is less than or equal to the given timestamp and return the corresponding value. If no such timestamp is
  found, we return an empty string.

Complexity Analysis:

1. Time Complexity:
- For set: O(1) for each call, as we are just appending to a list.
- For get: O(log n) for each call, where n is the number of entries for the key, due to the binary search.

2. Space Complexity: O(k * n), where k is the number of unique keys and n is the average number of entries 
   per key.

This solution efficiently handles the requirements of storing and retrieving values based on different 
timestamps using a combination of a hash table and binary search.

'''
