# Binary Search, Merge Sort, Quick Sort, Search in Rotated Array
#Leetcode 704, 35, 278, 34, 88

#Leetcode 33: Search in Rotated Sorted Array
def search(nums, target):
    '''
    There is an integer array nums sorted
    in ascending order (with distinct values).
    Prior to being passed to your function, 
    nums is possibly rotated at an unknown pivot 
    index k (1 <= k < nums.length) such that the 
    resulting array is 
    [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
    For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
    Given the array nums after the possible rotation and an integer target,
    return the index of target if it is in nums, or -1 if it is not in nums.
    
    You must write an algorithm with O(log n) runtime complexity.
    >>> Search([4,5,6,7,0,1,2], 0)
    >>> 4

    >>> Search([4,5,6,7,0,1,2], 3)
    >>> -1

    >>> Search([1], 0)
    >>> -1
    '''
    
    mid = len(nums)//2
    if target == nums[mid]:
        return mid
    if target > nums[mid]:
        for i in mid:
            return