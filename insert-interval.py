# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].


# case 1 : if it doesn't overlap
# Case 2 : If it does overlap
def insert(intervals, newInterval):
    if intervals[-1][1] < newInterval[0]:
        intervals.append(newInterval)
        return intervals
    for i in range(len(intervals)-1):
        if intervals[i][1] < newInterval[0] and intervals[i+1][0] > newInterval[1]:
            intervals.insert(i+1, newInterval)
            return intervals
    
    # If it does overlap : 
    result = []
    for i in range(len(intervals)):
        if intervals[i][0] < newInterval[0] and intervals[i][1] > newInterval[0]:
            start = intervals[i][0]
            index = i
            break
        else:
            result.append(intervals[i])

    tempEnd = intervals[index][1]
    while tempEnd < newInterval[1] and index < len(intervals)-1:
        index += 1
        tempEnd = intervals[index][1]

        if intervals[index][0] > newInterval[1]:
            tempEnd = newInterval[1]
            # break
        if intervals[index][0] < newInterval[1]:
            tempEnd = newInterval[1]
            # index -= 1
            # break
        else:
            tempEnd = intervals[index][1]
        
        index += 1
    result_interval = [start, tempEnd]

    result.append(result_interval)

    for i in range(index, len(intervals)):
        result.append(intervals[i])
    return result






def insert(intervals, newInterval):
    if not intervals:
        return [newInterval]
    if intervals[-1][1] < newInterval[0]:
        intervals.append(newInterval)
        return intervals
    for i in range(len(intervals)-1):
        if intervals[i][1] < newInterval[0] and intervals[i+1][0] > newInterval[1]:
            intervals.insert(i+1, newInterval)
            return intervals

    result = []
    index = 0
    start = intervals[0][0]
    for i in range(len(intervals)):
        if intervals[i][0] < newInterval[0] and intervals[i][1] > newInterval[0]:
            start = intervals[i][0]
            index = i
            break
        else:
            result.append(intervals[i])
    while newInterval[1] > intervals[index][1] and index < len(intervals)-1:
        index += 1
    if newInterval[1] >= intervals[index][0]:
        end = max(intervals[index][1], newInterval[1])
        result.append([start, end])
    else:
        end = newInterval[1]
        result.append([start, end])
        result.append(intervals[index])
    for i in range(index+1, len(intervals)):
        result.append(intervals[i])
    return result


def overlap(i1, i2):
    if i1[1] < i2[0] or i1[0] > i2[1]:
        return False
    else:
        return True

def insert(intervals, newInterval):
    result = []
    for i in range(len(intervals)):
        if newInterval[1] < intervals[i][0]:
            result.append(newInterval)
            return result + intervals[i:]
        elif newInterval[0] > intervals[i][1]:
            result.append(intervals[i])
        else:
            newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
    result.append(newInterval)
    return result



# intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
# newInterval = [4,8]
# print(insert(intervals, newInterval))
# intervals = [[1,3],[6,9]]
# newInterval = [2,5]
# print(insert(intervals, newInterval))
# intervals = [[1,5]]
# newInterval = [2,7]
# print(insert(intervals, newInterval))









def insert(intervals, newInterval):
    ans = []
    for i in range(len(intervals)):
        if newInterval[1] < intervals[i][0]:
            ans.append(newInterval)
            return ans + intervals[i:]
        elif newInterval[0] > intervals[i][1]:
            ans.append(intervals[i])
        else:
            newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
    ans.append(newInterval)
    return ans

# intervals = [[1,5]]
# newInterval = [6,8]



















def insert(intervals, newInterval):
    ans = []
    for i in range(len(intervals)):
        if newInterval[1] < intervals[i][0]:
            ans.append(newInterval)
            return ans + intervals[i:]
        elif newInterval[0] > intervals[i][1]:
            ans.append(intervals[i])
        else:
            newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
    ans.append(newInterval)
    return ans











intervals = [[1,3],[6,9]]
newInterval = [2,5]

print(insert(intervals, newInterval))