# Given an array of meeting time intervals intervals where 
# intervals[i] = [starti, endi], return the minimum number of 
# conference rooms required.
# Example 1:

# Input: intervals = [[0,30],[5,10],[15,20]]
# Output: 2

def minMeetingRooms(intervals):
    overlaps, ans, times = 0,1, []
    for i in range(len(intervals)):
        times.append([intervals[i][0], True])
        times.append([intervals[i][1], False])
    times.sort()
    for i in range(len(times)):
        if times[i][1]:
            overlaps += 1
        else:
            overlaps -= 1
        ans = max(ans, overlaps)
    return ans

intervals = [[0,30],[5,10],[15,20]]

print(minMeetingRooms(intervals))