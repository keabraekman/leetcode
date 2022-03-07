# Given an array of meeting time intervals where intervals[i] = [starti, endi], determine if a person could attend all meetings.

 

# Example 1:

# Input: intervals = [[0,30],[5,10],[15,20]]
# Output: false


def canAttendMeetings(intervals):
    intervals = sorted(intervals, key=lambda x:x[0])
    for i in range(len(intervals)-1):
        if intervals[i][1] > intervals[i+1][0]:
            return False
    return True