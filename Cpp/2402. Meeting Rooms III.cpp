// 2402. Meeting Rooms III.


// Topic: Array, Hash Table, Sorting, Heap (Priority Queue), Simulation.


/*
### Task:
---
You are given an integer n. There are n rooms numbered from 0 to n - 1.

You are given a 2D integer array meetings where meetings[i] = [starti, endi] means that a meeting will be held during the half-closed time interval [starti, endi). All the values of starti are unique.

Meetings are allocated to rooms in the following manner:

    1. Each meeting will take place in the unused room with the lowest number.
    2. If there are no available rooms, the meeting will be delayed until a room becomes free. The delayed meeting should have the same duration as the original meeting.
    3. When a room becomes unused, meetings that have an earlier original start time should be given the room.

Return the number of the room that held the most meetings. If there are multiple rooms, return the room with the lowest number.

A half-closed interval [a, b) is the interval between a and b including a and not including b.

Example 1:
Input: n = 2, meetings = [[0,10],[1,5],[2,7],[3,4]]
Output: 0
Explanation:
- At time 0, both rooms are not being used. The first meeting starts in room 0.
- At time 1, only room 1 is not being used. The second meeting starts in room 1.
- At time 2, both rooms are being used. The third meeting is delayed.
- At time 3, both rooms are being used. The fourth meeting is delayed.
- At time 5, the meeting in room 1 finishes. The third meeting starts in room 1 for the time period [5,10).
- At time 10, the meetings in both rooms finish. The fourth meeting starts in room 0 for the time period [10,11).
Both rooms 0 and 1 held 2 meetings, so we return 0. 

Example 2:
Input: n = 3, meetings = [[1,20],[2,10],[3,5],[4,9],[6,8]]
Output: 1
Explanation:
- At time 1, all three rooms are not being used. The first meeting starts in room 0.
- At time 2, rooms 1 and 2 are not being used. The second meeting starts in room 1.
- At time 3, only room 2 is not being used. The third meeting starts in room 2.
- At time 4, all three rooms are being used. The fourth meeting is delayed.
- At time 5, the meeting in room 2 finishes. The fourth meeting starts in room 2 for the time period [5,10).
- At time 6, all three rooms are being used. The fifth meeting is delayed.
- At time 10, the meetings in rooms 1 and 2 finish. The fifth meeting starts in room 1 for the time period [10,12).
Room 0 held 1 meeting while rooms 1 and 2 each held 2 meetings, so we return 1. 

Constraints:
1 <= n <= 100
1 <= meetings.length <= 10^5
meetings[i].length == 2
0 <= starti < endi <= 5 * 10^5
All the values of starti are unique.

### Testcase:
---
2
[[0,10],[1,5],[2,7],[3,4]]
3
[[1,20],[2,10],[3,5],[4,9],[6,8]]


### Code:
---
class Solution {
public:
    int mostBooked(int n, vector<vector<int>>& meetings) {
        
    }
};


*/
// Solution: ------------------------------------------------------------------------------------------------------------


class Solution {
public:
    int mostBooked(int n, vector<vector<int>>& meetings) {
        sort(meetings.begin(), meetings.end()); // Step 1

        priority_queue<int, vector<int>, greater<int>> availableRooms; // Step 2
        for (int i = 0; i < n; ++i) availableRooms.push(i);

        priority_queue<pair<long, int>, vector<pair<long, int>>, greater<pair<long, int>>> ongoingMeetings; // Step 3
        vector<int> meetingCount(n, 0); // Step 4

        for (auto& meeting : meetings) {
            long start = meeting[0], end = meeting[1];

            // Free up rooms that are now available
            while (!ongoingMeetings.empty() && ongoingMeetings.top().first <= start) {
                availableRooms.push(ongoingMeetings.top().second);
                ongoingMeetings.pop();
            }

            // Allocate room for the current meeting
            if (!availableRooms.empty()) {
                int room = availableRooms.top();
                availableRooms.pop();
                meetingCount[room]++;
                ongoingMeetings.push({end, room});
            } else {
                // Wait for the next room to become available
                auto nextAvailable = ongoingMeetings.top();
                ongoingMeetings.pop();
                meetingCount[nextAvailable.second]++;
                ongoingMeetings.push({nextAvailable.first + (end - start), nextAvailable.second});
            }
        }

        // Step 6: Find the room with the most meetings
        int maxMeetings = 0, resultRoom = 0;
        for (int i = 0; i < n; ++i) {
            if (meetingCount[i] > maxMeetings) {
                maxMeetings = meetingCount[i];
                resultRoom = i;
            }
        }

        return resultRoom;
    }
};


// Description: ====================================================================================================================
/*
To solve the "Meeting Rooms III" problem, we need to simulate the allocation of meetings to rooms while keeping track of the number 
of meetings each room holds. The goal is to return the room number that held the most meetings, with ties broken by the lowest room 
number. This problem can be efficiently solved using a priority queue (heap) for managing room availability and sorting the meetings 
based on their start times.

### Approach:

1. **Sort Meetings**: Sort the `meetings` array based on the start time of each meeting to process them in chronological order.

2. **Available Rooms Queue**: Use a priority queue (min-heap) to keep track of available rooms. Initially, all rooms are available and 
     are pushed into this queue.

3. **Ongoing Meetings Queue**: Use another priority queue to keep track of ongoing meetings. This queue will store pairs consisting of 
     the meeting end time and the room number. This queue is sorted by the end time to ensure the earliest finishing meeting is processed 
     first.

4. **Room Counters**: Maintain an array to count the number of meetings held in each room.

5. **Simulation**: Iterate through the sorted meetings. For each meeting, free up any rooms that have become available by the meeting's 
     start time and update the available rooms queue. If there are available rooms, allocate the current meeting to the room with the 
     lowest number. If not, wait for the next room to become available, adjust the meeting's end time to reflect the delay, and then 
     allocate it.

6. **Find the Room with Most Meetings**: After processing all meetings, iterate through the room counters to find the room that held the 
     most meetings. If there's a tie, the room with the lowest number is chosen.

### Explanation:

- The `availableRooms` priority queue keeps track of the rooms that are currently available, sorted by room number.
- The `ongoingMeetings` priority queue keeps track of meetings currently in progress, sorted by their end times.
- The `meetingCount` array counts how many meetings each room has hosted.
- During the simulation, we allocate meetings to rooms based on availability and update the end times for delayed meetings.
- Finally, we find the room with the most meetings hosted and return its number.

*/
