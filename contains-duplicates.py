# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

def containsDuplicate(nums):
    visited = dict()
    for n in nums:
        if n in visited:
            return False
        else:
            visited[n] = n
    return True


def containsDuplicate(nums):
    return len(nums) != len(set(nums))