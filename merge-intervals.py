# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
# and return an array of the non-overlapping intervals that cover all the intervals in the input.

# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

def merge(intervals):
    # Sort the intervals by their first values (smallest)
    intervals.sort(key = lambda i : i[0])
    # Initialize the result array with the first interval
    result = [intervals[0]]
    # start and end in intervals. Linear for loop
    for start, end in intervals[1:]:
        # Last end is the previous end
        lastEnd = result[-1][1]
        # If they overlap, 
        # the last end of result will be the max between lastEnd and the new end
        if start <= lastEnd:
            result[-1][1] = max(lastEnd, end)
        # If they don't overlap, 
        # Append the new interval. 
        else:
            result. append([start, end])
    return result

















def twoIntervals(i1, i2):
    if i1[1] < i2[0]:
        return [i1, i2]
    else:
        if i1[0] < i2[0]:
            if i1[1] < i2[1]:
                return [i1[0], i2[1]]
            else:
                return i1
        else:
            if i1[1] < i2[1]:
                return i2
            else:
                return [i2[0], i1[1]]







def merge2(intervals):
    intervals = sorted(intervals, key = lambda x:x[0])
    result = [intervals[0]]
    for start, end in intervals[1:]:
        lastEnd = result[-1][1]
        if start > lastEnd:
            result.append([start, end])
        else:
            result[-1][1] = max(lastEnd, end)
    return result


intervals = [[1,3],[2,6],[8,10],[15,18]]
intervals = [[1,4],[2,3]]
print(merge2(intervals))