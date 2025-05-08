# Two Sum II, Move Zeroes, Longest Substring Without Repeating Characters, Max Sliding Window
# Leetcode 209, 11, 438, 567, 76

# Leetcode 3: Longest Substring Without Repeating Characters
#set - Set items are unordered, unchangeable, and do not allow duplicate values.
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
# min mark need to use float("inf") -  positive infinity in Python
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

# leetcode 11
# two points with while loop - compare each left element and each right element: while left<right
def maxArea(height):
    '''
    You are given an integer array height of length n.
    There are n vertical lines such that the two endpoints 
    of the i-th line are (i, 0) and (i, height[i]).
    >>> maxArea([1,8,6,2,5,4,8,3,7])
    >>> 49
    '''
    left = 0
    max_area = 0
    right = len(height) - 1

    while left < right:
        h = min(height[left], height[right])
        max_area = max((right-left) *h, max_area)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_area

# leetcode 438
# compare two dictionaries to make the same length of windows
def findAnagrams(s, p):
    '''
    Given two strings s and p, return all the start indices of p's anagrams in s.
    You may return the answer in any order. s and p consist of lowercase English letters.
    >>> findAnagrams("cbaebabacd", "abc")
    >>> [0, 6]
    '''
    result = []
    len_p = len(p)
    len_s = len(s)
    if len_p > len_s:
        return []

    dict_s = {}
    dict_p = {}
    for i in range(len_p):
        dict_s[s[i]] = dict_s.get(s[i], 0) + 1
        dict_p[p[i]] = dict_p.get(p[i], 0) + 1
        

    if dict_s == dict_p:
        result.append(0)
    

    for i in range(len_p, len_s):
        dict_s[s[i]] = dict_s.get(s[i], 0) + 1
        dict_s[s[i - len_p]] -= 1

        if dict_s[s[i-len_p]] == 0:
            del dict_s[s[i-len_p]]
        
        if dict_s == dict_p:
            result.append(i - len_p + 1)
    return result

# leetcode 567
def permutation(s1, s2):
    '''
    Given two strings s1 and s2, return True if s2 contains a permutation of s1, or False otherwise.
    In other words, check if one of s1's permutations is a substring of s2.
    >>> permutation("ab", "eidbaooo")
    >>> True

    >>> permutation("ab", "eidboaoo")
    >>> False
    '''
    len_s1 = len(s1)
    len_s2 = len(s2)
    if len_s1 > len_s2:
        return False

    dict_s1 = {}
    dict_s2 = {}
    for i in range(len_s1):
        dict_s1[s1[i]] = dict_s1.get(s1[i], 0) + 1
        dict_s2[s2[i]] = dict_s2.get(s2[i], 0) + 1
        
    if dict_s1 == dict_s2:
        return True
    

    for i in range(len_s1, len_s2):
        dict_s2[s2[i]] = dict_s2.get(s2[i], 0) + 1
        dict_s2[s2[i - len_s1]] -= 1

        if dict_s2[s2[i-len_s1]] == 0:
            del dict_s2[s2[i-len_s1]]
        
        if dict_s1 == dict_s2:
            return True
    return False

# leetcode 76
def miniSubstring(s, t):
    '''
    Given two strings s and t of lengths m and n respectively, 
    return the minimum window in s which contains all the characters of t.
    If there is no such window in s, return the empty string ""
    >>> miniSubstring("ADOBECODEBANC", "ABC")
    >>> "BANC"
    '''
    if not s or not t or len(s) < len(t):
        return ""
    if s == t:
        return s
    
    len_s = len(s)
    len_t = len(t)

    dict_min = {}
    dict_t = {}

    left = 0
    have = 0
    res = ""
    
    min_len = float("inf")
    
    for i in range(len_t):
        dict_t[t[i]] = dict_t.get(t[i], 0) + 1


    for right in range(len_s):
        char = s[right]
        dict_min[char] = dict_min.get(char, 0) + 1
        
        if char in dict_t and dict_t[char] == dict_min[char]:
            have += 1
        
        while have == len_t:
            min_len =min(min_len,right - left + 1)
            res = s[left:right + 1]

            dict_min[s[left]] -= 1
            if s[left] in dict_t and dict_min[s[left]] < dict_t[s[left]]:
                have -= 1
            left += 1
    return res




if __name__ == "__main__":
    print(minSubArrayLen([2,3,1,2,4,3], 7))
    print(maxArea([1,8,6,2,5,4,8,3,7]))
    print(findAnagrams("cbaebabacd", "abc"))
    print(permutation("ab", "eidbaooo"))
    print(permutation("ab", "eidboaoo"))
    print(miniSubstring("ADOBECODEBANC", "ABC"))
    print( miniSubstring("a", "aa"))
    print(miniSubstring("aa", "aa"))