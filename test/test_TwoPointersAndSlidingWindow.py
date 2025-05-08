import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from TwoPointersAndSlidingWindow import longest_substring, minSubArrayLen, maxArea, findAnagrams, permutation, miniSubstring
def test_longest_substring_examples():
    assert longest_substring("abcabcbb") == 3
    assert longest_substring("bbbbb") == 1
    assert longest_substring("pwwkew") == 3

def test_longest_substring_edge_cases():
    assert longest_substring("") == 0
    assert longest_substring(" ") == 1
    assert longest_substring("au") == 2

def test_minSubArrayLen_examples():
    assert minSubArrayLen([2,3,1,2,4,3], 7) == 2
    assert minSubArrayLen([1,4,4],1) == 1
    assert minSubArrayLen([1,1,1,1,1,1,1,1], 11) == 0

def test_minSubArrayLen_edge_cases():
    assert minSubArrayLen([5], 5) == 1
    assert minSubArrayLen([1]*99 + [100], 100) == 1

def test_maxArea_examples():
    assert maxArea([1,8,6,2,5,4,8,3,7]) == 49
    assert maxArea([1,1]) == 1

def test__maxArea_edge_cases():
    assert maxArea([1,2,4,3]) == 4
    assert maxArea([2,3,4,5,18,17,6]) == 17

def test_findAnagrams_examples():
    assert findAnagrams("cbaebabacd", "abc") == [0, 6]
    assert findAnagrams("abab", "ab") == [0, 1, 2]

def test_findAnagrams_edge_cases():
    assert findAnagrams("a", "a") == [0]
    assert findAnagrams("a", "b") == []
    assert findAnagrams("", "abc") == []

def test_permutation_examples():
    assert permutation("ab", "eidbaooo") == True
    assert permutation("ab", "eidboaoo") == False

def test_permutation_edge_cases():
    assert permutation("a", "a") == True
    assert permutation("abc", "bbbca") == True
    assert permutation("abc", "bbbcc") == False

def test_miniSubstring_examples():
    assert miniSubstring("ADOBECODEBANC", "ABC") == "BANC"
    assert miniSubstring("a", "a") == "a"
    assert miniSubstring("a", "aa") == ""

def test_miniSubstring_edge_cases():
    assert miniSubstring("aa", "aa") == "aa"
    assert miniSubstring("ab", "b") == "b"