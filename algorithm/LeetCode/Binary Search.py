


# Binary Search is generally composed of 3 main sections:
# Pre-processing - Sort if collection is unsorted.
# Binary Search - Using a loop or recursion to divide search space in half after each comparison.
# Post-processing - Determine viable candidates in the remaining space.

# Distinguishing Syntax:
# Initial Condition: left = 0, right = length-1
# Termination: left > right
# Searching Left: right = mid-1
# Searching Right: left = mid+1


def binarySearch(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if len(nums) == 0:
        return -1

    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    # End Condition: left > right
    return -1