# https://leetcode.com/problems/longest-substring-without-repeating-characters
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}  # Dictionary to store the last index of each character
        left = 0  # Left pointer of the sliding window
        max_length = 0

        for right in range(len(s)):
            # If character is already in window, move left pointer
            if s[right] in char_index and char_index[s[right]] >= left:
                left = char_index[s[right]] + 1

            # Update the last seen index of current character
            char_index[s[right]] = right

            # Update max length
            max_length = max(max_length, right - left + 1)

        return max_length

# s1 = "abcabcbb"
# | right | s\[right] | char\_index        | left | max\_length |
# | ----- | --------- | ------------------ | ---- | ----------- |
# | 0     | a         | {a:0}              | 0    | 1           |
# | 1     | b         | {a:0, b:1}         | 0    | 2           |
# | 2     | c         | {a:0, b:1, c:2}    | 0    | 3           |
# | 3     | a         | {a:0,...} ⇒ left=1 | 1    | 3           |
# | 4     | b         | {b:4,...} ⇒ left=2 | 2    | 3           |
# | 5     | c         | {c:5,...} ⇒ left=3 | 3    | 3           |
# | 6     | b         | {b:6,...} ⇒ left=5 | 5    | 2           |
# | 7     | b         | {b:7,...} ⇒ left=7 | 7    | 1           |



# Consider the string `s = "abca"`.

# | i (right) | s\[i] | left | char\_index     | Explanation                                                                                       |
# | --------- | ----- | ---- | --------------- | ------------------------------------------------------------------------------------------------- |
# | 0         | a     | 0    | {a:0}           | First character → `max_length = 1`                                                                |
# | 1         | b     | 0    | {a:0, b:1}      | No duplicate → `max_length = 2`                                                                   |
# | 2         | c     | 0    | {a:0, b:1, c:2} | No duplicate → `max_length = 3`                                                                   |
# | 3         | a     | 0    | {a:0, b:1, c:2} | `a` is already in `char_index`, and `char_index[a] = 0 >= left = 0`, so update `left = 0 + 1 = 1` |

# 🧠 This means the substring changes to `"bca"`, removing the duplicate.

# **👉 The purpose of this line is:**

# > When a duplicate character appears, the current substring becomes invalid, so we update the start index (`left`) to the position right after the last occurrence of the duplicate character.


def test_solution():
    sol = Solution()

    # Test case 1: Example 1
    s1 = "abcabcbb"
    result1 = sol.lengthOfLongestSubstring(s1)
    print(f"Input: s = \"{s1}\"")
    print(f"Output: {result1}")
    print(f"Expected: 3")
    print(f"Explanation: The answer is \"abc\", with the length of 3.")
    print()

    # Test case 2: Example 2
    s2 = "bbbbb"
    result2 = sol.lengthOfLongestSubstring(s2)
    print(f"Input: s = \"{s2}\"")
    print(f"Output: {result2}")
    print(f"Expected: 1")
    print(f"Explanation: The answer is \"b\", with the length of 1.")
    print()

    # Test case 3: Example 3
    s3 = "pwwkew"
    result3 = sol.lengthOfLongestSubstring(s3)
    print(f"Input: s = \"{s3}\"")
    print(f"Output: {result3}")
    print(f"Expected: 3")
    print(f"Explanation: The answer is \"wke\", with the length of 3.")
    print()

    # Additional test cases
    # Test case 4: Empty string
    s4 = ""
    result4 = sol.lengthOfLongestSubstring(s4)
    print(f"Input: s = \"{s4}\"")
    print(f"Output: {result4}")
    print(f"Expected: 0")
    print()

    # Test case 5: Single character
    s5 = "a"
    result5 = sol.lengthOfLongestSubstring(s5)
    print(f"Input: s = \"{s5}\"")
    print(f"Output: {result5}")
    print(f"Expected: 1")
    print()

    # Test case 6: All unique characters
    s6 = "abcdef"
    result6 = sol.lengthOfLongestSubstring(s6)
    print(f"Input: s = \"{s6}\"")
    print(f"Output: {result6}")
    print(f"Expected: 6")
    print()

    # Test case 7: With spaces and symbols
    s7 = "a b!a"
    result7 = sol.lengthOfLongestSubstring(s7)
    print(f"Input: s = \"{s7}\"")
    print(f"Output: {result7}")
    print(f"Expected: 3")
    print()

if __name__ == "__main__":
    test_solution()