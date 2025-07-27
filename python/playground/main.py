from typing import List, Optional

# Utils
# ┌─────┐     ┌─────┐     ┌─────┐
# │ val │ →→→ │ val │ →→→ │ val │
# │  1  │     │  2  │     │  3  │
# └─────┘     └─────┘     └─────┘
# A linked list is a data structure in which elements (called nodes) are connected in sequence, with each node pointing to the next one.
# It may look similar to Python’s built-in list [], but it allows for faster insertion and deletion operations, and it works even when the nodes are scattered in memory.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        """String representation for easy debugging"""
        result = []
        current = self
        while current:
            result.append(str(current.val))
            current = current.next
        return " -> ".join(result)

# 1 => xxoooo
class TwoSum:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        return False

# 9 => ooo
class Palindrome:
    def isPalindrome(self, x: int) -> bool:
        return False

# 13 => xx
class RomanToInteger:
    def romanToInt(self, s: str) -> int:
        roman_map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        return False

# 14 => x
class LongestCommonPrefix:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        return False

# 15
class ValidParentheses:
    def isValid(self, s: str) -> bool:
        return False

# 21 -> x
class MergeTwoSortedList:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        return False

# 26 ->
class RemoveDuplicatesFromSortedArray:
    def removeDuplicates(self, nums: List[int]) -> int:
        return False

# 27 => xx
class RemoveElement:
    def removeElement(self, nums: List[int], val: int) -> int:
        return False

# 28 => ooo
class FindTheIndexOfTheFirst:
    def strStr(self, haystack: str, needle: str) -> int:
        return False

# 35 => oxo
class SearchInsertPosition:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return False

def test_two_sum():
    sol = TwoSum()

    nums1 = [2, 7, 11, 15]
    target1 = 9
    result1 = sol.twoSum(nums1, target1)
    print(f"Test 1: nums={nums1}, target={target1}")
    print(f"Result: {result1}")
    assert result1 == [0, 1] or result1 == [1, 0]


def test_palindrome():
    sol = Palindrome()

    # Test cases from the problem
    test_cases = [
        (121, True, "Basic palindrome"),
        (-121, False, "Negative number"),
        (10, False, "Ends with 0"),
        (0, True, "Single digit 0"),
        (1, True, "Single digit"),
        (1221, True, "Even length palindrome"),
        (12321, True, "Odd length palindrome"),
        (123, False, "Not a palindrome"),
        (1000021, False, "Large non-palindrome"),
        (1234321, True, "Large palindrome")
    ]

    print("=== Testing String Approach ===")
    for x, expected, description in test_cases:
        result1 = sol.isPalindrome(x)
        status1 = "✅ PASS" if result1 == expected else "❌ FAIL"
        print(f"Input: {x:>8} | Expected: {expected:>5} | Got: {result1:>5} | {status1} | {description}")

def test_roman_to_integer():
    test_cases = [
        ("III", 3),
        ("LVIII", 58),
        ("MCMXCIV", 1994),
        ("IV", 4),
        ("IX", 9),
        ("VX", 5),
        ("XL", 40),
        ("XC", 90),
        ("CD", 400),
        ("CM", 900)
    ]

    sol = RomanToInteger()
    for roman, expected in test_cases:
        result = sol.romanToInt(roman)
        status = "✓" if result == expected else "✗"
        print(f"{status} {roman:>8} = {result:>4} (expected: {expected})")

def test_longest_common_prefix():
    sol = LongestCommonPrefix()

    # Test case 1
    strs1 = ["flower", "flow", "flight"]
    result1 = sol.longestCommonPrefix(strs1)
    print(f"Input: {strs1}")
    print(f"Output: '{result1}'")
    print(f"Expected: 'fl'")
    print()

    # Test case 2
    strs2 = ["dog", "racecar", "car"]
    result2 = sol.longestCommonPrefix(strs2)
    print(f"Input: {strs2}")
    print(f"Output: '{result2}'")
    print(f"Expected: ''")
    print()

    # Additional test cases
    test_cases = [
        [""],
        ["a"],
        ["abc", "abc", "abc"],
        ["abcdef", "abc", "abcd"],
        ["", "abc"],
        ["abc", ""]
    ]

    print("Additional test cases:")
    for i, strs in enumerate(test_cases, 3):
        result = sol.longestCommonPrefix(strs)
        print(f"Test {i}: {strs} -> '{result}'")

def test_remove_duplicates():
    """Test the function with various cases."""
    sol = RemoveDuplicatesFromSortedArray()

    test_cases = [
        ([1, 1, 2], 2, [1, 2]),
        ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5, [0, 1, 2, 3, 4]),
        ([1], 1, [1]),
        ([1, 1, 1], 1, [1]),
        ([1, 2, 3, 4, 5], 5, [1, 2, 3, 4, 5]),
        ([1, 1, 2, 2, 3, 3], 3, [1, 2, 3]),
        ([-1, 0, 0, 0, 3, 3], 3, [-1, 0, 3])
    ]

    print("Testing Remove Duplicates from Sorted Array:")
    print("=" * 70)
    print(f"{'Input':<25} {'Expected K':<12} {'Result K':<10} {'First K Elements':<20} {'Status'}")
    print("=" * 70)

    for original_nums, expected_k, expected_unique in test_cases:
        # Test main solution
        nums = original_nums.copy()  # Don't modify original
        result_k = sol.removeDuplicates(nums)
        result_unique = nums[:result_k]

        status = "✓" if result_k == expected_k and result_unique == expected_unique else "✗"

        print(f"{str(original_nums):<25} {expected_k:<12} {result_k:<10} "
              f"{str(result_unique):<20} {status}")

    print("=" * 70)

def test_remove_element():
    sol = RemoveElement()

    # Test Case 1
    nums1 = [3, 2, 2, 3]
    val1 = 3
    k1 = sol.removeElement(nums1, val1)
    print(f"Test 1: nums = {nums1[:k1]}, k = {k1}")
    assert k1 == 2
    assert sorted(nums1[:k1]) == [2, 2]

def test_find_the_index_of_the_first():
    sol = FindTheIndexOfTheFirst()

    haystack1 = "sadbutsad"
    needle1 = "sad"
    result1 = sol.strStr(haystack1, needle1)
    print(f"Test 1: haystack='{haystack1}', needle='{needle1}' -> {result1}")
    assert result1 == 0

def test_search_insert_position():
    sol = SearchInsertPosition()

    # Test case 1: target found
    nums1 = [1, 3, 5, 6]
    target1 = 5
    result1 = sol.searchInsert(nums1, target1)
    print(f"nums = {nums1}, target = {target1}")
    print(f"Output: {result1}")
    print(f"Expected: 2")
    print()

    # Test case 2: target not found, insert in middle
    nums2 = [1, 3, 5, 6]
    target2 = 2
    result2 = sol.searchInsert(nums2, target2)
    print(f"nums = {nums2}, target = {target2}")
    print(f"Output: {result2}")
    print(f"Expected: 1")
    print()

if __name__ == "__main__":
    print("=" * 40)
    print("playground")
    print("=" * 40)

    # test_two_sum()
    # test_palindrome()
    # test_roman_to_integer()
    test_longest_common_prefix()

    # test_remove_duplicates()
    # test_remove_element()
    # test_find_the_index_of_the_first()
    # test_search_insert_position()