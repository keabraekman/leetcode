# Given an array of intervals intervals where intervals[i] = [starti, endi], 
# return the minimum number of intervals you need to remove to make the rest 
# of the intervals non-overlapping.

 

# Example 1:

# Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
# Output: 1
# Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.


def eraseOverlapIntervals(intervals):
    ans, intervals = 0, sorted(intervals, key=lambda x:x[0])
    for i in range(len(intervals)-1):
        if intervals[i][1] > intervals[i+1][0]:
            ans += 1
            if intervals[i][1] < intervals[i+1][1]:
                intervals[i+1] = intervals[i]
    return ans

intervals = [[1,2],[2,3],[3,4],[1,3],[3,8]]
print(eraseOverlapIntervals(intervals))