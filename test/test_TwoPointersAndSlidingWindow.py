import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from TwoPointersAndSlidingWindow import longest_substring, minSubArrayLen
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