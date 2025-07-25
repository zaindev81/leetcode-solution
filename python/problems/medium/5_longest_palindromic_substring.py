# https://leetcode.com/problems/longest-palindromic-substring/
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        start = 0
        max_len = 1

        def expand_around_center(left: int, right: int) -> int:
            # Expand outward from center and return the length of palindrome
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1

        for i in range(len(s)):
            # Check for odd-length palindromes (center is a single character)
            len1 = expand_around_center(i, i)
            print("len1", len1)
            # Check for even-length palindromes (center is between two characters)
            len2 = expand_around_center(i, i + 1)
            print("len2", len2)

            # Select the longer palindrome
            current_max = max(len1, len2)

            if current_max > max_len:
                max_len = current_max
                # Calculate the starting position of the palindrome
                start = i - (current_max - 1) // 2

        return s[start:start + max_len]


# Example: "aba" → center is "b" (at index i = 1)
# Example: "abba" → center is between "b" and "b" (between index 1 and 2)


# expand_around_center(0, 0)
# | Step | `left` | `right` | `s[left]` | `s[right]` | Match? | Action                            |
# | ---- | ------ | ------- | --------- | ---------- | ------ | --------------------------------- |
# | 1    | 0      | 0       | `"b"`     | `"b"`      | ✅      | Expand → `left = -1`, `right = 1` |
# | 2    | -1     | 1       | —         | `"a"`      | ❌      | Exit loop                         |
# right - left - 1 = 1 - (-1) - 1 = 1


# expand_around_center(1, 1)
# | Step | `left` | `right` | `s[left]` | `s[right]` | Match? | Action                      |
# | ---- | ------ | ------- | --------- | ---------- | ------ | --------------------------- |
# | 1    | 1      | 1       | `"a"`     | `"a"`      | ✅      | Expand left → 0, right → 2  |
# | 2    | 0      | 2       | `"b"`     | `"b"`      | ✅      | Expand left → -1, right → 3 |
# | 3    | -1     | 3       | —         | `"a"`      | ❌      | Exit loop                   |
# right - left - 1 = 4 - 0 - 1 = 3


# "babad"
# | Index `i` | Center(s) | Odd-Length Palindrome | Even-Length Palindrome | Longer Length | Update `max_len`? | `start` |
# | --------- | --------- | --------------------- | ---------------------- | ------------- | ----------------- | ------- |
# | 0         | `"b"`     | `"b"` (len=1)         | —                      | 1             | ✅ `max_len = 1`   | 0       |
# | 1         | `"a"`     | `"bab"` (len=3)       | —                      | 3             | ✅ `max_len = 3`   | 0       |
# | 2         | `"b"`     | `"aba"` (len=3)       | —                      | 3             | ❌ (no change)     | 0       |
# | 3         | `"a"`     | `"a"` (len=1)         | `"ad"` (no match)      | 1             | ❌ (no change)     | 0       |
# | 4         | `"d"`     | `"d"` (len=1)         | —                      | 1             | ❌ (no change)     | 0       |


def test_solution():
    sol = Solution()

    # Test case 1
    result1 = sol.longestPalindrome("babad")
    print(f"Input: 'babad' -> Output: '{result1}'")
    assert result1 == "bab" or result1 == "aba"

    # Test case 2
    result2 = sol.longestPalindrome("cbbd")
    print(f"Input: 'cbbd' -> Output: '{result2}'")
    assert result2 == "bb"

    # Additional test cases
    result3 = sol.longestPalindrome("a")
    print(f"Input: 'a' -> Output: '{result3}'")
    assert result3 == "a"

    result4 = sol.longestPalindrome("ac")
    print(f"Input: 'ac' -> Output: '{result4}'")
    assert result4 == "a" or result4 == "c"

    result5 = sol.longestPalindrome("racecar")
    print(f"Input: 'racecar' -> Output: '{result5}'")
    assert result5 == "racecar"

    result6 = sol.longestPalindrome("noon")
    print(f"Input: 'noon' -> Output: '{result6}'")
    assert result6 == "noon"

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()