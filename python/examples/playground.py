from typing import List, Optional

# Utils
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


# 1
class TwoSum:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        return False

# 9
class Palindrome:
    def isPalindrome(self, x: int) -> bool:
        return False

# 13
class RomanToInteger:
    def romanToInt(self, s: str) -> int:
        return False

# 14
class LongestCommonPrefix:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        return False

# 15
class ValidParentheses:
    def isValid(self, s: str) -> bool:
        return False

# 21
class MergeTwoSortedList:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        return False


# 26
class RemoveDuplicatesFromSortedArray:
    def removeDuplicates(self, nums: List[int]) -> int:
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
        # ("III", 3),
        # ("LVIII", 58),
        # ("MCMXCIV", 1994),
        ("IV", 4),
        ("IX", 9),
        # ("XL", 40),
        # ("XC", 90),
        # ("CD", 400),
        # ("CM", 900)
    ]

    sol = RomanToInteger()
    for roman, expected in test_cases:
        result = sol.romanToInt(roman)
        status = "✓" if result == expected else "✗"
        print(f"{status} {roman:>8} = {result:>4} (expected: {expected})")

if __name__ == "__main__":
    print("playground")
    # test_two_sum()
    # test_palindrome()
