import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from BitManipulation import single_number, missing_number, missing_number_bit, find_difference
def test_single_number_basic():
    assert single_number([2, 2, 1]) == 1

def test_single_number_mixed():
    assert single_number([4, 1, 2, 1, 2]) == 4

def test_single_number_negative():
    assert single_number([-1, -1, -2]) == -2

def test_single_number_large():
    assert single_number([10**6, 1, 1]) == 10**6

def test_single_number_only_one():
    assert single_number([42]) == 42

def test_missing_number_basic():
    assert missing_number([3, 0, 1]) == 2

def test_missing_number_all_present():
    assert missing_number([0, 1, 2, 3, 4]) == 5

def test_missing_number_zero_missing():
    assert missing_number([1, 2, 3]) == 0

def test_missing_number_bit_basic():
    assert missing_number_bit([3, 0, 1]) == 2

def test_missing_number_bit_all_present():
    assert missing_number_bit([0, 1, 2, 3, 4]) == 5

def test_missing_number_bit_zero_missing():
    assert missing_number_bit([1, 2, 3]) == 0

def test_find_difference_example():
    assert find_difference("abcd", "abcde") == "e"

def test_find_difference_last_letter_missing():
    assert find_difference("a", "aa") == "a"

def test_find_difference_middle_letter():
    assert find_difference("xyz", "xayz") == "a"