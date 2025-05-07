#set - Set items are unordered, unchangeable, and do not allow duplicate values.
# min mark need to use float("inf") -  positive infinity in Python


# Two Sum II, Move Zeroes, Longest Substring Without Repeating Characters, Max Sliding Window
# Leetcode 209, 11, 438, 567, 76
# Leetcode 3: Longest Substring Without Repeating Characters
def longest_substring(s):
    '''
    Given a string s, find the length of the longest substring without repeating characters.

    >>> longest_substring("abcabcbb")
    >>> 3

    >>> longest_substring("bbbbb")
    >>> 1

    >>> longest_substring("pwwkew")
    >>> 3
    '''
    seen = set()
    left = 0
    max_len = 0
    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        max_len = max(max_len, right - left + 1)
    return max_len
        
# leetcode 209
def minSubArrayLen(nums, target):
    '''
    Given an array of positive integers nums and a positive integer target,
    return the minimal length of a subarray whose sum is greater than or equal to target. 
    If there is no such subarray, return 0 instead.
    >>> minSubArrayLen([2,3,1,2,4,3], 7)
    >>> 2

    >>> minSubArrayLen([1,4,4], 4)
    >>> 1

    >>> minSubArrayLen([1,1,1,1,1,1,1,1], 11)
    >>> 0
    '''
    min_len = float('inf')
    left = 0
    total = 0
    for right in range(len(nums)):
        total += nums[right]
        while total >= target:
            min_len= min(min_len, right - left + 1)
            total -= nums[left]
            left += 1
    return min_len if min_len != float('inf') else 0

if __name__ == "__main__":
    print(minSubArrayLen([2,3,1,2,4,3], 7))