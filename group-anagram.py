# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]


# Start with sorting by number of letters
# Sort alphabetically
# If the word is duplicate, return the indexes

# return indices of anagrams in groups
def groupAnagrams(strs):
    answer = []
    sorted_strs = []
    indices_2d = []
    for i in range(len(strs)):
        sorted_strs.append(''.join(sorted(strs[i])))
    for i in range(len(sorted_strs)):
        indices_2d.append(indices(sorted_strs, sorted_strs[i]))

    unique_groups = remove_duplicates(indices_2d)
    for i in range(len(unique_groups)):
        group = []
        for j in range(len(unique_groups[i])):
            group.append(strs[unique_groups[i][j]])
        answer.append(group)
    return answer

# Groups the indices of anagrams
def indices(strs, value):
    list_indices = []
    for index, str in enumerate(strs):
        if str == value:
            list_indices.append(index)
    return list_indices

# removes duplicates from anagram indices groups
def remove_duplicates(indices):
    unique = []
    for i in range(len(indices)):
        if indices[i] not in unique:
            unique.append(indices[i])
    return unique
    


strs = ["eat","tea","tan","ate","nat","bat"]
# print(groupAnagrams(strs))



def groupAnagrams(strs):
    res, ordered = [], []
    for i in range(len(strs)):
        ordered.append([strs[i], i])
    for i in range(len(ordered)):
        ordered[i][0] = ''.join(sorted(ordered[i][0]))
    ordered.sort(key=lambda x:x[0])
    group = [strs[ordered[0][1]]]
    for i in range(1,len(ordered)):
        if ordered[i][0] == ordered[i-1][0]:
            group.append(strs[ordered[i][1]])
        else:
            res.append(group)
            group = [strs[ordered[i][1]]]
    res.append(group)
    return res

strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))